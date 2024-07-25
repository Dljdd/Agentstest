from crewai import Crew,Process
from agents import researcher,writer
from tasks import task1,task2
from crewai_tools import SerperDevTool
from tools import search_tool
import os

os.environ["SERPER_API_KEY"] =""
crew = Crew(
    agents = [researcher, writer],
    tasks = [task1, task2],
    verbose = 2, # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("##############")
print(result)