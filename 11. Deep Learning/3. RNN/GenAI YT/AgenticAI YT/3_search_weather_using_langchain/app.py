import os
import certifi
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# LangChain imports
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# ==========================================
# ENV VARIABLES & SSL SETUP
# ==========================================
os.environ["SSL_CERT_FILE"] = certifi.where()
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

# ==========================================
# INITIALIZE TOOLS & AGENT COMPONENTS
# ==========================================
search_tool = TavilySearchResults(max_results=1)

@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather information for a city."""
    url = f"https://weatherstack.com{WEATHERSTACK_API_KEY}&query={city}"
    try:
        response = requests.get(url)
        data = response.json()
        if "current" not in data:
            return f"Could not fetch weather data for {city}"
        return (
            f"City: {city}\n"
            f"Temperature: {data['current']['temperature']}°C\n"
            f"Weather: {data['current']['weather_descriptions'][0]}\n"
            f"Humidity: {data['current']['humidity']}%"
        )
    except Exception as e:
        return f"Error gathering weather data: {str(e)}"

llm = ChatGroq(
    model="llama-3.3-11b-vision-instant",
    temperature=0,
    api_key=GROQ_API_KEY
)
prompt = hub.pull("hwchase17/react")
tools = [search_tool, get_weather_data]

#create react agent
agent = create_react_agent(
    llm=llm, 
    tools=tools, 
    prompt=prompt
)
#create agent executor
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True  # This catches and heals the exact error you received
)

# ==========================================
# FASTAPI APP CONFIGURATION
# ==========================================
app = FastAPI(title="Agentic AI Weather & Search Service")

# Mount the static directory to serve CSS and JS assets
app.mount("/static", StaticFiles(directory="static"), name="static")

class QueryRequest(BaseModel):
    user_input: str

# Serve the main dashboard frontend page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("templates/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Frontend templates/index.html file missing.")

# POST endpoint for our frontend Javascript to target
@app.post("/ask-agent")
async def ask_agent(request: QueryRequest):
    if not request.user_input.strip():
        raise HTTPException(status_code=400, detail="Query cannot be blank.")
    try:
        result = agent_executor.invoke({"input": request.user_input})
        return {
            "query": request.user_input,
            "agent_response": result.get("output", "No response generated.")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
