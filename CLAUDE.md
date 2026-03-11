# AI-Powered Subscription Ecosystem Dashboard + ICP Research Tool

## Project Overview
Sales demo dashboard for PerformanceLabs with an ICP (Ideal Customer Profile) research tool that uses Claude to extract structured customer profiles from conversation, searches Apollo for matching prospects, and scores account fit.

## Tech Stack
- Backend: Python 3.11+, FastAPI, SQLAlchemy (async), PostgreSQL, Redis
- Frontend: Vanilla JS (ES modules), Chart.js 4, Vite, custom CSS
- AI: Anthropic Claude API via agent framework
- External APIs: Apollo.io (prospect search)
- Infra: Docker Compose (PostgreSQL + Redis), Alembic migrations

## Key Commands
- Backend: `cd backend && uvicorn app.main:app --reload --port 8000`
- Frontend: `cd frontend && npm run dev`
- Tests: `cd backend && python -m pytest tests/ -v`
- Build: `cd frontend && npm run build`
- Database: `docker compose up -d` then `cd backend && alembic upgrade head`

## Architecture

### Dashboard (sample data)
- `backend/app/main.py` — FastAPI app with dashboard + ICP routes
- `backend/app/sample_data.py` — Hardcoded demo data (50 subscribers)
- `backend/app/data_generators.py` — Aggregation helpers

### ICP Research (Phase 1)
- `backend/app/routes/icp.py` — CRUD + `/conversation` endpoint
- `backend/app/models/icp.py` — SQLAlchemy model (UUID PK, JSON criteria/weights)
- `backend/app/schemas/icp.py` — Pydantic request/response schemas
- `backend/app/services/apollo.py` — Apollo.io client with tenacity retry
- `backend/app/services/scoring.py` — ICP fit scoring (0-1 scale)

### Agent Framework
- `backend/agents/base/agent.py` — BaseAgent (owns AsyncAnthropic client)
- `backend/agents/base/tool.py` — BaseTool (receives client via DI)
- `backend/agents/icp_architect/agent.py` — ICPArchitect agent
- `backend/agents/icp_architect/tools/extract_criteria.py` — Claude ICP extraction
- `backend/agents/icp_architect/prompts/ingestion.txt` — System prompt

### Tests
- `backend/tests/test_main.py` — Dashboard endpoint tests
- `backend/tests/test_icp_routes.py` — ICP CRUD tests (async, in-memory SQLite)
- `backend/tests/test_scoring.py` — Scoring unit tests

## API Endpoints
| Endpoint | Purpose |
|----------|---------|
| `GET /api/dashboard/kpis` | MRR, subscribers, active rate, ARPU, engagement, churn |
| `GET /api/subscribers` | Status/tier distributions + snapshot table |
| `GET /api/churn` | Scatter data + risk distribution + high-risk list |
| `GET /api/segments` | 6 AI behavioral segments with radar data |
| `GET /api/recommendations` | Upsell/retention per segment with revenue impact |
| `GET /api/revenue-forecast` | Historical + projected MRR (baseline vs AI-enhanced) |
| `GET /api/retention-actions` | AI agent action log with timeline data |
| `GET /api/icp/` | List ICP models (optional `is_active` filter) |
| `POST /api/icp/` | Create ICP model |
| `GET /api/icp/{id}` | Get single ICP model |
| `PATCH /api/icp/{id}` | Update ICP model |
| `POST /api/icp/{id}/activate` | Activate ICP model (deactivates others) |
| `POST /api/icp/conversation` | Claude-powered ICP extraction from natural language |

## Conventions
- Dashboard uses pure sample data — no external API calls needed
- ICP features require PostgreSQL (via Docker) and ANTHROPIC_API_KEY
- Agent tools receive `anthropic.AsyncAnthropic` client via constructor (DI)
- Frontend uses vanilla JS with ES modules (no React)
- Vite proxies /api to backend at localhost:8000
