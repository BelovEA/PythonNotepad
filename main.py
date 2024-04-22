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

    with open("Notepad.json", 'a') as f_writer:
        json.dump(note, f_writer)
        f_writer.write("\n")

