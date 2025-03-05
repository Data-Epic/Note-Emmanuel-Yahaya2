# This is a test change for the PRgit add test.py
from datetime import datetime


# Base Class
class Note:
    def __init__(self, content):
        self.content = content
        self.created_at = datetime.now()

    def display(self):
        return f"[Created at: {self.created_at}] {self.content}"


# Subclass: TextNote
class TextNote(Note):
    def display(self):
        return f"[Text Note] {super().display()}"


# Subclass: ReminderNote
class ReminderNote(Note):
    def __init__(self, content, reminder_time):
        super().__init__(content)
        self.reminder_time = reminder_time

    def display(self):
        return f"[Reminder Note] {super().display()} | Reminder: {self.reminder_time}"


# Notes Manager
class NotesManager:
    def __init__(self):
        self.notes = []
        self.counter = 1

    def add_note(self, note_type, content, reminder_time=None):
        if note_type.lower() == "text":
            note = TextNote(content)
        elif note_type.lower() == "reminder":
            note = ReminderNote(content, reminder_time)
        else:
            print("Invalid note type!")
            return

        self.notes.append((self.counter, note))
        print(f"Note added with ID: {self.counter}")
        self.counter += 1

    def delete_note(self, note_id):
        self.notes = [(id, note) for id, note in self.notes if id != note_id]
        print(f"Note {note_id} deleted!")

    def show_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            for id, note in self.notes:
                print(f"ID {id}: {note.display()}")

    def search_notes(self, keyword):
        results = [(id, note) for id, note in self.notes if keyword.lower() in note.content.lower()]
        if results:
            for id, note in results:
                print(f"ID {id}: {note.display()}")
        else:
            print("No matching notes found.")


# Interactive Testing
if __name__ == "__main__":
    manager = NotesManager()

    while True:
        print("\nOptions: [1] Add Note  [2] Show Notes  [3] Search  [4] Delete  [5] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            note_type = input("Enter note type (text/reminder): ").strip().lower()
            content = input("Enter note content: ").strip()
            reminder_time = input("Enter reminder time (or press Enter to skip): ").strip()
            reminder_time = reminder_time if reminder_time else None
            manager.add_note(note_type, content, reminder_time)

        elif choice == "2":
            manager.show_notes()

        elif choice == "3":
            keyword = input("Enter keyword to search: ").strip()
            manager.search_notes(keyword)

        elif choice == "4":
            note_id = int(input("Enter note ID to delete: ").strip())
            manager.delete_note(note_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again!")







