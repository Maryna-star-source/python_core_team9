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

    def search_notes(self, keyword):
        result = []
        for title, content in self.notes.items():
            if keyword.lower() in title.lower() or keyword.lower() in content.lower():
                result.append(f"Title: {title}\nContent: {content}\n")
        return result if result else "No matching notes found."


@user_error
def add_tag(*args):
    title = args[0]
    tags = args[1:]
    return notes.add_tags(title, tags)


@user_error
def search_notes_by_tag(*args):
    tag = args[0]
    sort_by_keywords = args[1:].lower() == "true" if len(args) > 1 else False
    return notes.search_notes_by_tag(tag, sort_by_keywords)


@user_error
def add_note(*args):
    title = args[0]
    content_start_index = 1
    tags = []
    #  теги в аргументах
    for i, arg in enumerate(args[1:]):
        if arg.startswith("-tags="):
            tags = arg.split("=")[1].split(",")
            content_start_index = i + 1
            break
    content = " ".join(args[content_start_index:])
    new_note = Note(title, content, tags)
    notes.notes[title] = new_note
    return f"Note '{title}' added."


@user_error
def edit_note(*args):
    title = args[0]
    new_content_start_index = 1
    tags = []
    # теги в аргументах
    for i, arg in enumerate(args[1:]):
        if arg.startswith("--tags="):
            tags = arg.split("=")[1].split(",")
            new_content_start_index = i + 1
            break
    new_content = " ".join(args[new_content_start_index:])
    if title in notes.notes:
        notes.notes[title].content.edit_content(new_content)
        notes.notes[title].tags = Tags(tags)
        return f"Note '{title}' edited."
    else:
        return f"Note '{title}' not found."


@user_error
def search_notes(*keywords, notes):
    matching_notes = [
        f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}"
        for title, note in notes.items()
        if all(
            keyword.lower() in title.lower()
            or keyword.lower() in note["content"].lower()
            for keyword in keywords
        )
    ]
    if matching_notes:
        return "\n".join(matching_notes)
    else:
        return "No matching notes found."


@user_error
def delete_note(*args):
    title = args[0]
    if title in notes.notes:
        del notes.notes[title]
        return f"Note '{title}' deleted."
    else:
        return f"Note '{title}' not found."


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
