from collections import UserDict
from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
from datetime import datetime
import os.path
import pickle
from classes import Field


class NoteError:
    ...


class Title(Field):
    pass


class Content(Field):
    def edit_content(self, new_content):
        self.value = new_content


class Tags(Field):
    def __init__(self, tags=None):
        super().__init__(tags or [])

    def add_tags(self, new_tags):
        self.value.extend(new_tags)


class Note:
    def __init__(self, title, content, tags=None):
        self.title = Title(title)
        self.content = Content(content)
        self.tags = Tags(tags)

    def add_note(self, title, content):
        self.notes[title] = content
        return f"note {self.title} has been successfully added \n\t{self}"

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

    def search_notes_by_tag(self, tag, sort_by_keywords=False):
        matching_notes = [
            f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}"
            for title, note in self.notes.items()
            if tag.lower() in map(str.lower, note["tags"])
        ]

    def add_tags(self, title, tags):  # метод для додавання тегів
        if title in self.notes:
            self.notes[title].tags.extend(tags)
            return f"Tags {', '.join(tags)} added to the note with title '{title}'."
        else:
            raise NoteError(f"Note with title '{title}' not found.")

    def search_notes_by_tag(self, tag, sort_by_keywords=False):
        matching_notes = [
            note
            for note in self.notes.values()
            if tag.lower() in map(str.lower, note.tags)
        ]
        if sort_by_keywords:
            matching_notes.sort(key=lambda note: note.keywords)
        if matching_notes:
            return "\n".join(map(str, matching_notes))
        else:
            return "No notes found with the specified tag."


# from collections import UserDict
# from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
# from datetime import datetime
# import os.path
# import pickle
# from classes import Field


# class Note:
#     def __init__(self, title: str, content: str):
#         self.title = title
#         self.notes = content

#     def add_note(self, title, content):
#         self.notes[title] = content

#     def edit_note(self, title, new_content):
#         if title in self.notes:
#             self.notes[title] = new_content
#             return f"Note '{title}' edited."
#         else:
#             return f"Note '{title}' not found."

#     def delete_note(self, title):
#         if title in self.notes:
#             del self.notes[title]
#             return f"Note '{title}' deleted."
#         else:
#             return f"Note '{title}' not found."


# class NotesBook(UserDict):
#     def __init__(self):
#         self.notes = {}

#     def add_tags(self, title, tags): # метод для додавання тегів
#         if title in self.notes:
#             self.notes[title].tags.extend(tags)
#             return f"Tags {', '.join(tags)} added to the note with title '{title}'."
#         else:
#             raise NoteError(f"Note with title '{title}' not found.")


#     def search_notes(self, keyword):
#         result = []
#         for title, content in self.notes.items():
#             if keyword.lower() in title.lower() or keyword.lower() in content.lower():
#                 result.append(f"Title: {title}\nContent: {content}\n")
#         return result if result else "No matching notes found."
