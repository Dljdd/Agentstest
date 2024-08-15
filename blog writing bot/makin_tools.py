from llama_index.legacy.tools.tool_spec.base import BaseToolSpec

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os


load_dotenv()
# Define your API key here
groq_api_key = os.getenv('GROQ_API_KEY')

chat_llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=groq_api_key,
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=3500,
)
class SEOTool(BaseToolSpec):

    def generate_strategy(self, topic):
        message = HumanMessage(
            content=[
                {"type": "text", "text": f"I want you to act as a SEO Strategist and provide me with a detailed analysis of the top SEO keywords related to {topic} along with an in-depth analysis of their search volume, competition, and potential ranking opportunities."},
                    ]
        )
        ai_msg = chat_llm.invoke([message])
        strategy = ai_msg.content
        return strategy
    

# seo = SEOTool()

# print(seo.generate_strategy("Flux Model"))