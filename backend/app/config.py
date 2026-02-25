from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    anthropic_api_key: str = ""
    proxycurl_api_key: str = ""
    newsapi_key: str = ""

    # Model selection
    claude_model: str = "claude-sonnet-4-5-20250929"

    # API base URLs
    proxycurl_base_url: str = "https://nubela.co/proxycurl/api/v2"
    newsapi_base_url: str = "https://newsapi.org/v2"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
