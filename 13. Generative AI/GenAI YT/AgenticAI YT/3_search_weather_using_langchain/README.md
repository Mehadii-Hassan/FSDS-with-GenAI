# ⚡ Agentic AI Cognitive Search & Weather Engine

A professional, tech-forward web application built with **FastAPI**, **LangChain (v0.1 Environment)**, and **Groq Cloud API**. This application initializes an autonomous AI Agent powered by **Llama 3.1 8B**, utilizing custom tools to search the web and fetch live weather data dynamically.

The system features a modern, glassmorphic frontend UI dashboard built with native JavaScript, CSS variables, and clean layout animations.

---

## 🚀 Key Features

*   **Autonomous ReAct Agent:** Utilizes LangChain's reasoning-and-action framework to break down complex user multi-step tasks.
*   **Groq Llama 3.1 Acceleration:** Ultra-fast, low-latency text completion and tool assignment on a lightweight parameter footprint.
*   **Custom Weather API Tool:** Directly connects with the WeatherSTACK API engine to securely extract live conditions (temperature, humidity, description) for any global city.
*   **Tavily Web Search Tool:** Gives the agent live web browsing capabilities to cross-reference general facts (e.g., finding country capitals).
*   **FastAPI Backend Architecture:** Clean, async-first Python API structure serving static frontend visual layers natively.
*   **Modern Visual Interface:** Fluid layout built with modern CSS properties, crisp loading indicators, adaptive execution tags, and responsive viewport padding constraints.

---

## 🛠️ Installation & Setup Guide

### 1. Environment Prerequisite
Ensure you have Python 3.10 or 3.11 installed inside an isolated workspace framework (like Anaconda or `venv`).

### 2. Clone or Enter Project Folder
Open your terminal window (e.g., MINGW64 Git Bash) and head directly into your codebase root:
```bash
cd "Desktop/FSDS with Gen AI/FSDS-with-GenAI/11. Deep Learning/3. RNN/GenAI YT/AgenticAI YT/3_search_weather_using_langchain"
```

### 3. Install Target Dependencies
Update your local system libraries securely matching the framework runtime parameters using:
```bash

conda create -n s_weather python=3.11 -y
conda activate s_weather
pip install -r requirements.txt

```

### 4. Create and Configure Environment Secrets
Create a file named `.env` in your root project directory. Open it in a text editor and provide your valid endpoint API security strings:

```env
GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
WEATHERSTACK_API_KEY="your_weatherstack_api_key_here"
```
> **Note:** Access credentials safely across respective official administration portals: [Groq Console](https://groq.com), [Tavily AI Dash](https://tavily.com), and [WeatherStack Dashboard](https://weatherstack.com).

---

## ⚡ Execution Operations

Launch your application framework server engine via `uvicorn` using the exact syntax mapping below:

```bash
uvicorn app:app --reload
```

*   `app` (left of the colon): Targets your core script file named `app.py`.
*   `app` (right of the colon): Initializes the web framework instance object `app = FastAPI()`.
*   `--reload`: Activates Hot-Reload monitoring to refresh application pipelines immediately upon code modifications.

Once the terminal outputs `INFO: Uvicorn running on http://127.0.0.1:8000`, open your browser of choice and interact directly with your environment dashboards!

---

## 🖥️ UI Client Usage Example

1. Open your browser to `http://127.0.0.1:8000`.
2. Enter a compound multi-layered inquiry into the interactive query element:
   *   *Example:* `"Find the capital of India and then find its current weather."*
3. Click **Execute Agent**.
4. The loader indicator activates while the console streams the autonomous agent's thinking iterations behind the scenes, cleanly populating the final response metrics block upon successful completion!

---

## 🛠️ Troubleshooting Matrix

*   **Error 413 (Rate Limit Exceeded):** Free tiers limit the massive `llama-3.3-70b-versatile` model to 12,000 TPM. The code is pre-configured to use `llama-3.1-8b-instant` to stay safely below this restriction.
*   **Tool choice is none Error:** This occurs due to payload syntax parsing updates on newer Groq configurations. Ensure your drivers stay aligned by running `pip install -U langchain-groq`.
*   **CSS Style Warnings:** The code handles both `-webkit-background-clip: text` syntax triggers alongside modern standard fallback variables (`background-clip: text`) to completely bypass modern code linter warnings.
