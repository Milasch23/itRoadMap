# 🗒️ CLI Notes Manager

![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=flat-square&logo=windows&logoColor=white)

A lightweight command-line application to manage personal notes, built with Python. Notes are stored persistently in a local JSON file. No external dependencies required — only Python's built-in modules.

## 📖 Overview

**CLI Notes Manager** is a beginner-friendly Python project that demonstrates core programming concepts through a practical, real-world application. You can create, list, search, and delete notes — all from your terminal — and every change is saved automatically to a local JSON file so your notes are never lost between sessions.

## ✨ Features

| Feature                  | Description                                        | Status |
| ------------------------ | -------------------------------------------------- | ------ |
| **Create notes**   | Write and save a new note to the file              | ✅     |
| **List notes**     | Display all saved notes with index numbers         | ✅     |
| **Search notes**   | Find notes by keyword (case-insensitive)           | ✅     |
| **Delete notes**   | Remove a note by its index number                  | ✅     |
| **Error handling** | Graceful handling if the notes file does not exist | ✅     |

## 📁 Project Structure

```
notes_cli/
├── notes.py         # Main application file
└── notes.json       # Auto-generated file where notes are stored (created on first run)
```

> **Note:** `notes.json` is created automatically the first time you save a note. You do not need to create it manually.


## ⚙️ Requirements

- **Python 3.6** or higher
- **No external libraries** — only built-in modules are used:

| Module   | Purpose                                                          |
| -------- | ---------------------------------------------------------------- |
| `json` | Serialize and deserialize notes to/from JSON format              |
| `os`   | Check whether the notes file exists before attempting to read it |


## 🚀 How to Run

**1. Clone or download the repository**

```bash
https://github.com/Milasch23/itRoadMap.git
```

**2. Navigate to the project folder**

```bash
cd week3/notes_cli
```

**3. Run the application**

```bash
python notes.py
```

> On some systems you may need to use `python3` instead of `python`.

## 🖥️ Usage

When you run the application, you will see the following menu in your terminal:

```
🗒️  Note Manager - Welcome

    1. Create a note
    2. Show notes
    3. Search a note
    4. Delete a note
    5. Exit

```

### Menu Options

| Option | Action                | Description                                |
| ------ | --------------------- | ------------------------------------------ |
| `1`  | **Create note** | Write and save a new note                  |
| `2`  | **List notes**  | Display all saved notes with index numbers |
| `3`  | **Search note** | Find notes containing a specific keyword   |
| `4`  | **Delete note** | Remove a note by its number                |
| `5`  | **Exit**        | Close the application                      |


## 💾 How Notes Are Stored

Notes are saved as a **JSON array** in `notes.json`, located in the same directory as `notes.py`. The file is created automatically on the first run — no setup needed.

**Example `notes.json`:**

```json
[
    "Buy groceries",
    "Study Python",
    "Call the dentist"
]
```

Each note is stored as a plain string. The entire list is overwritten on every save, ensuring the file always reflects the current state of your notes.

## 🧠 Key Concepts Used

| Concept                                               | Used For                                              |
| ----------------------------------------------------- | ----------------------------------------------------- |
| File I/O (`open()`, `"r"`, `"w"`)               | Reading and writing the notes file                    |
| JSON serialization (`json.load()`, `json.dump()`) | Converting between Python lists and JSON              |
| `os.path.exists()`                                  | Checking if the notes file exists before reading      |
| `try/except ValueError`                             | Handling invalid user input (non-numeric)             |
| List comprehensions                                   | Filtering notes by keyword in search                  |
| `while True` + `break`                            | Keeping the menu running until the user exits         |
| `if __name__ == "__main__"`                         | Entry point guard to prevent auto-execution on import |
| `enumerate(start=1)`                                | Displaying notes with 1-based numbering               |


## 📄 License

This project is open source and available under the [MIT License](LICENSE).

> Built with 🐍 Python — no frameworks, no dependencies, just clean code.