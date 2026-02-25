from pydantic import BaseModel, HttpUrl
from typing import Optional


class ProspectRequest(BaseModel):
    linkedin_url: str


class LinkedInProfile(BaseModel):
    full_name: str = ""
    headline: str = ""
    summary: str = ""
    occupation: str = ""
    company: str = ""
    industry: str = ""
    location: str = ""
    experiences: list[dict] = []
    education: list[dict] = []
    skills: list[str] = []


class NewsArticle(BaseModel):
    title: str
    description: str = ""
    source: str = ""
    url: str = ""
    published_at: str = ""


class ProspectBrief(BaseModel):
    profile: LinkedInProfile
    news: list[NewsArticle] = []
    summary: str = ""
    talking_points: list[str] = []
    icebreakers: list[str] = []
    raw_synthesis: str = ""
