# 🚀 CareerPilot AI

CareerPilot AI is an AI-powered career guidance assistant built using **Google ADK**, **Gemini 2.5 Flash**, and **Streamlit**. It helps students explore career paths, generate learning roadmaps, prepare for interviews, analyze resumes, and identify skill gaps.

## ✨ Features

* 🎯 Career Guidance
* 🛣️ Personalized Learning Roadmaps
* 💬 Interview Preparation
* 📄 AI Resume Analysis
* 📊 Skill Gap Analysis
* 💻 Interactive Streamlit Web Interface

## 🛠️ Tech Stack

* Python
* Google ADK
* Gemini 2.5 Flash
* Streamlit
* PyPDF2
* python-dotenv

## 📂 Project Structure

```
CareerPilot-AI/
│
├── agents/
│   ├── career_agent.py
│   ├── roadmap_agent.py
│   ├── interview_agent.py
│   ├── resume_agent.py
│   ├── skill_gap_agent.py
│   └── root_agent.py
│
├── app.py
├── test_agent.py
├── requirements.txt
├── .env
└── README.md
```

## 🚀 Installation

1. Clone the repository.

```bash
git clone https://github.com/thedehalatha/CareerPilot-AI.git
```

2. Create a virtual environment.

```bash
python -m venv venv
```

3. Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Add your Gemini API key to a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

6. Run the application.

```bash
streamlit run app.py
```

## 📸 Screenshots

Add screenshots of the Streamlit application here.

## 📈 Future Improvements

* User authentication
* Resume score visualization
* Job recommendations
* Cloud deployment
* Database integration

## 👩‍💻 Author

Developed by Dehalatha.
