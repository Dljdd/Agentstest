import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# from tools import query_tool
from tools import PDFParsingTool, TextStructuringTool, ContentSelectionTool, ConceptExtractionTool, QuestionCreationTool, AnswerExtractionTool

# from tools.pdf_parsing_tool import PDFParsingTool
# from tools.text_structuring_tool import TextStructuringTool
# from tools.content_selection_tool import ContentSelectionTool
# from tools.concept_extraction_tool import ConceptExtractionTool
# from tools.question_creation_tool import QuestionCreationTool
# from tools.answer_extraction_tool import AnswerExtractionTool

# Import the chat LLM and other dependencies
from agents import chat_llm

load_dotenv()

# Initialize the tools
pdf_parsing_tool = PDFParsingTool(file_path="flashcard/data/probability and statistics - T.Veerarajan.pdf")
text_structuring_tool = TextStructuringTool()
# Assuming structured_content will be generated after text structuring
structured_content = {}  # This will be filled after task 1
content_selection_tool = ContentSelectionTool(structured_content=structured_content)
concept_extraction_tool = ConceptExtractionTool(embed_model=your_embed_model)
question_creation_tool = QuestionCreationTool(llm=chat_llm)
answer_extraction_tool = AnswerExtractionTool(query_engine=your_query_engine)

Textbook_Parser = Agent(
    role="Textbook Parser",
    goal="Parse the textbook and structure its contents for further processing.",
    backstory="You are a highly experienced data extraction specialist...",
    verbose=True,
    allow_delegation=False,
    tools=[pdf_parsing_tool],
    llm=chat_llm,
)

Chapter_Selector = Agent(
    role="Chapter Selector",
    goal="Identify and select the specific chapter(s) requested by the user...",
    backstory="You are an expert content navigator...",
    verbose=True,
    allow_delegation=False,
    tools=[content_selection_tool],
    llm=chat_llm,
)

Flashcard_Generator = Agent(
    role="Flashcard Generator",
    goal="Break down the selected chapter into key concepts...",
    backstory="You are a seasoned educational content developer...",
    verbose=True,
    allow_delegation=False,
    tools=[concept_extraction_tool],
    llm=chat_llm,
)

Question_Designer = Agent(
    role="Question Designer",
    goal="Craft clear and concise questions...",
    backstory="You are an educational expert...",
    verbose=True,
    allow_delegation=False,
    tools=[question_creation_tool],
    llm=chat_llm,
)

Answer_Extractor = Agent(
    role="Answer Extractor",
    goal="Provide accurate answers to the questions...",
    backstory="You are an academic with a deep understanding...",
    verbose=True,
    allow_delegation=False,
    tools=[answer_extraction_tool],
    llm=chat_llm,
)

# Define tasks as you already have
task1 = Task(
    description="Parse the provided textbook and structure its contents into chapters and sections.",
    expected_output="A structured document with clearly defined chapters and sections.",
    agent=Textbook_Parser,
)

task2 = Task(
    description="Select the specific chapter requested by the user from the parsed textbook.",
    expected_output="The selected chapter content, ready for further analysis.",
    agent=Chapter_Selector,
)

task3 = Task(
    description="Break down the selected chapter into key concepts, terms, and details for flashcard creation.",
    expected_output="A list of key concepts and terms extracted from the chapter.",
    agent=Flashcard_Generator,
)

task4 = Task(
    description="Create questions based on the key concepts identified from the chapter.",
    expected_output="A set of well-formulated questions derived from the chapter's key concepts.",
    agent=Question_Designer,
)

task5 = Task(
    description="Extract and provide accurate answers to the questions designed.",
    expected_output="A set of question-answer pairs ready for flashcard use.",
    agent=Answer_Extractor,
)

# Run the process through Crew
crew = Crew(
    agents=[Textbook_Parser, Chapter_Selector, Flashcard_Generator, Question_Designer, Answer_Extractor],
    tasks=[task1, task2, task3, task4, task5],
    verbose=2,  # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)