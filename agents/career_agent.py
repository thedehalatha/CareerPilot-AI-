from google.adk.agents import Agent

from agents.skill_agent import skill_agent
from agents.roadmap_agent import roadmap_agent


career_agent = Agent(
    name="CareerPilot",

    model="gemini-2.5-flash",

    description="Main AI career assistant",

    instruction="""

You are CareerPilot AI.

You help students with:

1. Career guidance
2. Skill gap analysis
3. Learning roadmaps
4. Interview preparation

Use your specialist agents when needed.

""",

    
)