from crewai_tools import LlamaIndexTool


class ContentSelectionTool(LlamaIndexTool):
    def __init__(self, structured_content):
        self.structured_content = structured_content
    
    def select_chapter(self, chapter_title):
        selected_chapter = self.structured_content.get(chapter_title, None)
        if not selected_chapter:
            raise ValueError(f"Chapter titled '{chapter_title}' not found.")
        return selected_chapter
