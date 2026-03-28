import json # Used to serialize/deserialize notes to/from JSON format
import os # Used to check if the notes file exists before reading it

FILE = "week3/notes_cli/notes.json" # Path to the file where notes will be stored

def upload_notes(): # Load notes from the JSON file
    
    # If the file doesn't exist, return an empty list to avoid FileNotFoundError 
    if not os.path.exists(FILE):
        return [] 
    
    # Open the file in read mode and deserialize its JSON content into a Python list
    with open(FILE, 'r', encoding='utf-8') as file:
        return json.load(file) 
    

def save_notes(notes): # Save the current list of notes to the JSON file

    # Open the life in write mode and serialize the list into formatted JSON
    with open(FILE, 'w', encoding='utf-8') as file:

        # indent=4 makes the JSON human-readable
        # ensure_ascii=False allows special characters
        json.dump(notes, file, indent=4, ensure_ascii=False)


def create_note(): # prompt the user to write a new note and save it

    text = input("Write your note: ").strip() # Remove accidental leading/trailing

    # Prevent saving an empty note
    if not text:
        print("The note cannot be empty.")
        return
    
    # Load existing notes, append the new one, then save
    notes = upload_notes()
    notes.append(text) # Add the new note to the end of the list 
    save_notes(notes) # Persist the updated list to the file
    print("Note successfully saved.")


def show_notes(): # Display all saved notes with their index numbers
    notes = upload_notes()
    
    # Handle the case where there are no notes yet
    if not notes:
        print("There are no notes uploaded")
        return
    
    print("\n Notes: ")
    print("*-" * 30)

    # enumerate(start=1) = start the counter at 1 instead of 0
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
    print("*-" * 30)


def search_note(): # Search for notes containing a specific keyword

    # Convert input to lowercase to enable case-insensitive matching
    term = input("Enter the word you are looking for: ").strip().lower()

    # Prevent searching with an empty term
    if not term:
        print("You must type something.")
        return
    
    notes = upload_notes()

    results = []
    for note in notes:
        if term in note.lower():
            results.append(note)

    # Inform the user if no matches were found
    if not results:
        print(f"Notes with '{term}' not found.")
        return
    

    print(f"Results for {term}")
    print("*-" * 30)
    for i, note in enumerate(results, start=1):
        print(f"{i}. {note}")
    print("*-" * 30)


def delete_note(): # Show all notes and delete the one selected by the user

    # Display notes first so the user knows which number to pick
    show_notes()
    notes = upload_notes()

    # If there are no notes, show_notes() already inform the user - just exit
    if not notes:
        return
    
    try:
        # Convert user input to integer - may raise ValueError if input is not numeric
        number = int(input("Which note do you want to delete?: "))

        # Validate that the number is within the valid range of existing notes
        if number < 1 or number > len(notes):
            print("That number doesn't correspond to any note.")
            return
        
        # pop() removes the element at the given index and returns it 
        # number - 1 converts from 1-based (user) to 0-based (Python list) indexing
        deleted = notes.pop(number - 1)
        save_notes(notes) # Save the list without the deleted note
        print(f"Deleted note: '{deleted}'")

    except ValueError:
        # Triggered when the user types something that can't be converted to int
        print("Please enter a valid number.")


def menu(): # Main loop of the application
    print("Note Manager - Welcome") # Shown only once at startup

    # Keep the menu running until the user explicitly chooses to exit
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
                break # exit the match loop, ending the program 
            case _: 
                # Catch any input that doesn't match the valid options
                print("Please, enter a valid number.")


# Only run the app if this file is executed directly
# Prevents menu() from running if this module is imported elsewhere
if __name__ == "__main__":
    menu()
