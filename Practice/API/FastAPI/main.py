from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI() #server initilization

class Tea(BaseModel):
    id : int
    name : str
    origin : str 

teas : List[Tea] = []

@app.get("/")
def read_root():
    return {"message" : "welcome to the Tea House"}

@app.get("/teas")
def get_teas():
    return teas

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

