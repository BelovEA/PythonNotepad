import datetime
import json

import datetime
import json


def WriteToNotepad():
    newNoteTitle = input("Enter your Title: ")
    newNoteText = input("Enter your note: ")
    note = {
        "title": newNoteTitle,
        "date": datetime.datetime.now().isoformat(),
        "text": newNoteText
    }

    try:
        with open("Notepad.json", 'r') as file:
            notes = json.load(file)
            if not isinstance(notes, list):
                notes = []
    except FileNotFoundError:
        notes = []

    notes.append(note)

    with open("Notepad.json", 'w') as f_writer:
        json.dump(notes, f_writer, indent=4)


def ReadFromNotepad(date_filter=None):
    try:
        with open("Notepad.json", 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("No notes file found.")
        return

    if date_filter:
        filtered_notes = [note for note in notes if note['date'].startswith(date_filter)]
        for note in filtered_notes:
            print(f"Title: {note['title']}\nDate: {note['date']}\nNote: {note['text']}\n")
    else:
        for note in notes:
            print(f"Title: {note['title']}\nDate: {note['date']}\nNote: {note['text']}\n")

def EditNotes():
    title_to_edit = input("Enter the title of the note to edit: ")
    try:
        with open("Notepad.json", 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("No notes file found.")
        return


    for note in notes:
        if note['title'] == title_to_edit:
            print(f"Current Note: {note['text']}")
            new_text = input("Enter new text for the note: ")
            note['text'] = new_text
            note['date'] = datetime.datetime.now().isoformat()
            break
    else:
        print("Note not found.")
        return


    with open("Notepad.json", 'w') as file:
        json.dump(notes, file, indent=4)
    print("Note updated successfully.")

def DeleteNotes():
    title_to_delete = input("Enter the title of the note to delete: ")
    try:
        with open("Notepad.json", 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("No notes file found.")
        return


    notes = [note for note in notes if note['title'] != title_to_delete]


    with open("Notepad.json", 'w') as file:
        json.dump(notes, file, indent=4)
        print("Note deleted successfully.")

WriteToNotepad()
print(ReadFromNotepad())
EditNotes()
print(ReadFromNotepad())
DeleteNotes()
print(ReadFromNotepad())