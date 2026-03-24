# Exercise 2 - Write a program that reads a CSV file (data.csv) with two columns: name and age.

# Calculate the average age.

# Write the average and a sorted list of names to a new file (summary.txt).

# Handle malformed lines (those that do not have two fields or where the age is not a number) by ignoring them and logging an error message.

# Use functions to read, process, and write.

def read_csv(file_name):
    data = []

    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                if not line:
                    continue
                parts = line.split(',')
                
                if len(parts) != 2:
                    print(f"Line {line_num}: invalid format (Two fields were expected) -> {line}")
                    continue
                
                name, age_str = parts

                try:
                    age = int(age_str)
                    data.append((name.strip(), age))

                except ValueError:
                    print(f"Line {line_num}: Non-numerical age -> {age_str}")
    
    except FileNotFoundError:
        print("File not found.")
        return None
    
    return data


def calculate_average(data):
    if not data:
        return 0
    
    total = sum(age for _, age in data)

    return total / len(data)


def write_summ(name_output, average, data):
    try: 
        with open(name_output, 'w', encoding="utf-8") as file:
            file.write(f"Age average: {average:2f}\n")
            file.write("Sorted names:\n")
            names = sorted([name for name, _ in data])

            for name in names:
                file.write(f"- {name}")
        
        print(f"Summary saved in {name_output}")
    
    except IOError as e:
        print(f"Error: {e}")


def main(): 
    data = read_csv("week3/integrated_exercises/data.csv")

    if data is not None:
        average = calculate_average(data)
        write_summ("week3/integrated_exercises/summary.txt", average, data)


if __name__ == "__main__":
    main()