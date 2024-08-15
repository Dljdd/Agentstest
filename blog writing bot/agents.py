from dotenv import load_dotenv
import os
from llama_index.llms.groq import Groq
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from crewai import Agent, Task, Crew, Process
from tools import query_tool, seo_tool

load_dotenv()
# Define your API key here
groq_api_key = os.getenv('GROQ_API_KEY')

chat_llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=groq_api_key,
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=3500,
)

llm = Groq(model="llama-3.1-70b-versatile", api_key=groq_api_key)

# Agents
research_specialist = Agent(
    role="Research Specialist",
    goal="To gather accurate and comprehensive information from reliable sources across the internet to support the blog's content.",
    backstory="""The Research Specialist was developed as a data-driven analyst, fine-tuned to identify trustworthy and relevant sources of information. It has years of experience in academic research and journalism, making it a meticulous and thorough researcher.""",
    verbose=True,
    allow_delegation=False,
    tools=[query_tool],
    llm=chat_llm,
)

content_writer = Agent(
    role="Content Writer",
    goal="To craft engaging, informative, and well-structured blog posts based on the research provided.",
    backstory="""Content Writer has a background in creative writing and journalism, having crafted numerous articles, essays, and stories. It’s known for its ability to adapt its tone and style to different audiences, ensuring that the content is both engaging and informative.""",
    llm=chat_llm,
    verbose=True,
    allow_delegation=False,
)

content_editor = Agent(
    role="Content Editor",
    goal="To ensure that all blog posts are grammatically correct, coherent, and aligned with the blog's overall voice and tone.",
    backstory="""The Content Editor has a background in editorial work, having spent years refining and perfecting various types of written content. It has a sharp eye for detail and a deep understanding of language, tone, and audience engagement.""",
    llm=chat_llm,
    verbose=True,
    allow_delegation=False,
)


seo_strategist = Agent(
    role="SEO Strategist",
    goal="To optimize blog posts for search engines to ensure high visibility and ranking in search results.",
    backstory="""SEO Strategist was designed as a specialist in digital marketing and search engine optimization. With a background in data analytics and online marketing, it excels at making content discoverable.""",
    llm=chat_llm,
    verbose=True,
    # tools = [seo_tool],
    allow_delegation=False,
)

