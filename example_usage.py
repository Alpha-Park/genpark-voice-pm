# -*- coding: utf-8 -*-
from client import GenParkVoicePm

pm = GenParkVoicePm()

# 1. Fibonacci Story Point Estimation
story = {
    "backend_complexity": 4.0,
    "frontend_complexity": 3.0,
    "integration_dependencies_count": 2.0,
    "novelty_uncertainty_score": 3.0
}
est = pm.estimate_story_points_fibonacci(story)
print(f"Fibonacci Estimation: {est['estimated_story_points']} Story Points ({est['complexity_risk_category']}, Raw Effort: {est['raw_effort_score']})")

# 2. PRD Decomposition
prd = """
The system must support real-time cryptographic receipt issuance for high-value transactions.
The user interface should display instant verification badges upon webhook confirmation.
The platform must enable multi-tenant team access controls.
"""
decomp = pm.decompose_prd_to_invest_stories(prd)
print()
print(f"PRD Decomposition: {decomp['total_stories_synthesized']} User Stories Synthesized")
for s in decomp['user_stories']:
    print(f"  [{s['story_id']}] {s['narrative']}")

# 3. 0/1 Knapsack Sprint Backlog Scheduling
backlog = [
    {"id": "US-001", "name": "Payment Delegation", "story_points": 8, "business_value": 90},
    {"id": "US-002", "name": "Audit Trail Export", "story_points": 5, "business_value": 45},
    {"id": "US-003", "name": "Webhooks Gateway", "story_points": 13, "business_value": 110},
    {"id": "US-004", "name": "Theme Toggle", "story_points": 2, "business_value": 20},
    {"id": "US-005", "name": "SSO Auth", "story_points": 8, "business_value": 85}
]
sprint = pm.schedule_sprint_backlog_knapsack(backlog, velocity_capacity=25)
print()
print(f"Sprint Knapsack: Allocated {sprint['allocated_story_points']}/{sprint['sprint_velocity_capacity']} pts ({sprint['capacity_utilization_pct']}%)")
print(f"  Maximized Business Value: {sprint['maximized_business_value']} points")
for s in sprint['allocated_stories']:
    print(f"  + {s['id']}: {s['name']} ({s['story_points']} pts, Val={s['business_value']})")
