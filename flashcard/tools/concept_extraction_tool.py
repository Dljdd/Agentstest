from crewai_tools import LlamaIndexTool
from rag_embed import embed_model

class ConceptExtractionTool(LlamaIndexTool):
    def __init__(self, embed_model):
        super().__init__()  # Call the parent class's initializer if it has one
        self.embed_model = embed_model
    
    def extract_concepts(self, chapter_content):
        # Use an embedding model or NLP techniques to find key concepts
        concepts = self.embed_model.get_keywords(chapter_content, top_k=20)
        return concepts
