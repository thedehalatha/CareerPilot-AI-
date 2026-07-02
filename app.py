import streamlit as st
import asyncio
import os

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

from agents.root_agent import root_agent

# Debug (Remove later)
print("API KEY:", os.getenv("GOOGLE_API_KEY"))


st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.markdown("### Your AI-powered Career Guidance Assistant")


st.sidebar.title("🚀 CareerPilot AI")

st.sidebar.markdown("### Features")

st.sidebar.markdown("""
- 🎯 Career Guidance
- 🛣️ Learning Roadmap
- 💬 Interview Preparation
- 📄 Resume Analysis
- 📊 Skill Gap Analysis
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Upload your resume or ask career-related questions."
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])



async def ask_agent(question):

    session_service = InMemorySessionService()

    runner = Runner(
        agent=root_agent,
        app_name="CareerPilot",
        session_service=session_service
    )

    session = await session_service.create_session(
        app_name="CareerPilot",
        user_id="student"
    )

    message = types.Content(
        role="user",
        parts=[
            types.Part(text=question)
        ]
    )

    answer = ""

    async for response in runner.run_async(
        user_id="student",
        session_id=session.id,
        new_message=message
    ):

        if response.content and response.content.parts:
            text = response.content.parts[0].text

            if text:
                answer += text

    return answer



st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF or TXT resume",
    type=["pdf", "txt"]
)

if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    if uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")

    else:
        import PyPDF2

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        resume_text = ""

        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    st.subheader("📄 Resume Preview")
    st.write(resume_text[:500])

    if resume_text:

        with st.spinner("Analyzing your resume..."):

            result = asyncio.run(
                ask_agent(
                    f"Analyze this resume and give feedback:\n\n{resume_text}"
                )
            )

        st.subheader("🤖 Resume Analysis")
        st.write(result)


user_input = st.chat_input(
    "Ask about careers, resumes, interviews, or roadmaps..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):

        result = asyncio.run(
            ask_agent(user_input)
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result
        }
    )

    with st.chat_message("assistant"):
        st.write(result)