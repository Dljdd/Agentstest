from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.voyageai import VoyageEmbedding

from agents import llm
import os
from dotenv import load_dotenv



load_dotenv()

#load the doc
reader = SimpleDirectoryReader(input_dir="./data")
docs = reader.load_data()

# load embedding model

model_name = "voyage-large-2-instruct"

voyage_api_key = os.getenv('VOYAGE_API_KEY')

embed_model = VoyageEmbedding(
    model_name=model_name, voyage_api_key=voyage_api_key
)

index = VectorStoreIndex.from_documents(docs,
                                        embed_model=embed_model,
                                        )

query_engine = index.as_query_engine(similarity_top_k=5, llm=llm)


