import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

from tools import query_tool

from agents import chat_llm
load_dotenv()



topic = "Analysis of Speech to Text"

researcher = Agent(
    role="Expert Researcher",
    goal=f"Find relevant and latest research related to the {topic}",
    backstory="""You work in Academia as a Lead Machine Learning & AI Scientist
  Your goal is to understand papers in the field of Artificial Intelligence and Machinelearning""",
    verbose=True,
    allow_delegation=False,
    tools=[query_tool],
    llm=chat_llm,
)
writer = Agent(
    role="Expert Machine Learning and AI  Writer",
    goal=f"Explain the paper given and how exactly it is related to the {topic} at hand and give places where we can add it within our paper",
    backstory="""You are a renowned Machine Learning & AI Writer, known for your insightful and engaging research papers.
  You transform complex concepts into compelling narratives.""",
    llm=chat_llm,
    verbose=True,
    allow_delegation=False,
)

task1 = Task(
    description=f"""Find 10 to 20 relevant research papers related to the topic: {topic} and get the important information related to them Papers from the year 2023 till 2024""",
    expected_output="Complete analysis with all key points in bullet points",
    agent=researcher,
)

task2 = Task(
    description="""Using the insights provided, Explain How relevant to the topic are the research papers and how can they be used 
  Your post should be informative yet accessible and not missing any important detail""",
    expected_output="Full analysis with explaining where in our research paper do the other papers fit in",
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