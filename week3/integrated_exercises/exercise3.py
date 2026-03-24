# Exercise 3 - Log File Analyzer

def read_log(file_name):
    processed_lines = []

    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                if not line:
                    continue

                parts = line.split(maxsplit=3)
                
                if len(parts) >= 3:
                    level = parts[2]
                    message = parts[3] if len(parts) > 3 else ""
                    processed_lines.append((level, message))
                else:
                    print(f"Line {line_num}: Unrecognized format -> {line}")
    
    except FileNotFoundError:
        print("File not found")
        return None
    
    return processed_lines


def analyze_log(logs):
    counter = {}
    errors = []

    for level, message in logs:
        counter[level] = counter.get(level, 0) + 1
        if level == "ERROR":
            errors.append(message)
    
    return counter, errors


def generate_report(output_name, counter, errors):
    
    try:
        with open(output_name, 'w', encoding="utf-8") as file:
            file.write("*-*-*-* LOG REPORT *-*-*-*\n\n")
            file.write("Level count:\n")

            for level, amount in sorted(counter.items()):
                file.write(f"  {level}: {amount}\n")
            
            file.write(f"Number of errors: {len(errors)}\n\n")
            file.write("Errors list:\n")

            for i, err in enumerate(errors, 1):
                file.write(f"{i}. {err}\n")
        
        print(f"Report saved in {output_name}")

    except IOError as e:
        print(f"Error: {e}")


def main():
    inputs = read_log("week3/integrated_exercises/log.txt")
    if inputs is not None:
        counter, errors = analyze_log(inputs)
        generate_report("week3/integrated_exercises/report.txt", counter, errors)

if __name__ == "__main__":
    main()