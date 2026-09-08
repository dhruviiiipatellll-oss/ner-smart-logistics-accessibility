from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="NER Smart Logistics & Accessibility Platform",
    description="AI-powered healthcare logistics and accessibility intelligence",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "NER Smart Logistics Platform"}

@app.get("/")
async def root():
    return {
        "message": "Welcome to NER Smart Logistics & Accessibility Platform",
        "version": "0.1.0",
        "endpoints": {
            "health": "/health",
            "facilities": "/api/v1/facilities",
            "routing": "/api/v1/routing",
            "accessibility": "/api/v1/accessibility",
            "patients": "/api/v1/patients"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)