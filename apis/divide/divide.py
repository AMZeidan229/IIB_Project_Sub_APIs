from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List , Any


app = FastAPI()

class REQUEST_MODEL(BaseModel):
    numsdiv: List[Any]

class RESPONSE_MODEL(BaseModel):
    op_str : str
    divide: int | float

class ERROR_MODEL(BaseModel):
    error: str


@app.post("/divide")
async def create_item(request: REQUEST_MODEL):
    op_string = "/".join([str(i) for i in request.numsdiv])
    
    if 0 in request.numsdiv and request.numsdiv.index(0) != 0 :
        return ERROR_MODEL(error="Cannot divide by zero")
    
    for element in request.numsdiv:
        if isinstance(element, bool):
            return ERROR_MODEL(error="List contains non numeric data")
        
        if not isinstance(element, (int,float)):
            return ERROR_MODEL(error="List contains non numeric data")
        

    
    return RESPONSE_MODEL(op_str=op_string , divide=eval(op_string))

if __name__ == "__divide__":
    uvicorn.run("divide:app", host="127.0.0.1", port=8040)