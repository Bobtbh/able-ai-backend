from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Backend is live"}

@app.post("/generate")
def generate(request: PromptRequest):
    return {"response": f"You said: {request.prompt}"}
