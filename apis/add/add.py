from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List , Any


app = FastAPI()

class REQUEST_MODEL(BaseModel):
    numsum: List[Any]

class RESPONSE_MODEL(BaseModel):
    op_str : str
    sum: int | float

class ERROR_MODEL(BaseModel):
    error: str

@app.post("/add")
async def create_item(request: REQUEST_MODEL):
    op_string = "+".join([str(i) for i in request.numsum])
    result = eval(op_string)

    for element in request.numsum:
        if isinstance(element, bool):
            return ERROR_MODEL(error="List contains non numeric data")
        
        if not isinstance(element, (int , float)):
            return ERROR_MODEL(error="List contains non numeric data")

    return RESPONSE_MODEL(op_str=op_string , sum=result)

if __name__ == "__add__":
    uvicorn.run("add:app", host="127.0.0.1", port=8010)