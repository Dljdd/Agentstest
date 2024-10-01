from dotenv import load_dotenv
import os
from llama_index.llms.groq import Groq
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process


from tools.pdf_parsing_tool import PDFParsingTool
from tools.text_structuring_tool import TextStructuringTool
from tools.content_selection_tool import ContentSelectionTool
from tools.concept_extraction_tool import ConceptExtractionTool
from tools.question_creation_tool import QuestionCreationTool
from tools.answer_extraction_tool import AnswerExtractionTool

from rag_embed import embed_model

load_dotenv()
# Define your API key here
groq_api_key = os.getenv('GROQ_API_KEY')

chat_llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=groq_api_key,
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=1000,
)

llm = Groq(model="llama-3.1-70b-versatile", api_key=groq_api_key)

pdf_parsing_tool = PDFParsingTool(file_path="flashcard/data/probability and statistics - T.Veerarajan.pdf")
text_structuring_tool = TextStructuringTool()
# Assume `structured_content` comes from the text structuring tool
content_selection_tool = ContentSelectionTool(structured_content={})
concept_extraction_tool = ConceptExtractionTool(embed_model=embed_model)
question_creation_tool = QuestionCreationTool(llm=your_llm)
answer_extraction_tool = AnswerExtractionTool(query_engine=your_query_engine)

PDF_Parser = Agent(
    role="PDF Parser",
    goal="Extract and parse text from a PDF document.",
    backstory="You are an expert in document processing and text extraction and are able to segregate data based on its relevance",
    verbose=True,
    allow_delegation=False,
    tools=[pdf_parsing_tool],
    llm=your_llm,
)

Text_Structurer = Agent(
    role="Text Structurer",
    goal="Organize extracted text into structured chapters and sections.",
    backstory="You are a content organization specialist...",
    verbose=True,
    allow_delegation=False,
    tools=[text_structuring_tool],
    llm=llm,
)

Chapter_Selector = Agent(
    role="Chapter Selector",
    goal="Identify and select the specific chapter(s) requested by the user...",
    backstory="You are an expert content navigator...",
    verbose=True,
    allow_delegation=False,
    tools=[content_selection_tool],
    llm=llm,
)

Flashcard_Generator = Agent(
    role="Flashcard Generator",
    goal="Break down the selected chapter into key concepts...",
    backstory="You are a seasoned educational content developer...",
    verbose=True,
    allow_delegation=False,
    tools=[concept_extraction_tool],
    llm=llm,
)

Question_Designer = Agent(
    role="Question Designer",
    goal="Craft clear and concise questions...",
    backstory="You are an educational expert...",
    verbose=True,
    allow_delegation=False,
    tools=[question_creation_tool],
    llm=llm,
)

Answer_Extractor = Agent(
    role="Answer Extractor",
    goal="Provide accurate answers to the questions...",
    backstory="You are an academic with a deep understanding...",
    verbose=True,
    allow_delegation=False,
    tools=[answer_extraction_tool],
    llm=llm,
)
