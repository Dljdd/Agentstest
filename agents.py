from crewai import Agent
import os
from tools import search_tool
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = ""

researcher = Agent(
    role = "Senior Research Assistant",
    goal = "Look up the latest Advancements in AI Agents",
    backstory = """You work at a leading tech think tank.
    Your expertise lies in searching Google for AI Agent frameworks.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ChatGroq(temperature=0.2, model_name="llama3-8b-8192")
)


writer = Agent(
  role='Professional Short-Article Writer',
  goal='summarize the latest advancement in AI agents in a concise article',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True,
  llm=ChatGroq(temperature=0.2, model_name="llama3-8b-8192")
)