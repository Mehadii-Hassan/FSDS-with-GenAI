from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI() #server initilization

@app.get("/")
def read_root():
    return {"Hello" : "world"}

