from crewai import Task
from agents import researcher, writer
from agents import topic

task1 = Task(
  description=f"""Conduct a comprehensive analysis of the latest advancements in {topic} 2020 onwards.
  Identify key trends, breakthrough studies, and potential industry impacts.""",
  expected_output="Full analysis report in bullet points with the respective paper",
  agent=researcher
)



task2 = Task(
  description=f"""Using the insights provided, write a short article
  that highlights the most significant {topic} advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="Detailed analysis on which paper contains relevant information about the topic along with a link to the paper at least 800 words",
  agent=writer
)