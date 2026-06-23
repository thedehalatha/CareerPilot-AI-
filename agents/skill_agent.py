from google.adk.agents import Agent


skill_agent = Agent(
    name="SkillAnalyzer",
    model="gemini-2.0-flash",
    description="Analyzes student skills and gaps",

    instruction="""

You are SkillAnalyzer AI.

Your job:

1. Ask user about current skills
2. Compare skills with target career
3. Identify missing skills
4. Suggest what to learn next

Give simple practical advice.

"""
)