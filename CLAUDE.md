# Prospect Brief Generator

## Project Overview
Sales tool: paste a LinkedIn URL, get an AI-generated prospect brief with talking points and icebreakers.

## Tech Stack
- Backend: Python 3.11+, FastAPI, httpx, Anthropic SDK
- Frontend: React 19, Vite, Tailwind CSS
- APIs: Proxycurl (LinkedIn), NewsAPI (news), Claude (synthesis)

## Key Commands
- Backend: `cd backend && uvicorn app.main:app --reload --port 8000`
- Frontend: `cd frontend && npm run dev`
- Install backend deps: `cd backend && pip install -r requirements.txt`
- Install frontend deps: `cd frontend && npm install`

## Architecture
- `backend/app/main.py` — FastAPI entry point with CORS
- `backend/app/routers/prospects.py` — POST /api/prospect endpoint
- `backend/app/services/linkedin.py` — Proxycurl API client
- `backend/app/services/news.py` — NewsAPI client
- `backend/app/services/synthesis.py` — Claude brief generation
- `backend/app/models.py` — Pydantic models for all data
- `backend/app/config.py` — Settings from .env

## Conventions
- Use async/await throughout backend services
- Pydantic models for all request/response schemas
- Frontend uses functional components with hooks
- Vite proxies /api to backend at localhost:8000
