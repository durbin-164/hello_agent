from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.post("/welcome")
async def welcome(request: NameRequest):
    return {"message": f"Welcome {request.name}"}
