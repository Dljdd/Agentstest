from crewai import Agent
import os
from tools import search_tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
topic = "retroactive interference "
researcher = Agent(
    role = "Senior Research Assistant",
    goal = f"Look up the latest Advancements in {topic}",
    backstory = """You work at a leading tech think tank.
    Your expertise lies in searching Google for Psychology related research papers.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ChatGroq(temperature=0.2, model_name="llama3-8b-8192")
)


writer = Agent(
  role='Professional Short-Article Writer',
  goal=f'summarize the latest advancement in {topic} in a concise article',
  backstory="""You are a renowned Content Strategist, known for your insightful and informative analysis skilss.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True,
  llm=ChatGroq(temperature=0.2, model_name="llama3-8b-8192")
)