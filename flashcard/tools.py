
from crewai_tools import LlamaIndexTool
from rag_embed import query_engine

import pdfplumber

query_tool = LlamaIndexTool.from_query_engine(
    query_engine,
    name="research paper query tool",
    description="Use this tool to lookup research papers",
)

query_tool.args_schema.schema()

