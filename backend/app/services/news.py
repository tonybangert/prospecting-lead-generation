import httpx

from app.config import Settings
from app.models import NewsArticle


async def fetch_company_news(company_name: str, settings: Settings) -> list[NewsArticle]:
    """Fetch recent news articles about a company via NewsAPI."""
    if not company_name:
        return []

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.newsapi_base_url}/everything",
            params={
                "q": company_name,
                "sortBy": "publishedAt",
                "pageSize": 5,
                "language": "en",
            },
            headers={"X-Api-Key": settings.newsapi_key},
            timeout=15.0,
        )

    if response.status_code != 200:
        return []

    data = response.json()
    articles = data.get("articles", [])

    return [
        NewsArticle(
            title=a.get("title", ""),
            description=a.get("description", ""),
            source=a.get("source", {}).get("name", ""),
            url=a.get("url", ""),
            published_at=a.get("publishedAt", ""),
        )
        for a in articles
    ]
