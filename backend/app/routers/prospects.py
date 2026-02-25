from fastapi import APIRouter, HTTPException, Depends

from app.config import Settings, get_settings
from app.models import ProspectRequest, ProspectBrief
from app.services.linkedin import fetch_linkedin_profile
from app.services.news import fetch_company_news
from app.services.synthesis import generate_brief

router = APIRouter()


@router.post("/prospect", response_model=ProspectBrief)
async def create_prospect_brief(
    request: ProspectRequest,
    settings: Settings = Depends(get_settings),
):
    # 1. Fetch LinkedIn profile
    profile = await fetch_linkedin_profile(request.linkedin_url, settings)
    if not profile.full_name:
        raise HTTPException(status_code=404, detail="Could not retrieve LinkedIn profile")

    # 2. Fetch recent news about the company
    news = await fetch_company_news(profile.company, settings)

    # 3. Synthesize brief with Claude
    brief = await generate_brief(profile, news, settings)

    return brief
