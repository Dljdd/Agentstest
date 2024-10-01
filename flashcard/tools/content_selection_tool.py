from crewai_tools import LlamaIndexTool
from pydantic import BaseModel

class ContentSelectionTool(BaseModel):
    structured_content: dict  # Declare the field with an appropriate type

    def select_chapter(self, chapter_title: str):
        selected_chapter = self.structured_content.get(chapter_title, None)
        if not selected_chapter:
            raise ValueError(f"Chapter titled '{chapter_title}' not found.")
        return selected_chapter
