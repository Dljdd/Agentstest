
from crewai_tools import LlamaIndexTool
from rag_embed import query_engine
query_tool = LlamaIndexTool.from_query_engine(
    query_engine,
    name="psych query tool",
    description="Use this tool to lookup psychology research papers",
)

query_tool.args_schema.schema()