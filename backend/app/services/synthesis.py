import anthropic
import json

from app.config import Settings
from app.models import LinkedInProfile, NewsArticle, ProspectBrief


SYSTEM_PROMPT = """You are a sales research assistant. Given a prospect's LinkedIn profile and recent company news, generate a concise sales brief.

Return valid JSON with these fields:
- "summary": A 2-3 sentence overview of who this person is and their role
- "talking_points": A list of 3-5 relevant conversation starters based on their background
- "icebreakers": A list of 2-3 personalized icebreaker messages for outreach"""


async def generate_brief(
    profile: LinkedInProfile,
    news: list[NewsArticle],
    settings: Settings,
) -> ProspectBrief:
    """Use Claude to synthesize a prospect brief from profile + news data."""
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)

    user_message = _build_user_message(profile, news)

    response = await client.messages.create(
        model=settings.claude_model,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    raw_text = response.content[0].text
    parsed = _parse_response(raw_text)

    return ProspectBrief(
        profile=profile,
        news=news,
        summary=parsed.get("summary", ""),
        talking_points=parsed.get("talking_points", []),
        icebreakers=parsed.get("icebreakers", []),
        raw_synthesis=raw_text,
    )


def _build_user_message(profile: LinkedInProfile, news: list[NewsArticle]) -> str:
    parts = [
        f"## Prospect Profile",
        f"**Name**: {profile.full_name}",
        f"**Headline**: {profile.headline}",
        f"**Company**: {profile.company}",
        f"**Industry**: {profile.industry}",
        f"**Location**: {profile.location}",
        f"**Summary**: {profile.summary}",
    ]

    if profile.experiences:
        parts.append("\n## Recent Experience")
        for exp in profile.experiences[:3]:
            company = exp.get("company", "Unknown")
            title = exp.get("title", "Unknown")
            parts.append(f"- {title} at {company}")

    if news:
        parts.append("\n## Recent Company News")
        for article in news:
            parts.append(f"- **{article.title}** ({article.source}): {article.description}")

    return "\n".join(parts)


def _parse_response(text: str) -> dict:
    """Extract JSON from Claude's response, handling markdown code fences."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        lines = lines[1:]  # Remove opening fence
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]  # Remove closing fence
        cleaned = "\n".join(lines)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"summary": text, "talking_points": [], "icebreakers": []}
