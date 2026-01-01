# Lesson 6: File Operations

## Reading Files

### Reading Entire File
```python
# Method 1: Using with statement (recommended)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed after the with block

# Method 2: Manual open/close
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # Important: always close!
```

### Reading Line by Line
```python
# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline characters

# Read one line at a time (memory efficient for large files)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read single line
with open("example.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
```

## Writing Files

### Write Mode (Overwrites existing content)
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Append Mode (Adds to existing content)
```python
with open("output.txt", "a") as file:
    file.write("This line is appended.\n")
    file.write("Another appended line.\n")
```

## File Modes
- `"r"` - Read (default). File must exist.
- `"w"` - Write. Creates new file or overwrites existing.
- `"a"` - Append. Adds to end of file.
- `"r+"` - Read and write.
- `"b"` - Binary mode (e.g., `"rb"`, `"wb"`)

## Working with CSV Files

### Reading CSV
```python
import csv

# Reading CSV file
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # Each row is a list

# Reading CSV with dictionary
with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row["name"], row["age"])  # Access by column name
```

### Writing CSV
```python
import csv

# Writing CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open("output.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Writing with dictionary
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)
```

## Working with JSON Files

### Reading JSON
```python
import json

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Parse JSON string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data["name"])
```

### Writing JSON
```python
import json

# Write to JSON file
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding", "gaming"]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
```

## File and Directory Operations

### Using os module
```python
import os

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists")

# Get file size
size = os.path.getsize("example.txt")
print(f"File size: {size} bytes")

# List files in directory
files = os.listdir(".")
print(files)

# Create directory
os.mkdir("new_folder")

# Remove file
os.remove("temp.txt")

# Remove directory
os.rmdir("old_folder")

# Get current directory
current_dir = os.getcwd()
print(current_dir)

# Change directory
os.chdir("/path/to/directory")
```

### Using pathlib (Modern approach)
```python
from pathlib import Path

# Create Path object
file_path = Path("example.txt")

# Check if exists
if file_path.exists():
    print("File exists")

# Read file
content = file_path.read_text()

# Write file
file_path.write_text("Hello, World!")

# Get file info
print(file_path.name)       # filename
print(file_path.suffix)     # extension
print(file_path.parent)     # parent directory

# List directory
directory = Path(".")
for file in directory.iterdir():
    print(file.name)
```

## Error Handling with Files
```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Practice Exercises
1. Write a program that reads a text file and counts the number of words
2. Create a program that reads a file and writes its content in reverse to a new file
3. Write a program that reads a CSV file of student grades and calculates the average
4. Create a program that writes a list of dictionaries to a JSON file
5. Write a program that searches for a specific word in a file and prints the line numbers where it appears
6. Create a program that copies content from one file to another

## Summary
You've now learned the fundamentals of Python programming:
- Basic syntax and printing
- Variables and data types
- Control flow (if/else, loops)
- Functions
- Data structures (lists, tuples, dictionaries, sets)
- File operations

Keep practicing these concepts to become proficient in Python!
