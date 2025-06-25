from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_code(data: PromptRequest):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "user", "content": data.prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    response.raise_for_status()
    result = response.json()
    return {
        "response": result["choices"][0]["message"]["content"]
    }
