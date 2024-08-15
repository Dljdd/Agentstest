
from crewai_tools import LlamaIndexTool
# from rag_embed import query_engine
from makin_tools import SEOTool
from crewai_tools import SerperDevTool
import os

os.environ["SERPER_API_KEY"] =os.getenv('SERPER_API_KEY')

query_tool = SerperDevTool()

seo_tool = SEOTool()


