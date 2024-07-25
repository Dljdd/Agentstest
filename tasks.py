from crewai import Task
from agents import researcher, writer


task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI Agents in March of 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
  expected_output="Full analysis report in bullet points",
  agent=researcher
)



task2 = Task(
  description="""Using the insights provided, write a short article
  that highlights the most significant AI Agent advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="Full blog post of at least 3 paragraphs",
  agent=writer
)