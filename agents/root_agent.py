from google.adk.agents import Agent

from agents.career_agent import career_agent
from agents.roadmap_agent import roadmap_agent
from agents.interview_agent import interview_agent


root_agent = Agent(

    name="CareerPilotRoot",

    model="gemini-2.5-flash",

    description="Main CareerPilot assistant",

    instruction="""

You are the main CareerPilot AI.

Choose the right agent:

Career agent:
- career advice
- skills
- job roles

Roadmap agent:
- learning path
- study plan
- technologies

""",

    sub_agents=[
    career_agent,
    roadmap_agent,
    interview_agent
]
)