from dotenv import load_dotenv
import os
from llama_index.llms.groq import Groq
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process

load_dotenv()
# Define your API key here
groq_api_key = os.getenv('GROQ_API_KEY')

chat_llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=groq_api_key,
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=1000,
)

llm = Groq(model="llama-3.1-70b-versatile", api_key=groq_api_key)

