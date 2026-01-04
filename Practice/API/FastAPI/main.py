from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI() #server initilization

teas = []

@app.get("/")
def read_root():
    return {"message" : "welcome to the Tea House"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

