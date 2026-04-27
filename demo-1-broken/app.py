from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/chat")
def chat(prompt: str):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    })
    return res.json()
