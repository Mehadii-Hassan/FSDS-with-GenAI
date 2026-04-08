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


@app.post("/addteas")
def add_tea(tea : Tea):
    teas.append(tea)
    return tea


@app.put("/updatetea/{tea_id}")
def update_tea(tea_id : int, updated_tea : Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}


@app.delete("/deletetea/{tea_id}")
def delete_tea(tea_id : int):
    for index, tea in enumerate(teas):
        if tea_id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error" : "Tea not found"}


@app.get("/getteas")
def get_teas():
    return teas

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

