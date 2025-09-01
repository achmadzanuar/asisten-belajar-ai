from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Setup Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "Pong from Backend!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Halo {name}, selamat datang di Backend AI!"}

# 🔹 Endpoint rekomendasi dengan Gemini
@app.get("/rekomendasi")
def rekomendasi(keyword: str = Query(..., description="Keyword untuk rekomendasi")):
    prompt = f"Buatkan 5 rekomendasi terbaik untuk: {keyword}, jelaskan secara singkat."
    response = model.generate_content(prompt)
    return {"keyword": keyword, "rekomendasi": response.text}
