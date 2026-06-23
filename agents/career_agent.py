from google.adk.agents import Agent


career_agent = Agent(
    name="CareerPilot",
    model="gemini-2.5-flash",
    description="AI career assistant",
    instruction="""

You are CareerPilot AI.

Your job is to help students with:

1. Career guidance
2. Skill gap analysis
3. Learning roadmap
4. Interview preparation

Give clear and practical answers.

"""
)