from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import prospects

app = FastAPI(
    title="Prospect Brief Generator",
    description="Generate sales briefs from LinkedIn profiles",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prospects.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
