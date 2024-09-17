from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List , Any


app = FastAPI()

class REQUEST_MODEL(BaseModel):
    numsmult: List[Any]

class RESPONSE_MODEL(BaseModel):
    op_str : str
    multiply: int | float

class ERROR_MODEL(BaseModel):
    error: str

@app.post("/multiply")
async def create_item(request: REQUEST_MODEL):
    op_string = "*".join([str(i) for i in request.numsmult])
    result = eval(op_string)

    for element in request.numsmult:
        if isinstance(element, bool):
            return ERROR_MODEL(error="List contains non numeric data")
        
        if not isinstance(element, (int,float)):
            return ERROR_MODEL(error="List contains non numeric data")

    return RESPONSE_MODEL(op_str=op_string , multiply=result)

if __name__ == "__multiply__":
    uvicorn.run("multiply:app", host="127.0.0.1", port=8030)