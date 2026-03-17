import os

# FILE HANDLING

file1 = open("file_name.txt", "w", encoding = "utf-8") 



# Opening modes

file2 = open("file_name2.txt", "r", encoding = "utf-8") # Read-only. Error if the file doesn't exist

file3 = open("file_name3.txt", "w", encoding = "utf-8") # Write-only: Writes. Overwrites if it exists, creates if it doesn't

file4 = open("file_name4.txt", "a", encoding = "utf-8") # Append. Writes at the end, without erasing. Creates if it doesn't exist

file5 = open("file_name5.txt", "r+", encoding = "utf-8") # Reading + Writing. It reads and writes. Error if the file doesn't exist

file6 = open("file_name5.txt", "w+", encoding = "utf-8") # Writing + Reading. Overwrites if the file exists

file7 = open("file_name6.txt", "a+", encoding = "utf-8") # Reads and adds at the end

file8 = open("file_name7.txt", "rb", encoding = "utf-8") # Or 'wb'. Binary mode. Byte reading and writing

file9 = open("file_name8.txt", "x", encoding = "utf-8") # Exclusive creation. Creates a new file. Error if the file already exists



# Best practice - With Block

# RECOMMENDED METHOD — guaranteed automatic closure
with open("file_name9.txt", "r", encoding = "utf-8") as file:
    content = file.read()
    print(content)
# The file is closed automatically here


# MANUAL METHOD - You have to close the file yourself
file10 = open("file_name10.txt", "r", encoding = "utf-8")
content2 = file10.read()
file10.close()



# File Reading

# .read() <<-- Reads all the content
with open("file_name11.txt", "r", encoding = "utf-8") as fileA:
    all_text = fileA.read() # Reads the entire file as a string
    print(all_text)

with open("file_name12.txt", "r", encoding = "utf-8") as fileB:
    first_50 = fileB.read(50) # Reads only the 50 first characters


# .readline() <<-- It reads line by line
with open("file_name13.txt", "r", encoding = "utf-8") as fileC:
    first_line = fileC.readline() # This reads the first line
    second_line = fileC.readline() # This one reads the second line
    print(first_line + second_line)


# .readlines() <<-- Returns a list of lines
with open("file_name14.txt", "r", encoding = "utf-8") as fileD:
    lines = fileD.readlines()
    for line in lines:
        print(line.strip())


# Direct Iteration - More memory-efficient
with open("big_file.txt", "r", encoding = "utf-8") as fileE:
    for line in fileE: # This loop reads line by line without loading everything
        print(line.strip())



# File Writing

# .write() <<--It writes a string
with open("hello_file.txt", "w", encoding = "utf-8") as f:
    f.write("Hello, World!\n")
    f.write("This is the second line!\n")


# writelines() <<-- It writes a list of Strings
fruits = ["Apple\n", "Strawberry\n", "Peach\n"]
with open("fruits.txt", "w", encoding = "utf-8") as f:
    f.writelines(fruits)


# 'a' Mode <<-- Adding without erasing
with open("log.txt", "a", encoding="utf-8") as f: 
    f.write("New record: 2025-08-12") #Adds at the end of the file



# Other Object File Methods
with open("hello_file.txt", "r", encoding = "utf-8") as f:
    seek1 = f.seek(3) # Moves the cursor to that position
    tell1 = f.tell() # Returns the current cursor position
    flush1 = f.flush() # Flush the buffer to disk
    truncate1 = f.truncate() # Trims the file to n bytes



# Exception handling with files

# Never assume that a file exists

try:
    with open("data.txt", "r", encoding = "utf-8") as f:
        content3 = f.read()
        print(content3)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("You don't have permission to access the file.")

except IsADirectoryError:
    print("The path points to a directory, not a file.")

except IOError as e:
    print("I/O Error")

except Exception as e:
    print("Unexpected Error")

finally:
    print("Operation completed (with or without an error).")


# Verifying if the file exists
path = "data_file.txt"
if os.path.exists(path):
    with open(path, "r", encoding = "utf-8") as f:
        print(f.read())
else: 
    print(f"'{path}' doesn't exists.")

