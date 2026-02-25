import httpx

from app.config import Settings
from app.models import LinkedInProfile


async def fetch_linkedin_profile(linkedin_url: str, settings: Settings) -> LinkedInProfile:
    """Fetch a LinkedIn profile via the Proxycurl API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.proxycurl_base_url}/linkedin",
            params={"url": linkedin_url},
            headers={"Authorization": f"Bearer {settings.proxycurl_api_key}"},
            timeout=30.0,
        )

    if response.status_code != 200:
        return LinkedInProfile()

    data = response.json()

    return LinkedInProfile(
        full_name=data.get("full_name", ""),
        headline=data.get("headline", ""),
        summary=data.get("summary", ""),
        occupation=data.get("occupation", ""),
        company=_extract_current_company(data),
        industry=data.get("industry", ""),
        location=_format_location(data),
        experiences=data.get("experiences", []) or [],
        education=data.get("education", []) or [],
        skills=_extract_skills(data),
    )


def _extract_current_company(data: dict) -> str:
    experiences = data.get("experiences") or []
    for exp in experiences:
        if exp.get("ends_at") is None:
            return exp.get("company", "")
    return experiences[0].get("company", "") if experiences else ""


def _format_location(data: dict) -> str:
    parts = [data.get("city"), data.get("state"), data.get("country_full_name")]
    return ", ".join(p for p in parts if p)


def _extract_skills(data: dict) -> list[str]:
    return [s if isinstance(s, str) else s.get("name", "") for s in (data.get("skills") or [])]
