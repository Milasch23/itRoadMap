import json
import os

FILE = "notes.json"

def upload_notes():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding='utf-8') as file:
        return json.load(file)
    

def save_notes(notes):
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)


def create_note():
    text = input("Write your note: ").strip()
    if not text:
        print("The note cannot be empty.")
        return
    notes = upload_notes()
    notes.append(text)
    save_notes(notes)
    print("Note successfully saved.")


def show_notes():
    notes = upload_notes()
    if not notes:
        print("There are no notes uploaded")
        return
    print("\n Notes: ")
    print("*-" * 30)
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
    print("*-" * 30)


def search_note():
    term = input("Enter the word you are looking for: ").strip().lower()
    if not term:
        print("You must type something.")
        return
    notes = upload_notes()
    results = []
    for note in notes:
        if term in note.lower():
            results.append(note)
    if not results:
        print(f"Notes with '{term}' not found.")
        return
    print(f"Results for {term}")
    print("*-" * 30)
    for i, note in enumerate(results, start=1):
        print(f"{i}. {note}")
    print("*-" * 30)


def delete_note():
    show_notes()
    notes = upload_notes()
    if not notes:
        return
    try:
        number = int(input("Which note do you want to delete?: "))
        if number < 1 or number > len(notes):
            print("That number doesn't correspond to any note.")
            return
        deleted = notes.pop(number - 1)
        save_notes(notes)
        print(f"Deleted note: '{deleted}'")
    except ValueError:
        print("Please enter a valid number.")


def menu():
    print("Note Manager - Welcome")
    while True:
        print("1. Create a note")
        print("2. Show notes")
        print("3. Search a note")
        print("4. Delete a note")
        print("5. Exit")
        option = int(input("Please, select an option: "))
        match option:
            case 1:
                create_note()
            case 2:
                show_notes()
            case 3:
                search_note()
            case 4:
                delete_note()
            case 5: 
                print("See you later!")
                break
            case _: 
                print("Please, enter a valid number.")


if __name__ == "__main__":
    menu()
