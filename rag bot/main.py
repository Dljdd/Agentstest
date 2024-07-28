import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

from tools import query_tool

from agents import chat_llm
load_dotenv()




researcher = Agent(
    role="Expert Researcher",
    goal="Uncover insights about the research paper",
    backstory="""You work in Academia as a Lead Psychologist
  Your goal is to understand papers in the field of psychology""",
    verbose=True,
    allow_delegation=False,
    tools=[query_tool],
    llm=chat_llm,
)
writer = Agent(
    role="Expert Psychology Writer",
    goal="Explain the experiment conducted in the article, focusing on the procedure and results obtained",
    backstory="""You are a renowned Psychology Research Writer, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
    llm=chat_llm,
    verbose=True,
    allow_delegation=False,
)

task1 = Task(
    description="""Conduct a comprehensive analysis of the given research paper keeping in mind all the important points""",
    expected_output="Complete analysis with all key points in bullet points",
    agent=researcher,
)

task2 = Task(
    description="""Using the insights provided, Explain the experiment conducted in the article, focusing on the procedure and results obtained
  Your post should be informative yet accessible and not missing any important detail""",
    expected_output="Full analysis with explaining the experiment conducted in the article, focusing on the procedure and results obtained",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,  # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)