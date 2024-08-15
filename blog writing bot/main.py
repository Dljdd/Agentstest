import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# from tools import query_tool, seo_tool

from agents import research_specialist, content_writer, content_editor, seo_strategist
load_dotenv()



topic = "How Sarvam AI is tackling Speech to text and text to speech for indic languages their website for reference: https://www.sarvam.ai/"


task1 = Task(
    description=f"""Conduct comprehensive research on the assigned blog topic: {topic}, gathering accurate and relevant information from reliable sources across the internet, including articles, studies, and expert opinions.""",
    expected_output="A detailed research brief summarizing key findings and relevant data points containing facts and figures which can be utilised.",
    agent=research_specialist,
)

task2 = Task(
    description="""Perform keyword research based on the topic and research brief, identifying primary and secondary keywords along with SEO guidelines that should be integrated into the blog post.""",
    expected_output="A list of targeted keywords and a set of SEO recommendations tailored to the blog post.",
    agent=seo_strategist,
)

task3 = Task(
    description="""Using the research brief and SEO guidelines, write a clear, engaging, and well-structured blog post on the topic: {topic}, ensuring the content is informative, accessible, and optimized for the target audience.""",
    expected_output="A complete draft of the blog post that is both engaging and SEO-friendly.",
    agent=content_writer,
)

task4 = Task(
    description="""Review the drafted blog post for grammar, punctuation, coherence, and style. Ensure that the content aligns with the blog’s overall voice and tone, making any necessary edits.""",
    expected_output="A polished and edited version of the blog post, ready for final optimization and publication.",
    agent=content_editor,
)

task5 = Task(
    description="""Optimize the finalized blog post for search engines by adjusting on-page SEO elements, including meta tags, headers, and keyword placement, ensuring the content is fully optimized for search visibility.""",
    expected_output="An SEO-optimized version of the blog post with all necessary on-page adjustments.",
    agent=seo_strategist,
)

# task6 = Task(
#     description=f"""Schedule the optimized and edited blog post for publication. Format it for readability, ensuring proper layout, image placement, and adherence to the content calendar.""",
#     expected_output="The blog post is published and formatted correctly on the blog platform, ready for reader engagement.",
#     agent=Publication_Manager,
# )

# task7 = Task(
#     description=f"""Monitor the performance of the published blog post by analyzing traffic, engagement, and conversion rates. Compile insights and recommendations to inform future blog strategies and content creation.""",
#     expected_output="A detailed report on the blog post’s performance, including actionable insights for improving future content.",
#     agent=Analytics_Feedback_Specialist,
# )

crew = Crew(
    agents=[research_specialist, seo_strategist,content_writer,content_editor, seo_strategist],
    tasks=[task1, task2, task3, task4, task5],
    verbose=2,  # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)