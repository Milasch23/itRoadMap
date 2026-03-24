import string

# Exercise 1 - Write a program that reads a text file (for example, text.txt) and displays:

# The total number of words.

# The longest word.

def read_file(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None
    
def word_clean(word):
    return word.strip(string.punctuation).lower()

def text_proc(text):
    if not text:
        return [], 0, None
    
    raw_words = text.split()
    words = [word_clean(w) for w in raw_words if word_clean(w)]
    total = len(words)
    longest = max(words, key=len) if words else None

    return words, total, longest

def show_results(total, longest):
    print(f"Words total {total}")
    if longest:
        print(f"Longest word: {longest}")

def main():
    file_name = "week3/integrated_exercises/text.txt"
    content = read_file(file_name)

    if content is not None:
        words, total, longest = text_proc(content)
        show_results(total, longest)

if __name__ == "__main__":
    main()

