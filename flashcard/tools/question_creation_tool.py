from crewai_tools import LlamaIndexTool



class QuestionCreationTool(LlamaIndexTool):
    def __init__(self, llm):
        self.llm = llm
    
    def create_questions(self, key_concepts):
        questions = []
        for concept in key_concepts:
            prompt = f"Create a question related to the concept: {concept}"
            question = self.llm(prompt)
            questions.append(question)
        return questions