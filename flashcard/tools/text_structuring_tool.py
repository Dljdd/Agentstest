from crewai_tools import LlamaIndexTool

class TextStructuringTool(LlamaIndexTool):
    def __init__(self):
        pass
    
    def structure_text(self, raw_text):
        structured_content = {}
        chapters = raw_text.split("Chapter")
        
        for idx, chapter in enumerate(chapters[1:], 1):
            chapter_title = f"Chapter {idx}"
            sections = chapter.split("\n\n")
            structured_content[chapter_title] = sections
        
        return structured_content
