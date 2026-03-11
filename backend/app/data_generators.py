"""
Data aggregation helpers for the Subscription Ecosystem Dashboard.
Computes summary views from the raw sample data for API responses.
"""

from app.sample_data import (
    SUBSCRIBERS,
    BEHAVIORAL_DATA,
    CHURN_PREDICTIONS,
    REVENUE_FORECAST,
)


def compute_kpi_summary():
    """Top-line KPI metrics for the dashboard header."""
    paying = [s for s in SUBSCRIBERS if s["monthly_rate"] > 0 and s["status"] == "active"]
    all_active = [s for s in SUBSCRIBERS if s["status"] in ("active", "trial")]
    total = len(SUBSCRIBERS)

    mrr = sum(s["monthly_rate"] for s in paying)
    active_rate = len(all_active) / total * 100 if total else 0
    arpu = mrr / len(paying) if paying else 0

    engagement_scores = [BEHAVIORAL_DATA[s["id"]]["engagement_score"] for s in all_active if s["id"] in BEHAVIORAL_DATA]
    avg_engagement = sum(engagement_scores) / len(engagement_scores) if engagement_scores else 0

    churned = len([s for s in SUBSCRIBERS if s["status"] == "churned"])
    churn_rate = churned / total * 100 if total else 0

    return {
        "mrr": round(mrr, 2),
        "total_subscribers": total,
        "active_rate": round(active_rate, 1),
        "arpu": round(arpu, 2),
        "avg_engagement": round(avg_engagement, 1),
        "churn_rate": round(churn_rate, 1),
    }


def compute_status_distribution():
    """Count subscribers by status for doughnut chart."""
    counts = {}
    for s in SUBSCRIBERS:
        counts[s["status"]] = counts.get(s["status"], 0) + 1
    return counts


def compute_tier_distribution():
    """Count subscribers by plan tier for doughnut chart."""
    counts = {}
    for s in SUBSCRIBERS:
        counts[s["plan_tier"]] = counts.get(s["plan_tier"], 0) + 1
    return counts


def compute_engagement_vs_churn():
    """Engagement score vs churn risk pairs for scatter plot."""
    points = []
    for s in SUBSCRIBERS:
        sid = s["id"]
        if sid in BEHAVIORAL_DATA and sid in CHURN_PREDICTIONS:
            points.append({
                "id": sid,
                "name": s["name"],
                "engagement_score": BEHAVIORAL_DATA[sid]["engagement_score"],
                "risk_score": CHURN_PREDICTIONS[sid]["risk_score"],
                "risk_level": CHURN_PREDICTIONS[sid]["risk_level"],
                "plan_tier": s["plan_tier"],
                "status": s["status"],
            })
    return points


def compute_monthly_metrics():
    """Combined time-series data for the revenue forecast line chart."""
    return {
        "historical": REVENUE_FORECAST["historical"],
        "projected_baseline": REVENUE_FORECAST["projected_baseline"],
        "projected_ai_enhanced": REVENUE_FORECAST["projected_ai_enhanced"],
    }


# ---------------------------------------------------------------------------
# TODO(human): Implement analyze_churn_factors
#
# This function should take a subscriber's behavioral data dict and return
# a list of human-readable strings describing why this subscriber might
# churn. The current dashboard uses hardcoded factors from sample_data.py,
# but this function would enable dynamic, rule-based churn analysis.
#
# Parameters:
#   behavior (dict): A single entry from BEHAVIORAL_DATA, e.g.:
#     {"avg_sessions_per_week": 2.1, "newsletters_opened_pct": 28,
#      "engagement_score": 38, "paywall_hits_per_week": 1, ...}
#
# Returns:
#   list[str]: Contributing factors, e.g.:
#     ["Session frequency below 2x/week", "Newsletter opens under 20%"]
# ---------------------------------------------------------------------------
def analyze_churn_factors(behavior):
    """Analyze behavioral data and return churn risk contributing factors.

    Replace this placeholder with rule-based logic that identifies
    which specific behaviors signal churn risk in an investment advisory context.
    """
    return []
