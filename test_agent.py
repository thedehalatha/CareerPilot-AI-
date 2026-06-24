import asyncio
from dotenv import load_dotenv
load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.root_agent import root_agent


async def main():

    session_service = InMemorySessionService()

    runner = Runner(
        agent=root_agent,
        app_name="CareerPilot",
        session_service=session_service
    )

    user_id = "student1"

    session = await session_service.create_session(
        app_name="CareerPilot",
        user_id=user_id
    )

    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text="I want to become an AI Engineer. What should I learn?"
            )
        ]
    )

    async for response in runner.run_async(
        user_id=user_id,
        session_id=session.id,
        new_message=message
    ):
        if response.content:
            print(response.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())