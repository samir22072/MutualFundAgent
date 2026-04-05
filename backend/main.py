from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

from crew import setup_crew
from models import ChatRequest, ChatResponse
import uvicorn

app = FastAPI(title="Mutual Funds Advisor API")

frontend_url = os.environ.get("FRONTEND_URL", "http://localhost:3000")

# Configure CORS to allow Next.js app to fetch
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    if not req.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    if not os.environ.get("GOOGLE_API_KEY"):
        raise HTTPException(status_code=500, detail="GOOGLE_API_KEY environment variable is missing")

    try:
        crew = setup_crew(req.query)
        result = crew.kickoff()
        return ChatResponse(response=result.raw)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
