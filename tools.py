from crewai_tools import SerperDevTool
import os

os.environ["SERPER_API_KEY"] =""

search_tool = SerperDevTool()