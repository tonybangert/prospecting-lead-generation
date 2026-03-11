"""
Sample data for the AI-Powered Subscription Ecosystem Dashboard.
The Motley Fool investment advisory demo data for PerformanceLabs.

50 subscribers with demographics, subscription details, behavioral data,
AI-generated churn predictions, segments, recommendations, revenue
forecasts, and automated retention actions.

Tiers & Annual Pricing:
  - Free (Fool.com): $0
  - Stock Advisor: $199/yr ($16.58/mo)
  - Rule Breakers: $299/yr ($24.92/mo)
  - Epic: $499/yr ($41.58/mo)
  - Epic Plus: $1,999/yr ($166.58/mo)
  - Fool One: $13,999/yr ($1,166.58/mo)
"""

# ---------------------------------------------------------------------------
# SUBSCRIBERS (50 total)
# Distribution: ~60% active, ~14% churned, ~10% paused, ~16% trial
# ---------------------------------------------------------------------------

SUBSCRIBERS = [
    # ── Active subscribers (30) ──────────────────────────────────────────
    {"id": 1, "name": "Sarah Chen", "email": "sarah.chen@email.com", "age_range": "25-34", "market": "New York", "source": "organic", "device_preference": "mobile", "plan_tier": "Epic", "status": "active", "start_date": "2024-03-10", "tenure_months": 24, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 1497.00, "total_paid": 998.00},
    {"id": 2, "name": "Michael Torres", "email": "michael.torres@email.com", "age_range": "35-44", "market": "Los Angeles", "source": "referral", "device_preference": "desktop", "plan_tier": "Fool One", "status": "active", "start_date": "2023-03-01", "tenure_months": 36, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 1166.58, "ltv": 62996.00, "total_paid": 41997.00},
    {"id": 3, "name": "Jessica Williams", "email": "jessica.w@email.com", "age_range": "45-54", "market": "Chicago", "source": "organic", "device_preference": "desktop", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2024-09-15", "tenure_months": 18, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 597.00, "total_paid": 398.00},
    {"id": 4, "name": "David Kim", "email": "david.kim@email.com", "age_range": "25-34", "market": "Boston", "source": "promotion", "device_preference": "mobile", "plan_tier": "Epic", "status": "active", "start_date": "2025-03-20", "tenure_months": 12, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 749.00, "total_paid": 499.00},
    {"id": 5, "name": "Amanda Foster", "email": "amanda.foster@email.com", "age_range": "55-64", "market": "Washington DC", "source": "organic", "device_preference": "tablet", "plan_tier": "Fool One", "status": "active", "start_date": "2022-03-05", "tenure_months": 48, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 1166.58, "ltv": 83994.00, "total_paid": 55996.00},
    {"id": 6, "name": "Robert Johnson", "email": "rob.johnson@email.com", "age_range": "35-44", "market": "New York", "source": "referral", "device_preference": "desktop", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2023-09-01", "tenure_months": 30, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 896.00, "total_paid": 597.00},
    {"id": 7, "name": "Emily Nakamura", "email": "emily.n@email.com", "age_range": "18-24", "market": "San Francisco", "source": "organic", "device_preference": "mobile", "plan_tier": "Free", "status": "active", "start_date": "2025-09-10", "tenure_months": 6, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},
    {"id": 8, "name": "James O'Brien", "email": "james.obrien@email.com", "age_range": "45-54", "market": "Philadelphia", "source": "promotion", "device_preference": "desktop", "plan_tier": "Epic", "status": "active", "start_date": "2024-07-12", "tenure_months": 20, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 1497.00, "total_paid": 998.00},
    {"id": 9, "name": "Maria Garcia", "email": "maria.garcia@email.com", "age_range": "25-34", "market": "Miami", "source": "organic", "device_preference": "mobile", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2025-01-08", "tenure_months": 14, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 597.00, "total_paid": 398.00},
    {"id": 10, "name": "Christopher Lee", "email": "chris.lee@email.com", "age_range": "35-44", "market": "Seattle", "source": "referral", "device_preference": "desktop", "plan_tier": "Fool One", "status": "active", "start_date": "2022-09-15", "tenure_months": 42, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 1166.58, "ltv": 83994.00, "total_paid": 55996.00},
    {"id": 11, "name": "Rachel Patel", "email": "rachel.patel@email.com", "age_range": "25-34", "market": "Denver", "source": "organic", "device_preference": "mobile", "plan_tier": "Epic", "status": "active", "start_date": "2024-11-05", "tenure_months": 16, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 1497.00, "total_paid": 998.00},
    {"id": 12, "name": "Thomas Anderson", "email": "tom.anderson@email.com", "age_range": "55-64", "market": "Dallas", "source": "organic", "device_preference": "desktop", "plan_tier": "Rule Breakers", "status": "active", "start_date": "2023-03-20", "tenure_months": 36, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 24.92, "ltv": 1346.00, "total_paid": 897.00},
    {"id": 13, "name": "Sophia Martinez", "email": "sophia.m@email.com", "age_range": "18-24", "market": "New York", "source": "promotion", "device_preference": "mobile", "plan_tier": "Free", "status": "active", "start_date": "2025-12-01", "tenure_months": 3, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},
    {"id": 14, "name": "Daniel Wright", "email": "dan.wright@email.com", "age_range": "45-54", "market": "Atlanta", "source": "organic", "device_preference": "tablet", "plan_tier": "Epic", "status": "active", "start_date": "2023-11-10", "tenure_months": 28, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 2246.00, "total_paid": 1497.00},
    {"id": 15, "name": "Lauren Hughes", "email": "lauren.h@email.com", "age_range": "35-44", "market": "Portland", "source": "referral", "device_preference": "desktop", "plan_tier": "Epic Plus", "status": "active", "start_date": "2024-03-25", "tenure_months": 24, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 166.58, "ltv": 5997.00, "total_paid": 3998.00},
    {"id": 16, "name": "Kevin Murphy", "email": "kevin.murphy@email.com", "age_range": "25-34", "market": "Chicago", "source": "organic", "device_preference": "mobile", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2025-05-18", "tenure_months": 10, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 299.00, "total_paid": 199.00},
    {"id": 17, "name": "Ashley Thompson", "email": "ashley.t@email.com", "age_range": "35-44", "market": "Boston", "source": "organic", "device_preference": "desktop", "plan_tier": "Epic", "status": "active", "start_date": "2024-05-03", "tenure_months": 22, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 1497.00, "total_paid": 998.00},
    {"id": 18, "name": "Brian Zhao", "email": "brian.zhao@email.com", "age_range": "45-54", "market": "New York", "source": "referral", "device_preference": "desktop", "plan_tier": "Fool One", "status": "active", "start_date": "2021-09-01", "tenure_months": 54, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 1166.58, "ltv": 104993.00, "total_paid": 69995.00},
    {"id": 19, "name": "Megan Davis", "email": "megan.davis@email.com", "age_range": "25-34", "market": "Austin", "source": "organic", "device_preference": "mobile", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2025-07-22", "tenure_months": 8, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 299.00, "total_paid": 199.00},
    {"id": 20, "name": "Nathan Scott", "email": "nathan.scott@email.com", "age_range": "18-24", "market": "Los Angeles", "source": "promotion", "device_preference": "mobile", "plan_tier": "Free", "status": "active", "start_date": "2025-11-15", "tenure_months": 4, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},
    {"id": 21, "name": "Olivia Robinson", "email": "olivia.r@email.com", "age_range": "35-44", "market": "Washington DC", "source": "organic", "device_preference": "tablet", "plan_tier": "Epic", "status": "active", "start_date": "2023-07-14", "tenure_months": 32, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 2246.00, "total_paid": 1497.00},
    {"id": 22, "name": "Andrew Mitchell", "email": "andrew.m@email.com", "age_range": "55-64", "market": "San Francisco", "source": "organic", "device_preference": "desktop", "plan_tier": "Rule Breakers", "status": "active", "start_date": "2021-03-10", "tenure_months": 60, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 24.92, "ltv": 2243.00, "total_paid": 1495.00},
    {"id": 23, "name": "Hannah Lewis", "email": "hannah.lewis@email.com", "age_range": "25-34", "market": "Miami", "source": "referral", "device_preference": "mobile", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2025-03-05", "tenure_months": 12, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 299.00, "total_paid": 199.00},
    {"id": 24, "name": "Justin Clark", "email": "justin.clark@email.com", "age_range": "45-54", "market": "Seattle", "source": "organic", "device_preference": "desktop", "plan_tier": "Epic", "status": "active", "start_date": "2024-09-20", "tenure_months": 18, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 1497.00, "total_paid": 998.00},
    {"id": 25, "name": "Samantha Reed", "email": "sam.reed@email.com", "age_range": "35-44", "market": "Denver", "source": "organic", "device_preference": "mobile", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2024-01-12", "tenure_months": 26, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 896.00, "total_paid": 597.00},
    {"id": 26, "name": "Patrick Kennedy", "email": "pat.kennedy@email.com", "age_range": "25-34", "market": "Philadelphia", "source": "promotion", "device_preference": "desktop", "plan_tier": "Free", "status": "active", "start_date": "2024-01-20", "tenure_months": 14, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},
    {"id": 27, "name": "Victoria Nguyen", "email": "vicky.nguyen@email.com", "age_range": "18-24", "market": "New York", "source": "organic", "device_preference": "mobile", "plan_tier": "Free", "status": "active", "start_date": "2026-01-05", "tenure_months": 2, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},
    {"id": 28, "name": "Gregory Campbell", "email": "greg.campbell@email.com", "age_range": "45-54", "market": "Dallas", "source": "organic", "device_preference": "desktop", "plan_tier": "Epic Plus", "status": "active", "start_date": "2022-11-08", "tenure_months": 40, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 166.58, "ltv": 11994.00, "total_paid": 7996.00},
    {"id": 29, "name": "Christina Morales", "email": "christina.m@email.com", "age_range": "35-44", "market": "Atlanta", "source": "referral", "device_preference": "mobile", "plan_tier": "Stock Advisor", "status": "active", "start_date": "2024-07-30", "tenure_months": 20, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 597.00, "total_paid": 398.00},
    {"id": 30, "name": "Derek Singh", "email": "derek.singh@email.com", "age_range": "25-34", "market": "Portland", "source": "organic", "device_preference": "desktop", "plan_tier": "Free", "status": "active", "start_date": "2025-05-01", "tenure_months": 10, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},

    # ── Churned subscribers (7) ──────────────────────────────────────────
    {"id": 31, "name": "Michelle Brown", "email": "michelle.b@email.com", "age_range": "35-44", "market": "New York", "source": "organic", "device_preference": "desktop", "plan_tier": "Stock Advisor", "status": "churned", "start_date": "2025-03-10", "tenure_months": 8, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 199.00, "total_paid": 199.00},
    {"id": 32, "name": "Ryan Cooper", "email": "ryan.cooper@email.com", "age_range": "25-34", "market": "Chicago", "source": "promotion", "device_preference": "mobile", "plan_tier": "Epic", "status": "churned", "start_date": "2025-07-01", "tenure_months": 4, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 499.00, "total_paid": 499.00},
    {"id": 33, "name": "Stephanie Bell", "email": "steph.bell@email.com", "age_range": "45-54", "market": "Los Angeles", "source": "organic", "device_preference": "tablet", "plan_tier": "Epic Plus", "status": "churned", "start_date": "2024-03-15", "tenure_months": 12, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 166.58, "ltv": 1999.00, "total_paid": 1999.00},
    {"id": 34, "name": "Mark Taylor", "email": "mark.taylor@email.com", "age_range": "18-24", "market": "Boston", "source": "referral", "device_preference": "mobile", "plan_tier": "Free", "status": "churned", "start_date": "2025-10-01", "tenure_months": 2, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},
    {"id": 35, "name": "Jennifer Adams", "email": "jen.adams@email.com", "age_range": "35-44", "market": "Miami", "source": "organic", "device_preference": "desktop", "plan_tier": "Stock Advisor", "status": "churned", "start_date": "2025-05-20", "tenure_months": 6, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 16.58, "ltv": 199.00, "total_paid": 199.00},
    {"id": 36, "name": "Eric Hoffman", "email": "eric.hoffman@email.com", "age_range": "55-64", "market": "Washington DC", "source": "promotion", "device_preference": "desktop", "plan_tier": "Epic", "status": "churned", "start_date": "2025-09-10", "tenure_months": 3, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 499.00, "total_paid": 499.00},
    {"id": 37, "name": "Lisa Chang", "email": "lisa.chang@email.com", "age_range": "25-34", "market": "Seattle", "source": "organic", "device_preference": "mobile", "plan_tier": "Free", "status": "churned", "start_date": "2025-06-15", "tenure_months": 5, "payment_method": None, "billing_cycle": None, "monthly_rate": 0, "ltv": 0, "total_paid": 0},

    # ── Paused subscribers (5) ───────────────────────────────────────────
    {"id": 38, "name": "William Price", "email": "will.price@email.com", "age_range": "45-54", "market": "Denver", "source": "organic", "device_preference": "desktop", "plan_tier": "Epic", "status": "paused", "start_date": "2024-12-01", "tenure_months": 15, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 998.00, "total_paid": 998.00},
    {"id": 39, "name": "Nicole Rivera", "email": "nicole.r@email.com", "age_range": "25-34", "market": "New York", "source": "referral", "device_preference": "mobile", "plan_tier": "Rule Breakers", "status": "paused", "start_date": "2025-06-10", "tenure_months": 9, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 24.92, "ltv": 299.00, "total_paid": 299.00},
    {"id": 40, "name": "Jason Park", "email": "jason.park@email.com", "age_range": "35-44", "market": "San Francisco", "source": "organic", "device_preference": "mobile", "plan_tier": "Epic Plus", "status": "paused", "start_date": "2024-09-05", "tenure_months": 18, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 166.58, "ltv": 3998.00, "total_paid": 3998.00},
    {"id": 41, "name": "Kimberly Wood", "email": "kim.wood@email.com", "age_range": "55-64", "market": "Dallas", "source": "organic", "device_preference": "tablet", "plan_tier": "Rule Breakers", "status": "paused", "start_date": "2024-03-18", "tenure_months": 24, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 24.92, "ltv": 598.00, "total_paid": 598.00},
    {"id": 42, "name": "Timothy Morgan", "email": "tim.morgan@email.com", "age_range": "25-34", "market": "Philadelphia", "source": "promotion", "device_preference": "desktop", "plan_tier": "Epic", "status": "paused", "start_date": "2025-08-14", "tenure_months": 7, "payment_method": "credit_card", "billing_cycle": "annual", "monthly_rate": 41.58, "ltv": 499.00, "total_paid": 499.00},

    # ── Trial subscribers (8) ────────────────────────────────────────────
    {"id": 43, "name": "Amanda Liu", "email": "amanda.liu@email.com", "age_range": "18-24", "market": "Los Angeles", "source": "organic", "device_preference": "mobile", "plan_tier": "Rule Breakers", "status": "trial", "start_date": "2026-02-10", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 24.92, "ltv": 598.00, "total_paid": 0},
    {"id": 44, "name": "Carlos Diaz", "email": "carlos.diaz@email.com", "age_range": "25-34", "market": "New York", "source": "promotion", "device_preference": "mobile", "plan_tier": "Epic", "status": "trial", "start_date": "2026-02-15", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 41.58, "ltv": 998.00, "total_paid": 0},
    {"id": 45, "name": "Rebecca Foster", "email": "rebecca.f@email.com", "age_range": "35-44", "market": "Chicago", "source": "referral", "device_preference": "desktop", "plan_tier": "Epic Plus", "status": "trial", "start_date": "2026-02-01", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 166.58, "ltv": 3998.00, "total_paid": 0},
    {"id": 46, "name": "Sean O'Malley", "email": "sean.omalley@email.com", "age_range": "18-24", "market": "Austin", "source": "organic", "device_preference": "mobile", "plan_tier": "Epic", "status": "trial", "start_date": "2026-02-20", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 41.58, "ltv": 998.00, "total_paid": 0},
    {"id": 47, "name": "Aisha Rahman", "email": "aisha.rahman@email.com", "age_range": "25-34", "market": "Washington DC", "source": "promotion", "device_preference": "mobile", "plan_tier": "Rule Breakers", "status": "trial", "start_date": "2026-02-05", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 24.92, "ltv": 598.00, "total_paid": 0},
    {"id": 48, "name": "Tyler James", "email": "tyler.james@email.com", "age_range": "18-24", "market": "Portland", "source": "organic", "device_preference": "mobile", "plan_tier": "Epic Plus", "status": "trial", "start_date": "2026-02-18", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 166.58, "ltv": 3998.00, "total_paid": 0},
    {"id": 49, "name": "Diana Kowalski", "email": "diana.k@email.com", "age_range": "35-44", "market": "Boston", "source": "organic", "device_preference": "desktop", "plan_tier": "Epic", "status": "trial", "start_date": "2026-02-12", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 41.58, "ltv": 998.00, "total_paid": 0},
    {"id": 50, "name": "Marcus Green", "email": "marcus.green@email.com", "age_range": "25-34", "market": "Atlanta", "source": "referral", "device_preference": "mobile", "plan_tier": "Epic Plus", "status": "trial", "start_date": "2026-02-25", "tenure_months": 1, "payment_method": None, "billing_cycle": None, "monthly_rate": 166.58, "ltv": 3998.00, "total_paid": 0},
]


# ---------------------------------------------------------------------------
# BEHAVIORAL DATA (keyed by subscriber id)
# Engagement metrics, content consumption, support history
# Content sections: stocks, sectors, retirement, options, dividends, personal_finance
# ---------------------------------------------------------------------------

BEHAVIORAL_DATA = {
    # ── Active subscribers ───────────────────────────────────────────────
    1:  {"avg_sessions_per_week": 6.1, "avg_time_on_site_min": 28, "articles_read_per_week": 14, "newsletters_opened_pct": 72, "paywall_hits_per_week": 1, "engagement_score": 85, "top_sections": ["stocks", "sectors"], "articles_read_30d": 56, "videos_watched_30d": 10, "podcasts_listened_30d": 6, "tickets_90d": 0, "satisfaction_score": 4.6, "last_ticket_category": None, "segment": "Market Watchers"},
    2:  {"avg_sessions_per_week": 7.3, "avg_time_on_site_min": 35, "articles_read_per_week": 18, "newsletters_opened_pct": 88, "paywall_hits_per_week": 0, "engagement_score": 94, "top_sections": ["stocks", "options", "sectors"], "articles_read_30d": 72, "videos_watched_30d": 15, "podcasts_listened_30d": 8, "tickets_90d": 0, "satisfaction_score": 4.9, "last_ticket_category": None, "segment": "Market Watchers"},
    3:  {"avg_sessions_per_week": 2.8, "avg_time_on_site_min": 15, "articles_read_per_week": 5, "newsletters_opened_pct": 35, "paywall_hits_per_week": 3, "engagement_score": 42, "top_sections": ["retirement", "personal_finance"], "articles_read_30d": 20, "videos_watched_30d": 2, "podcasts_listened_30d": 0, "tickets_90d": 1, "satisfaction_score": 3.8, "last_ticket_category": "billing", "segment": "Casual Browsers"},
    4:  {"avg_sessions_per_week": 5.5, "avg_time_on_site_min": 25, "articles_read_per_week": 13, "newsletters_opened_pct": 65, "paywall_hits_per_week": 2, "engagement_score": 78, "top_sections": ["market_news", "stocks"], "articles_read_30d": 52, "videos_watched_30d": 12, "podcasts_listened_30d": 5, "tickets_90d": 0, "satisfaction_score": 4.3, "last_ticket_category": None, "segment": "Market Watchers"},
    5:  {"avg_sessions_per_week": 4.2, "avg_time_on_site_min": 32, "articles_read_per_week": 8, "newsletters_opened_pct": 92, "paywall_hits_per_week": 0, "engagement_score": 80, "top_sections": ["retirement", "dividends", "stocks"], "articles_read_30d": 32, "videos_watched_30d": 4, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 4.7, "last_ticket_category": None, "segment": "Buy & Hold Veterans"},
    6:  {"avg_sessions_per_week": 2.1, "avg_time_on_site_min": 12, "articles_read_per_week": 4, "newsletters_opened_pct": 28, "paywall_hits_per_week": 1, "engagement_score": 38, "top_sections": ["market_news", "retirement"], "articles_read_30d": 16, "videos_watched_30d": 3, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 3.5, "last_ticket_category": None, "segment": "Casual Browsers"},
    7:  {"avg_sessions_per_week": 3.4, "avg_time_on_site_min": 18, "articles_read_per_week": 7, "newsletters_opened_pct": 40, "paywall_hits_per_week": 6, "engagement_score": 52, "top_sections": ["personal_finance", "dividends", "market_news"], "articles_read_30d": 28, "videos_watched_30d": 8, "podcasts_listened_30d": 3, "tickets_90d": 0, "satisfaction_score": 4.0, "last_ticket_category": None, "segment": "New Investors"},
    8:  {"avg_sessions_per_week": 3.8, "avg_time_on_site_min": 20, "articles_read_per_week": 9, "newsletters_opened_pct": 55, "paywall_hits_per_week": 4, "engagement_score": 58, "top_sections": ["sectors", "stocks"], "articles_read_30d": 36, "videos_watched_30d": 5, "podcasts_listened_30d": 1, "tickets_90d": 2, "satisfaction_score": 3.6, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},
    9:  {"avg_sessions_per_week": 2.5, "avg_time_on_site_min": 14, "articles_read_per_week": 5, "newsletters_opened_pct": 30, "paywall_hits_per_week": 2, "engagement_score": 40, "top_sections": ["personal_finance", "retirement"], "articles_read_30d": 20, "videos_watched_30d": 4, "podcasts_listened_30d": 1, "tickets_90d": 0, "satisfaction_score": 3.9, "last_ticket_category": None, "segment": "Casual Browsers"},
    10: {"avg_sessions_per_week": 8.2, "avg_time_on_site_min": 40, "articles_read_per_week": 22, "newsletters_opened_pct": 85, "paywall_hits_per_week": 0, "engagement_score": 96, "top_sections": ["stocks", "sectors", "options", "market_news"], "articles_read_30d": 88, "videos_watched_30d": 18, "podcasts_listened_30d": 10, "tickets_90d": 0, "satisfaction_score": 5.0, "last_ticket_category": None, "segment": "Market Watchers"},
    11: {"avg_sessions_per_week": 5.8, "avg_time_on_site_min": 26, "articles_read_per_week": 15, "newsletters_opened_pct": 70, "paywall_hits_per_week": 1, "engagement_score": 82, "top_sections": ["stocks", "sectors", "market_news"], "articles_read_30d": 60, "videos_watched_30d": 9, "podcasts_listened_30d": 7, "tickets_90d": 0, "satisfaction_score": 4.5, "last_ticket_category": None, "segment": "Market Watchers"},
    12: {"avg_sessions_per_week": 4.0, "avg_time_on_site_min": 30, "articles_read_per_week": 7, "newsletters_opened_pct": 90, "paywall_hits_per_week": 0, "engagement_score": 76, "top_sections": ["retirement", "dividends"], "articles_read_30d": 28, "videos_watched_30d": 2, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 4.8, "last_ticket_category": None, "segment": "Buy & Hold Veterans"},
    13: {"avg_sessions_per_week": 3.0, "avg_time_on_site_min": 10, "articles_read_per_week": 6, "newsletters_opened_pct": 20, "paywall_hits_per_week": 5, "engagement_score": 45, "top_sections": ["market_news", "personal_finance", "dividends"], "articles_read_30d": 24, "videos_watched_30d": 10, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 3.7, "last_ticket_category": None, "segment": "New Investors"},
    14: {"avg_sessions_per_week": 3.5, "avg_time_on_site_min": 22, "articles_read_per_week": 8, "newsletters_opened_pct": 50, "paywall_hits_per_week": 3, "engagement_score": 55, "top_sections": ["sectors", "retirement"], "articles_read_30d": 32, "videos_watched_30d": 4, "podcasts_listened_30d": 2, "tickets_90d": 1, "satisfaction_score": 3.5, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},
    15: {"avg_sessions_per_week": 6.5, "avg_time_on_site_min": 33, "articles_read_per_week": 16, "newsletters_opened_pct": 80, "paywall_hits_per_week": 0, "engagement_score": 88, "top_sections": ["stocks", "options", "sectors"], "articles_read_30d": 64, "videos_watched_30d": 14, "podcasts_listened_30d": 8, "tickets_90d": 0, "satisfaction_score": 4.7, "last_ticket_category": None, "segment": "Market Watchers"},
    16: {"avg_sessions_per_week": 3.2, "avg_time_on_site_min": 16, "articles_read_per_week": 6, "newsletters_opened_pct": 48, "paywall_hits_per_week": 4, "engagement_score": 50, "top_sections": ["market_news", "retirement"], "articles_read_30d": 24, "videos_watched_30d": 6, "podcasts_listened_30d": 1, "tickets_90d": 1, "satisfaction_score": 3.4, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},
    17: {"avg_sessions_per_week": 5.0, "avg_time_on_site_min": 24, "articles_read_per_week": 12, "newsletters_opened_pct": 68, "paywall_hits_per_week": 1, "engagement_score": 75, "top_sections": ["stocks", "retirement", "dividends"], "articles_read_30d": 48, "videos_watched_30d": 7, "podcasts_listened_30d": 4, "tickets_90d": 0, "satisfaction_score": 4.4, "last_ticket_category": None, "segment": "Market Watchers"},
    18: {"avg_sessions_per_week": 4.5, "avg_time_on_site_min": 35, "articles_read_per_week": 9, "newsletters_opened_pct": 95, "paywall_hits_per_week": 0, "engagement_score": 83, "top_sections": ["retirement", "stocks", "sectors"], "articles_read_30d": 36, "videos_watched_30d": 5, "podcasts_listened_30d": 3, "tickets_90d": 0, "satisfaction_score": 4.9, "last_ticket_category": None, "segment": "Buy & Hold Veterans"},
    19: {"avg_sessions_per_week": 2.3, "avg_time_on_site_min": 11, "articles_read_per_week": 4, "newsletters_opened_pct": 25, "paywall_hits_per_week": 2, "engagement_score": 35, "top_sections": ["personal_finance", "market_news"], "articles_read_30d": 16, "videos_watched_30d": 5, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 3.6, "last_ticket_category": None, "segment": "Casual Browsers"},
    20: {"avg_sessions_per_week": 3.6, "avg_time_on_site_min": 15, "articles_read_per_week": 8, "newsletters_opened_pct": 35, "paywall_hits_per_week": 7, "engagement_score": 48, "top_sections": ["market_news", "personal_finance", "retirement"], "articles_read_30d": 32, "videos_watched_30d": 12, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 3.8, "last_ticket_category": None, "segment": "New Investors"},
    21: {"avg_sessions_per_week": 5.4, "avg_time_on_site_min": 27, "articles_read_per_week": 11, "newsletters_opened_pct": 74, "paywall_hits_per_week": 0, "engagement_score": 79, "top_sections": ["stocks", "options", "retirement"], "articles_read_30d": 44, "videos_watched_30d": 6, "podcasts_listened_30d": 5, "tickets_90d": 0, "satisfaction_score": 4.5, "last_ticket_category": None, "segment": "Market Watchers"},
    22: {"avg_sessions_per_week": 3.8, "avg_time_on_site_min": 28, "articles_read_per_week": 6, "newsletters_opened_pct": 88, "paywall_hits_per_week": 0, "engagement_score": 72, "top_sections": ["retirement", "dividends", "sectors"], "articles_read_30d": 24, "videos_watched_30d": 2, "podcasts_listened_30d": 1, "tickets_90d": 0, "satisfaction_score": 4.6, "last_ticket_category": None, "segment": "Buy & Hold Veterans"},
    23: {"avg_sessions_per_week": 2.0, "avg_time_on_site_min": 13, "articles_read_per_week": 4, "newsletters_opened_pct": 22, "paywall_hits_per_week": 2, "engagement_score": 36, "top_sections": ["personal_finance", "market_news"], "articles_read_30d": 16, "videos_watched_30d": 3, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 3.7, "last_ticket_category": None, "segment": "Casual Browsers"},
    24: {"avg_sessions_per_week": 5.6, "avg_time_on_site_min": 30, "articles_read_per_week": 14, "newsletters_opened_pct": 75, "paywall_hits_per_week": 0, "engagement_score": 84, "top_sections": ["stocks", "sectors", "market_news"], "articles_read_30d": 56, "videos_watched_30d": 11, "podcasts_listened_30d": 6, "tickets_90d": 0, "satisfaction_score": 4.4, "last_ticket_category": None, "segment": "Market Watchers"},
    25: {"avg_sessions_per_week": 2.4, "avg_time_on_site_min": 14, "articles_read_per_week": 5, "newsletters_opened_pct": 32, "paywall_hits_per_week": 1, "engagement_score": 41, "top_sections": ["retirement", "personal_finance"], "articles_read_30d": 20, "videos_watched_30d": 3, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 3.8, "last_ticket_category": None, "segment": "Casual Browsers"},
    26: {"avg_sessions_per_week": 3.3, "avg_time_on_site_min": 17, "articles_read_per_week": 7, "newsletters_opened_pct": 42, "paywall_hits_per_week": 5, "engagement_score": 53, "top_sections": ["market_news", "sectors", "retirement"], "articles_read_30d": 28, "videos_watched_30d": 6, "podcasts_listened_30d": 2, "tickets_90d": 1, "satisfaction_score": 3.5, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},
    27: {"avg_sessions_per_week": 4.0, "avg_time_on_site_min": 12, "articles_read_per_week": 9, "newsletters_opened_pct": 15, "paywall_hits_per_week": 8, "engagement_score": 50, "top_sections": ["personal_finance", "dividends", "market_news", "retirement"], "articles_read_30d": 36, "videos_watched_30d": 14, "podcasts_listened_30d": 4, "tickets_90d": 0, "satisfaction_score": 3.9, "last_ticket_category": None, "segment": "New Investors"},
    28: {"avg_sessions_per_week": 4.8, "avg_time_on_site_min": 34, "articles_read_per_week": 10, "newsletters_opened_pct": 82, "paywall_hits_per_week": 0, "engagement_score": 81, "top_sections": ["retirement", "stocks", "dividends"], "articles_read_30d": 40, "videos_watched_30d": 3, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 4.8, "last_ticket_category": None, "segment": "Buy & Hold Veterans"},
    29: {"avg_sessions_per_week": 2.6, "avg_time_on_site_min": 15, "articles_read_per_week": 5, "newsletters_opened_pct": 30, "paywall_hits_per_week": 1, "engagement_score": 43, "top_sections": ["personal_finance", "retirement"], "articles_read_30d": 20, "videos_watched_30d": 4, "podcasts_listened_30d": 1, "tickets_90d": 0, "satisfaction_score": 3.9, "last_ticket_category": None, "segment": "Casual Browsers"},
    30: {"avg_sessions_per_week": 3.1, "avg_time_on_site_min": 16, "articles_read_per_week": 6, "newsletters_opened_pct": 45, "paywall_hits_per_week": 6, "engagement_score": 49, "top_sections": ["market_news", "retirement", "sectors"], "articles_read_30d": 24, "videos_watched_30d": 7, "podcasts_listened_30d": 2, "tickets_90d": 1, "satisfaction_score": 3.4, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},

    # ── Churned subscribers ──────────────────────────────────────────────
    31: {"avg_sessions_per_week": 0.5, "avg_time_on_site_min": 4, "articles_read_per_week": 1, "newsletters_opened_pct": 8, "paywall_hits_per_week": 0, "engagement_score": 12, "top_sections": ["retirement"], "articles_read_30d": 4, "videos_watched_30d": 0, "podcasts_listened_30d": 0, "tickets_90d": 2, "satisfaction_score": 2.5, "last_ticket_category": "cancellation", "segment": "At-Risk Disengaged"},
    32: {"avg_sessions_per_week": 0.8, "avg_time_on_site_min": 6, "articles_read_per_week": 2, "newsletters_opened_pct": 10, "paywall_hits_per_week": 0, "engagement_score": 18, "top_sections": ["market_news"], "articles_read_30d": 8, "videos_watched_30d": 1, "podcasts_listened_30d": 0, "tickets_90d": 1, "satisfaction_score": 2.8, "last_ticket_category": "research_quality", "segment": "At-Risk Disengaged"},
    33: {"avg_sessions_per_week": 1.2, "avg_time_on_site_min": 8, "articles_read_per_week": 3, "newsletters_opened_pct": 15, "paywall_hits_per_week": 0, "engagement_score": 22, "top_sections": ["sectors", "stocks"], "articles_read_30d": 12, "videos_watched_30d": 1, "podcasts_listened_30d": 0, "tickets_90d": 3, "satisfaction_score": 2.2, "last_ticket_category": "billing", "segment": "At-Risk Disengaged"},
    34: {"avg_sessions_per_week": 0.3, "avg_time_on_site_min": 3, "articles_read_per_week": 1, "newsletters_opened_pct": 5, "paywall_hits_per_week": 0, "engagement_score": 8, "top_sections": ["market_news"], "articles_read_30d": 2, "videos_watched_30d": 1, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 3.0, "last_ticket_category": None, "segment": "At-Risk Disengaged"},
    35: {"avg_sessions_per_week": 0.6, "avg_time_on_site_min": 5, "articles_read_per_week": 1, "newsletters_opened_pct": 12, "paywall_hits_per_week": 0, "engagement_score": 15, "top_sections": ["personal_finance"], "articles_read_30d": 4, "videos_watched_30d": 0, "podcasts_listened_30d": 0, "tickets_90d": 1, "satisfaction_score": 2.6, "last_ticket_category": "cancellation", "segment": "At-Risk Disengaged"},
    36: {"avg_sessions_per_week": 1.0, "avg_time_on_site_min": 7, "articles_read_per_week": 2, "newsletters_opened_pct": 18, "paywall_hits_per_week": 0, "engagement_score": 20, "top_sections": ["stocks", "sectors"], "articles_read_30d": 8, "videos_watched_30d": 0, "podcasts_listened_30d": 0, "tickets_90d": 2, "satisfaction_score": 2.4, "last_ticket_category": "pricing", "segment": "At-Risk Disengaged"},
    37: {"avg_sessions_per_week": 0.4, "avg_time_on_site_min": 3, "articles_read_per_week": 1, "newsletters_opened_pct": 6, "paywall_hits_per_week": 0, "engagement_score": 10, "top_sections": ["personal_finance"], "articles_read_30d": 3, "videos_watched_30d": 0, "podcasts_listened_30d": 0, "tickets_90d": 0, "satisfaction_score": 2.9, "last_ticket_category": None, "segment": "At-Risk Disengaged"},

    # ── Paused subscribers ───────────────────────────────────────────────
    38: {"avg_sessions_per_week": 1.5, "avg_time_on_site_min": 10, "articles_read_per_week": 3, "newsletters_opened_pct": 25, "paywall_hits_per_week": 0, "engagement_score": 28, "top_sections": ["sectors", "stocks"], "articles_read_30d": 12, "videos_watched_30d": 1, "podcasts_listened_30d": 0, "tickets_90d": 1, "satisfaction_score": 3.2, "last_ticket_category": "billing", "segment": "At-Risk Disengaged"},
    39: {"avg_sessions_per_week": 2.0, "avg_time_on_site_min": 12, "articles_read_per_week": 4, "newsletters_opened_pct": 30, "paywall_hits_per_week": 3, "engagement_score": 35, "top_sections": ["personal_finance", "retirement"], "articles_read_30d": 16, "videos_watched_30d": 2, "podcasts_listened_30d": 0, "tickets_90d": 1, "satisfaction_score": 3.3, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},
    40: {"avg_sessions_per_week": 1.8, "avg_time_on_site_min": 15, "articles_read_per_week": 3, "newsletters_opened_pct": 35, "paywall_hits_per_week": 0, "engagement_score": 32, "top_sections": ["market_news", "sectors"], "articles_read_30d": 12, "videos_watched_30d": 2, "podcasts_listened_30d": 1, "tickets_90d": 2, "satisfaction_score": 3.0, "last_ticket_category": "research_quality", "segment": "Price-Sensitive"},
    41: {"avg_sessions_per_week": 1.2, "avg_time_on_site_min": 8, "articles_read_per_week": 2, "newsletters_opened_pct": 20, "paywall_hits_per_week": 0, "engagement_score": 25, "top_sections": ["retirement"], "articles_read_30d": 8, "videos_watched_30d": 0, "podcasts_listened_30d": 0, "tickets_90d": 1, "satisfaction_score": 3.1, "last_ticket_category": "billing", "segment": "At-Risk Disengaged"},
    42: {"avg_sessions_per_week": 2.2, "avg_time_on_site_min": 14, "articles_read_per_week": 5, "newsletters_opened_pct": 38, "paywall_hits_per_week": 4, "engagement_score": 40, "top_sections": ["market_news", "stocks"], "articles_read_30d": 20, "videos_watched_30d": 4, "podcasts_listened_30d": 1, "tickets_90d": 1, "satisfaction_score": 3.2, "last_ticket_category": "pricing", "segment": "Price-Sensitive"},

    # ── Trial subscribers ────────────────────────────────────────────────
    43: {"avg_sessions_per_week": 4.2, "avg_time_on_site_min": 18, "articles_read_per_week": 9, "newsletters_opened_pct": 50, "paywall_hits_per_week": 5, "engagement_score": 58, "top_sections": ["personal_finance", "retirement", "market_news"], "articles_read_30d": 36, "videos_watched_30d": 8, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 4.0, "last_ticket_category": None, "segment": "New Investors"},
    44: {"avg_sessions_per_week": 3.8, "avg_time_on_site_min": 20, "articles_read_per_week": 8, "newsletters_opened_pct": 45, "paywall_hits_per_week": 6, "engagement_score": 55, "top_sections": ["stocks", "market_news", "sectors"], "articles_read_30d": 32, "videos_watched_30d": 10, "podcasts_listened_30d": 3, "tickets_90d": 0, "satisfaction_score": 4.1, "last_ticket_category": None, "segment": "New Investors"},
    45: {"avg_sessions_per_week": 5.0, "avg_time_on_site_min": 25, "articles_read_per_week": 11, "newsletters_opened_pct": 60, "paywall_hits_per_week": 3, "engagement_score": 68, "top_sections": ["sectors", "stocks", "options"], "articles_read_30d": 44, "videos_watched_30d": 6, "podcasts_listened_30d": 4, "tickets_90d": 0, "satisfaction_score": 4.3, "last_ticket_category": None, "segment": "New Investors"},
    46: {"avg_sessions_per_week": 2.8, "avg_time_on_site_min": 12, "articles_read_per_week": 6, "newsletters_opened_pct": 20, "paywall_hits_per_week": 7, "engagement_score": 42, "top_sections": ["market_news", "personal_finance"], "articles_read_30d": 24, "videos_watched_30d": 12, "podcasts_listened_30d": 1, "tickets_90d": 0, "satisfaction_score": 3.6, "last_ticket_category": None, "segment": "New Investors"},
    47: {"avg_sessions_per_week": 3.5, "avg_time_on_site_min": 16, "articles_read_per_week": 7, "newsletters_opened_pct": 38, "paywall_hits_per_week": 4, "engagement_score": 48, "top_sections": ["retirement", "personal_finance", "dividends"], "articles_read_30d": 28, "videos_watched_30d": 5, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 3.8, "last_ticket_category": None, "segment": "New Investors"},
    48: {"avg_sessions_per_week": 4.5, "avg_time_on_site_min": 22, "articles_read_per_week": 10, "newsletters_opened_pct": 55, "paywall_hits_per_week": 4, "engagement_score": 62, "top_sections": ["market_news", "stocks", "retirement", "sectors"], "articles_read_30d": 40, "videos_watched_30d": 14, "podcasts_listened_30d": 5, "tickets_90d": 0, "satisfaction_score": 4.2, "last_ticket_category": None, "segment": "New Investors"},
    49: {"avg_sessions_per_week": 3.2, "avg_time_on_site_min": 19, "articles_read_per_week": 7, "newsletters_opened_pct": 42, "paywall_hits_per_week": 5, "engagement_score": 52, "top_sections": ["options", "sectors", "stocks"], "articles_read_30d": 28, "videos_watched_30d": 4, "podcasts_listened_30d": 2, "tickets_90d": 0, "satisfaction_score": 3.9, "last_ticket_category": None, "segment": "New Investors"},
    50: {"avg_sessions_per_week": 4.8, "avg_time_on_site_min": 24, "articles_read_per_week": 11, "newsletters_opened_pct": 58, "paywall_hits_per_week": 3, "engagement_score": 65, "top_sections": ["stocks", "market_news", "options", "retirement"], "articles_read_30d": 44, "videos_watched_30d": 10, "podcasts_listened_30d": 6, "tickets_90d": 0, "satisfaction_score": 4.4, "last_ticket_category": None, "segment": "New Investors"},
}


# ---------------------------------------------------------------------------
# CHURN PREDICTIONS (keyed by subscriber id)
# Precomputed risk scores, levels, and contributing factors
# ---------------------------------------------------------------------------

CHURN_PREDICTIONS = {
    # Active — low risk
    1:  {"risk_score": 0.12, "risk_level": "low", "contributing_factors": ["Strong engagement trajectory", "Consistent research consumption habit"]},
    2:  {"risk_score": 0.05, "risk_level": "low", "contributing_factors": ["Power user across all research types", "Annual billing locks in commitment"]},
    3:  {"risk_score": 0.45, "risk_level": "medium", "contributing_factors": ["Below-average session frequency", "Low newsletter engagement", "Frequent paywall hits suggest research frustration"]},
    4:  {"risk_score": 0.18, "risk_level": "low", "contributing_factors": ["High stock pick consumption", "Promotion-acquired but well retained"]},
    5:  {"risk_score": 0.08, "risk_level": "low", "contributing_factors": ["Longest active tenure", "Highest newsletter open rate", "Annual billing"]},
    6:  {"risk_score": 0.52, "risk_level": "medium", "contributing_factors": ["Declining session frequency", "Low newsletter open rate", "Weekend-only usage pattern"]},
    7:  {"risk_score": 0.35, "risk_level": "medium", "contributing_factors": ["Free tier with high paywall hits", "Short tenure", "No revenue commitment"]},
    8:  {"risk_score": 0.42, "risk_level": "medium", "contributing_factors": ["Submitted pricing complaints", "Moderate engagement for Epic tier", "Paywall frustration signals"]},
    9:  {"risk_score": 0.48, "risk_level": "medium", "contributing_factors": ["Low session frequency", "Below-average newsletter engagement", "Narrow research interest"]},
    10: {"risk_score": 0.03, "risk_level": "low", "contributing_factors": ["Highest engagement score in database", "Reads across all research areas", "Annual billing"]},
    11: {"risk_score": 0.10, "risk_level": "low", "contributing_factors": ["Strong multi-format engagement", "Growing podcast consumption"]},
    12: {"risk_score": 0.09, "risk_level": "low", "contributing_factors": ["Buy-and-hold investor with long tenure", "Highest newsletter open rate in tier"]},
    13: {"risk_score": 0.40, "risk_level": "medium", "contributing_factors": ["Free tier exploring research", "Very short tenure", "High paywall hit rate"]},
    14: {"risk_score": 0.38, "risk_level": "medium", "contributing_factors": ["Pricing complaints filed", "Moderate engagement for Epic price", "Narrow sector focus"]},
    15: {"risk_score": 0.06, "risk_level": "low", "contributing_factors": ["High engagement across formats", "Annual billing", "Referral source indicates strong intent"]},
    16: {"risk_score": 0.55, "risk_level": "high", "contributing_factors": ["Pricing concerns raised", "Below-average engagement for paid tier", "Frequent paywall encounters"]},
    17: {"risk_score": 0.15, "risk_level": "low", "contributing_factors": ["Consistent research habit", "Good newsletter engagement", "Multi-sector reader"]},
    18: {"risk_score": 0.04, "risk_level": "low", "contributing_factors": ["Longest overall tenure", "Exceptional newsletter loyalty", "Annual billing"]},
    19: {"risk_score": 0.58, "risk_level": "high", "contributing_factors": ["Very low session frequency", "Minimal newsletter engagement", "Short tenure with declining activity"]},
    20: {"risk_score": 0.32, "risk_level": "medium", "contributing_factors": ["Free tier with high paywall hits", "Video-heavy consumption may not convert", "Promotion-acquired"]},
    21: {"risk_score": 0.11, "risk_level": "low", "contributing_factors": ["Strong multi-section engagement", "Good newsletter open rate"]},
    22: {"risk_score": 0.07, "risk_level": "low", "contributing_factors": ["Extremely long tenure", "Loyal dividend-focused investor", "Annual billing"]},
    23: {"risk_score": 0.55, "risk_level": "high", "contributing_factors": ["Lowest session frequency among active paid", "Very low newsletter engagement", "Weekend-only pattern"]},
    24: {"risk_score": 0.09, "risk_level": "low", "contributing_factors": ["High engagement score", "Multi-format consumer", "Diverse research interests"]},
    25: {"risk_score": 0.50, "risk_level": "medium", "contributing_factors": ["Declining session frequency", "Low newsletter engagement", "Narrow research focus"]},
    26: {"risk_score": 0.42, "risk_level": "medium", "contributing_factors": ["Free tier hitting paywall frequently", "Pricing-sensitive profile", "Promotion-acquired"]},
    27: {"risk_score": 0.38, "risk_level": "medium", "contributing_factors": ["Shortest tenure in database", "Very low newsletter engagement", "Extremely high paywall hits"]},
    28: {"risk_score": 0.06, "risk_level": "low", "contributing_factors": ["Long tenure with steady engagement", "Strong newsletter loyalty", "Retirement planning anchor"]},
    29: {"risk_score": 0.47, "risk_level": "medium", "contributing_factors": ["Below-average engagement", "Low newsletter opens", "Weekend browsing pattern"]},
    30: {"risk_score": 0.44, "risk_level": "medium", "contributing_factors": ["Free tier with pricing concerns", "Moderate engagement", "Paywall friction"]},

    # Churned — high risk (reflects pre-churn state)
    31: {"risk_score": 0.92, "risk_level": "high", "contributing_factors": ["Sessions dropped 80% before churn", "Filed cancellation request", "Newsletter engagement near zero"]},
    32: {"risk_score": 0.88, "risk_level": "high", "contributing_factors": ["Promotion-acquired with no organic engagement", "Only 4 months tenure", "Research quality complaints"]},
    33: {"risk_score": 0.85, "risk_level": "high", "contributing_factors": ["Multiple billing disputes", "Satisfaction score lowest in database", "Engagement declined steadily over 12 months"]},
    34: {"risk_score": 0.95, "risk_level": "high", "contributing_factors": ["Near-zero engagement from start", "Never opened a newsletter", "Free tier with no research connection"]},
    35: {"risk_score": 0.90, "risk_level": "high", "contributing_factors": ["Filed cancellation request", "Single-section reader with low frequency", "No multimedia engagement"]},
    36: {"risk_score": 0.87, "risk_level": "high", "contributing_factors": ["Pricing complaints before churn", "Promotion-acquired", "Low engagement relative to Epic price"]},
    37: {"risk_score": 0.93, "risk_level": "high", "contributing_factors": ["Engagement near zero", "No research diversification", "Silent churn — no support contact"]},

    # Paused — medium-high risk
    38: {"risk_score": 0.65, "risk_level": "high", "contributing_factors": ["Billing issue triggered pause", "Engagement dropped before pause", "15-month subscriber showing fatigue"]},
    39: {"risk_score": 0.60, "risk_level": "high", "contributing_factors": ["Pricing sensitivity flagged", "Engagement below tier average", "Paywall frustration noted"]},
    40: {"risk_score": 0.68, "risk_level": "high", "contributing_factors": ["Research quality complaint filed", "Multi-month pause suggests low urgency", "Engagement dropped 50% before pause"]},
    41: {"risk_score": 0.62, "risk_level": "high", "contributing_factors": ["Long tenure but declining engagement", "Billing issue on file", "Single-section reader"]},
    42: {"risk_score": 0.58, "risk_level": "high", "contributing_factors": ["Pricing concerns raised", "Promotion-acquired", "Short tenure before pause"]},

    # Trial — variable risk
    43: {"risk_score": 0.30, "risk_level": "medium", "contributing_factors": ["Good initial engagement", "Exploring multiple research areas", "High paywall hit rate shows interest"]},
    44: {"risk_score": 0.35, "risk_level": "medium", "contributing_factors": ["Decent engagement but promotion-acquired", "Heavy video consumer", "Paywall friction moderate"]},
    45: {"risk_score": 0.20, "risk_level": "low", "contributing_factors": ["Strong initial engagement", "Sector-focused reader with high intent", "Newsletter adoption started early"]},
    46: {"risk_score": 0.50, "risk_level": "medium", "contributing_factors": ["Low newsletter engagement", "Video-heavy usage may not sustain", "High paywall hits with frustration risk"]},
    47: {"risk_score": 0.40, "risk_level": "medium", "contributing_factors": ["Moderate engagement", "Promotion-acquired trial", "Not yet committed to specific research area"]},
    48: {"risk_score": 0.22, "risk_level": "low", "contributing_factors": ["Strong multi-format engagement", "Diverse research interests", "High session frequency for trial"]},
    49: {"risk_score": 0.38, "risk_level": "medium", "contributing_factors": ["Moderate engagement", "Options-focused but narrow", "Paywall hits suggest conversion barrier"]},
    50: {"risk_score": 0.18, "risk_level": "low", "contributing_factors": ["Excellent trial engagement", "Referral-acquired with strong intent", "Multi-section reader from day one"]},
}


# ---------------------------------------------------------------------------
# AI SEGMENTS (6 behavioral clusters)
# Each segment has a radar profile across 5 behavioral axes
# ---------------------------------------------------------------------------

SEGMENT_AXES = ["Engagement", "Research Breadth", "Newsletter Loyalty", "Visit Frequency", "Portfolio Activity"]

SEGMENTS = [
    {
        "name": "Buy & Hold Veterans",
        "size": 5,
        "subscriber_ids": [5, 12, 18, 22, 28],
        "color": "#db2777",
        "description": "Long-tenured subscribers deeply committed to their investment strategy. High newsletter loyalty, check portfolios daily, and prefer in-depth stock analysis. Lowest churn risk segment.",
        "avg_engagement": 78,
        "avg_monthly_rate": 509.92,
        "avg_tenure_months": 44,
        "radar_values": [78, 42, 90, 72, 35],
    },
    {
        "name": "Casual Browsers",
        "size": 7,
        "subscriber_ids": [3, 6, 9, 19, 23, 25, 29],
        "color": "#7c3aed",
        "description": "Part-time investors who check in on weekends. Low visit frequency but moderate research breadth. Respond well to curated weekend market digests and mobile-optimized content.",
        "avg_engagement": 39,
        "avg_monthly_rate": 16.58,
        "avg_tenure_months": 18,
        "radar_values": [39, 52, 28, 24, 32],
    },
    {
        "name": "Market Watchers",
        "size": 9,
        "subscriber_ids": [1, 2, 4, 10, 11, 15, 17, 21, 24],
        "color": "#10b981",
        "description": "Power users who consume research across all asset classes and formats. Highest session frequency and pick reviews. Most likely to upgrade tiers and refer other investors.",
        "avg_engagement": 85,
        "avg_monthly_rate": 305.47,
        "avg_tenure_months": 25,
        "radar_values": [85, 82, 75, 92, 78],
    },
    {
        "name": "At-Risk Disengaged",
        "size": 9,
        "subscriber_ids": [31, 32, 33, 34, 35, 36, 37, 38, 41],
        "color": "#ef4444",
        "description": "Subscribers with sharply declining or minimal engagement. Many have already churned or paused. Immediate intervention needed — personalized win-back campaigns and simplified market updates.",
        "avg_engagement": 18,
        "avg_monthly_rate": 38.82,
        "avg_tenure_months": 8,
        "radar_values": [18, 15, 12, 16, 8],
    },
    {
        "name": "New Investors",
        "size": 12,
        "subscriber_ids": [7, 13, 20, 27, 43, 44, 45, 46, 47, 48, 49, 50],
        "color": "#f59e0b",
        "description": "Recent subscribers and trial users actively exploring investment research. High paywall hit rates signal interest. Critical window for conversion — guided onboarding and personalized research paths drive retention.",
        "avg_engagement": 54,
        "avg_monthly_rate": 56.19,
        "avg_tenure_months": 2,
        "radar_values": [54, 68, 38, 48, 55],
    },
    {
        "name": "Price-Sensitive",
        "size": 8,
        "subscriber_ids": [8, 14, 16, 26, 30, 39, 40, 42],
        "color": "#06b6d4",
        "description": "Value-conscious investors who respond to promotions and raise pricing concerns. Moderate engagement but high paywall friction. Benefit from annual plan discounts and value-focused messaging.",
        "avg_engagement": 48,
        "avg_monthly_rate": 41.60,
        "avg_tenure_months": 13,
        "radar_values": [48, 50, 45, 52, 28],
    },
]


# ---------------------------------------------------------------------------
# RECOMMENDATIONS (per segment)
# Upsell and retention actions with projected revenue impact
# ---------------------------------------------------------------------------

RECOMMENDATIONS = [
    {
        "segment": "Buy & Hold Veterans",
        "actions": [
            {"type": "upsell", "title": "Epic Plus Upgrade Bundle", "description": "Offer exclusive deep-dive sector analysis + options research as upgrade incentive for long-term holders", "projected_monthly_impact": 850, "confidence": 0.82, "priority": "medium"},
            {"type": "retention", "title": "Veterans Research Club", "description": "Early access to new stock picks, quarterly portfolio review webinars, priority analyst Q&A sessions", "projected_monthly_impact": 320, "confidence": 0.90, "priority": "low"},
        ],
    },
    {
        "segment": "Casual Browsers",
        "actions": [
            {"type": "retention", "title": "Weekend Market Digest", "description": "Personalized Saturday morning email with top stock picks and market movers matched to portfolio interests", "projected_monthly_impact": 280, "confidence": 0.75, "priority": "high"},
            {"type": "upsell", "title": "Epic Trial Conversion", "description": "7-day Epic trial with full research access and personalized stock recommendations", "projected_monthly_impact": 450, "confidence": 0.60, "priority": "medium"},
        ],
    },
    {
        "segment": "Market Watchers",
        "actions": [
            {"type": "upsell", "title": "Epic Plus Annual Lock-In", "description": "20% annual discount for Epic Plus with exclusive deep-dive sector analysis and options strategies", "projected_monthly_impact": 1280, "confidence": 0.85, "priority": "high"},
            {"type": "retention", "title": "Power Investor Perks", "description": "Ad-free experience, real-time stock alerts, early access to new picks, priority analyst chat", "projected_monthly_impact": 400, "confidence": 0.88, "priority": "low"},
        ],
    },
    {
        "segment": "At-Risk Disengaged",
        "actions": [
            {"type": "retention", "title": "Win-Back Re-engagement Campaign", "description": "3-email sequence with personalized stock pick highlights and 50% off renewal for first year", "projected_monthly_impact": 520, "confidence": 0.45, "priority": "critical"},
            {"type": "retention", "title": "Simplified Daily Market Brief", "description": "One-click daily email with top 5 stock moves and portfolio impact — no login required", "projected_monthly_impact": 180, "confidence": 0.55, "priority": "high"},
        ],
    },
    {
        "segment": "New Investors",
        "actions": [
            {"type": "retention", "title": "Guided Investing Journey", "description": "7-day personalized research path based on initial investment interests and risk profile", "projected_monthly_impact": 920, "confidence": 0.72, "priority": "critical"},
            {"type": "upsell", "title": "Trial-to-Paid Conversion Offer", "description": "Lock in introductory rate for first year with access to Stock Advisor + Rule Breakers picks", "projected_monthly_impact": 1380, "confidence": 0.65, "priority": "high"},
        ],
    },
    {
        "segment": "Price-Sensitive",
        "actions": [
            {"type": "retention", "title": "Annual Plan Value Switch", "description": "Highlight per-month savings of annual billing with side-by-side comparison across all tiers", "projected_monthly_impact": 480, "confidence": 0.70, "priority": "high"},
            {"type": "upsell", "title": "Flexible Tier Adjustment", "description": "Offer Stock Advisor at discounted rate vs churn, preserving subscriber relationship and upsell path", "projected_monthly_impact": 340, "confidence": 0.78, "priority": "medium"},
        ],
    },
]


# ---------------------------------------------------------------------------
# REVENUE FORECAST
# 15 months historical (Jan 2025 – Mar 2026) + 12 months projected
# ---------------------------------------------------------------------------

REVENUE_FORECAST = {
    "historical": [
        {"month": "2025-01", "mrr": 3480, "subscribers": 38},
        {"month": "2025-02", "mrr": 3620, "subscribers": 39},
        {"month": "2025-03", "mrr": 3750, "subscribers": 40},
        {"month": "2025-04", "mrr": 3890, "subscribers": 41},
        {"month": "2025-05", "mrr": 3980, "subscribers": 42},
        {"month": "2025-06", "mrr": 4120, "subscribers": 43},
        {"month": "2025-07", "mrr": 4280, "subscribers": 44},
        {"month": "2025-08", "mrr": 4400, "subscribers": 44},
        {"month": "2025-09", "mrr": 4530, "subscribers": 45},
        {"month": "2025-10", "mrr": 4680, "subscribers": 46},
        {"month": "2025-11", "mrr": 4840, "subscribers": 47},
        {"month": "2025-12", "mrr": 4980, "subscribers": 47},
        {"month": "2026-01", "mrr": 5120, "subscribers": 48},
        {"month": "2026-02", "mrr": 5310, "subscribers": 49},
        {"month": "2026-03", "mrr": 5515, "subscribers": 50},
    ],
    "projected_baseline": [
        {"month": "2026-04", "mrr": 5625},
        {"month": "2026-05", "mrr": 5738},
        {"month": "2026-06", "mrr": 5853},
        {"month": "2026-07", "mrr": 5970},
        {"month": "2026-08", "mrr": 6089},
        {"month": "2026-09", "mrr": 6211},
        {"month": "2026-10", "mrr": 6335},
        {"month": "2026-11", "mrr": 6462},
        {"month": "2026-12", "mrr": 6591},
        {"month": "2027-01", "mrr": 6723},
        {"month": "2027-02", "mrr": 6857},
        {"month": "2027-03", "mrr": 6994},
    ],
    "projected_ai_enhanced": [
        {"month": "2026-04", "mrr": 5791},
        {"month": "2026-05", "mrr": 6081},
        {"month": "2026-06", "mrr": 6385},
        {"month": "2026-07", "mrr": 6704},
        {"month": "2026-08", "mrr": 7039},
        {"month": "2026-09", "mrr": 7391},
        {"month": "2026-10", "mrr": 7761},
        {"month": "2026-11", "mrr": 8149},
        {"month": "2026-12", "mrr": 8556},
        {"month": "2027-01", "mrr": 8984},
        {"month": "2027-02", "mrr": 9433},
        {"month": "2027-03", "mrr": 9905},
    ],
}


# ---------------------------------------------------------------------------
# RETENTION ACTIONS (AI agent log — 15 recent automated actions)
# ---------------------------------------------------------------------------

RETENTION_ACTIONS = [
    {"id": 1, "timestamp": "2026-03-04T09:15:00Z", "action_type": "email_campaign", "subscriber_id": 19, "subscriber_name": "Megan Davis", "description": "Sent personalized re-engagement email with top 5 stock picks matching her personal finance interests", "status": "completed", "outcome": "Subscriber opened email and reviewed 3 stock analyses within 24 hours"},
    {"id": 2, "timestamp": "2026-03-04T08:30:00Z", "action_type": "discount_offer", "subscriber_id": 16, "subscriber_name": "Kevin Murphy", "description": "Triggered 30% annual plan discount offer after 2nd pricing inquiry on Stock Advisor renewal", "status": "completed", "outcome": "Subscriber clicked offer link — conversion pending"},
    {"id": 3, "timestamp": "2026-03-03T16:45:00Z", "action_type": "paywall_unlock", "subscriber_id": 27, "subscriber_name": "Victoria Nguyen", "description": "Unlocked 3 premium stock analyses to reduce paywall friction during exploration phase", "status": "completed", "outcome": "Subscriber read all 3 analyses and added 2 stocks to watchlist"},
    {"id": 4, "timestamp": "2026-03-03T14:20:00Z", "action_type": "csm_trigger", "subscriber_id": 33, "subscriber_name": "Stephanie Bell", "description": "Escalated to Customer Success: high-value churned Epic Plus subscriber with billing disputes", "status": "in_progress", "outcome": None},
    {"id": 5, "timestamp": "2026-03-03T11:00:00Z", "action_type": "content_recommendation", "subscriber_id": 43, "subscriber_name": "Amanda Liu", "description": "Pushed personalized trial onboarding sequence: retirement planning + growth stock research path", "status": "completed", "outcome": "Subscriber completed 4 of 7 onboarding steps in first session"},
    {"id": 6, "timestamp": "2026-03-03T09:30:00Z", "action_type": "email_campaign", "subscriber_id": 23, "subscriber_name": "Hannah Lewis", "description": "Sent curated weekend market digest preview to re-engage weekend browsing pattern", "status": "completed", "outcome": "Email opened, subscriber reviewed Stock Advisor picks on Saturday"},
    {"id": 7, "timestamp": "2026-03-02T15:10:00Z", "action_type": "win_back_offer", "subscriber_id": 31, "subscriber_name": "Michelle Brown", "description": "Initiated 3-email win-back sequence with 50% off Stock Advisor renewal for first year", "status": "in_progress", "outcome": None},
    {"id": 8, "timestamp": "2026-03-02T13:45:00Z", "action_type": "paywall_unlock", "subscriber_id": 44, "subscriber_name": "Carlos Diaz", "description": "Unlocked premium sector analysis for trial user showing high interest in growth stocks", "status": "completed", "outcome": "Subscriber read 5 premium stock analyses in the session"},
    {"id": 9, "timestamp": "2026-03-02T10:20:00Z", "action_type": "discount_offer", "subscriber_id": 42, "subscriber_name": "Timothy Morgan", "description": "Offered pause-to-annual conversion: resume Epic at 25% off annual rate", "status": "pending", "outcome": None},
    {"id": 10, "timestamp": "2026-03-01T16:30:00Z", "action_type": "email_campaign", "subscriber_id": 6, "subscriber_name": "Robert Johnson", "description": "Sent weekday engagement nudge with breaking market alert and trending stock picks", "status": "completed", "outcome": "Subscriber visited site on Tuesday for first time in 3 weeks"},
    {"id": 11, "timestamp": "2026-03-01T14:00:00Z", "action_type": "content_recommendation", "subscriber_id": 48, "subscriber_name": "Tyler James", "description": "Surfaced Motley Fool Money podcast episodes based on market news + stocks reading pattern", "status": "completed", "outcome": "Subscriber listened to 2 podcast episodes"},
    {"id": 12, "timestamp": "2026-03-01T11:15:00Z", "action_type": "csm_trigger", "subscriber_id": 40, "subscriber_name": "Jason Park", "description": "Flagged paused Epic Plus subscriber for personal outreach — research quality concern", "status": "pending", "outcome": None},
    {"id": 13, "timestamp": "2026-02-28T15:45:00Z", "action_type": "win_back_offer", "subscriber_id": 35, "subscriber_name": "Jennifer Adams", "description": "Sent simplified daily market brief email — no login required — to re-establish research habit", "status": "completed", "outcome": "Subscriber opened 4 of 5 daily briefs sent so far"},
    {"id": 14, "timestamp": "2026-02-28T09:00:00Z", "action_type": "paywall_unlock", "subscriber_id": 7, "subscriber_name": "Emily Nakamura", "description": "Strategic paywall unlock of 5 premium stock picks across different sectors for free member", "status": "completed", "outcome": "Subscriber explored options and sector analysis for first time"},
    {"id": 15, "timestamp": "2026-02-27T13:30:00Z", "action_type": "discount_offer", "subscriber_id": 8, "subscriber_name": "James O'Brien", "description": "Preemptive annual plan discount after 2nd support ticket about Epic pricing", "status": "completed", "outcome": "Subscriber renewed at annual rate — retained at lower effective cost"},
]
