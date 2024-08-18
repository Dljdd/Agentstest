from crewai_tools import LlamaIndexTool

class AnswerExtractionTool(LlamaIndexTool):
    def __init__(self, query_engine):
        self.query_engine = query_engine
    
    def extract_answers(self, questions, chapter_content):
        answers = []
        for question in questions:
            answer = self.query_engine.query(question)
            answers.append(answer)
        return answers