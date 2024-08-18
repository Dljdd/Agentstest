import pdfplumber
from crewai_tools import LlamaIndexTool

class PDFParsingTool(LlamaIndexTool):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def parse_pdf(self):
        with pdfplumber.open(self.file_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
        
        return full_text
