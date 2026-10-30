# -*- coding: utf-8 -*-
"""
GenPark Voice PM MCP Server
FastMCP standard interface for Fibonacci story point estimation and sprint knapsack backlog scheduling.
"""

import json
from typing import Dict, Any, List
from client import GenParkVoicePm

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("genpark-voice-pm")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("genpark-voice-pm")

pm = GenParkVoicePm()

@mcp.tool()
def estimate_story_points_fibonacci(
    story_parameters: Dict[str, Any]
) -> str:
    """
    Estimates agile story points mapped to nearest Fibonacci number.
    """
    res = pm.estimate_story_points_fibonacci(story_parameters)
    return json.dumps(res, indent=2)

@mcp.tool()
def decompose_prd_to_invest_stories(
    prd_text: str
) -> str:
    """
    Parses PRD requirements text and synthesizes INVEST-compliant user stories.
    """
    res = pm.decompose_prd_to_invest_stories(prd_text)
    return json.dumps(res, indent=2)

@mcp.tool()
def schedule_sprint_backlog_knapsack(
    stories: List[Dict[str, Any]],
    velocity_capacity: int = 30
) -> str:
    """
    Solves 0/1 Knapsack dynamic programming to maximize total business value within sprint capacity.
    """
    res = pm.schedule_sprint_backlog_knapsack(stories, velocity_capacity)
    return json.dumps(res, indent=2)

def main():
    print("Testing Voice PM:")
    print(estimate_story_points_fibonacci({"backend_complexity": 3, "frontend_complexity": 2}))

if __name__ == "__main__":
    main()
