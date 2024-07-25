# import pandas as pd
import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
# from crewai_tools import YoutubeChannelSearchTool
import warnings
warnings.filterwarnings('ignore')


os.environ["GROQ_API_KEY"] = ""

# youtube_video_search_tool = YoutubeChannelSearchTool(youtube_channel_handle='@atrioc')

topic = 'ML vs DL vs Data Science'

Summarizer_Agent = Agent(
        role='Summarizer_Agent',
        goal=f"""Write an article about the given topic{topic} based on the facts provided to you""",
        
        verbose=True,
        allow_delegation=False,
        memory=True,
        max_iter=3,
        max_rpm=100,
        backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
        # tools=[youtube_video_search_tool],
        llm=ChatGroq(temperature=0.2, model_name="llama3-8b-8192")
    )

task_summarize_vid = Task(
        description=f"""Write an article on the provided topic {topic} make sure it is at least 400 words and is understandable and makes sense
            """,
        # tools=[youtube_video_search_tool],
        agent=Summarizer_Agent,
        output_file='new-blog-post.md'
        )



crew = Crew(
    agents=[Summarizer_Agent],
    tasks=[task_summarize_vid],

)


result = crew.kickoff()

print(result)