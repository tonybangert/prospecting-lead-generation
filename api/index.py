"""Vercel serverless entry point — re-exports the FastAPI app."""
import sys
from pathlib import Path

# Add backend to Python path so `from app.xxx import ...` works
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from app.main import app  # noqa: E402, F401
