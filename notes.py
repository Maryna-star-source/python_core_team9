from collections import UserDict
from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
from datetime import datetime
import os.path
import pickle
from classes import Field 


class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.notes = content
        
    def add_note(self, title, content):
        self.notes[title] = content 

    def edit_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            return f"Note '{title}' edited."
        else:
            return f"Note '{title}' not found." 

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            return f"Note '{title}' deleted."
        else:
            return f"Note '{title}' not found."
                
    
class NotesBook(UserDict):
    def __init__(self):
        self.notes = {} 

                                    
    def search_notes(self, keyword): 
        result = []
        for title, content in self.notes.items():
            if keyword.lower() in title.lower() or keyword.lower() in content.lower():
                result.append(f"Title: {title}\nContent: {content}\n")
        return result if result else "No matching notes found."

