"""
Solutions for Exercise 6: File Operations
==========================================
"""

import json
import csv

# Exercise 6.1: Write to file
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Exercise 6.2: Read from file
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# Exercise 6.3: Append to file
with open("output.txt", "a") as file:
    file.write("Line 4\n")
    file.write("Line 5\n")

# Exercise 6.4: Count words in file
def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 0

word_count = count_words("output.txt")
print(f"Word count: {word_count}")

# Exercise 6.5: Copy file
def copy_file(source, destination):
    try:
        with open(source, "r") as src:
            content = src.read()
        with open(destination, "w") as dst:
            dst.write(content)
        print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")

copy_file("output.txt", "copy.txt")

# Exercise 6.6: Read line by line
with open("output.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"{line_num}: {line.strip()}")

# Exercise 6.7: Search in file
def search_in_file(filename, search_word):
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                if search_word in line:
                    print(f"Found on line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print("File not found")

search_in_file("output.txt", "Line")

# Exercise 6.8: Reverse file content
def reverse_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()
        with open(output_file, "w") as file:
            file.writelines(reversed(lines))
    except FileNotFoundError:
        print("File not found")

reverse_file("output.txt", "reversed.txt")

# Exercise 6.9: Write CSV
students_data = [
    ["Name", "Age", "Grade"],
    ["Alice", "20", "A"],
    ["Bob", "22", "B"],
    ["Charlie", "21", "A"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

# Exercise 6.10: Read CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))

# Exercise 6.11: Write JSON
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

with open("books.json", "w") as file:
    json.dump(books, file, indent=4)

# Exercise 6.12: Read JSON
with open("books.json", "r") as file:
    books_data = json.load(file)
    for book in books_data:
        print(f"{book['title']} by {book['author']} ({book['year']})")

# Exercise 6.13: File statistics
def file_statistics(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            lines = content.split("\n")
            words = content.split()
            chars = len(content)
            return {
                "lines": len(lines),
                "words": len(words),
                "characters": chars
            }
    except FileNotFoundError:
        return None

stats = file_statistics("output.txt")
if stats:
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")

# Exercise 6.14: Filter file
def filter_even_numbers(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            numbers = [int(line.strip()) for line in file]
        with open(output_file, "w") as file:
            for num in numbers:
                if num % 2 == 0:
                    file.write(f"{num}\n")
    except FileNotFoundError:
        print("File not found")

# Exercise 6.15: Merge files
def merge_files(file1, file2, output_file):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            content1 = f1.read()
            content2 = f2.read()
        with open(output_file, "w") as out:
            out.write(content1)
            out.write("\n")
            out.write(content2)
    except FileNotFoundError:
        print("One or more files not found")

# Exercise 6.16: Log file parser

def create_log():
    with open("app.log", "w") as file:
        file.write("2024-01-01 10:00:00 - INFO - Application started\n")
        file.write("2024-01-01 10:05:00 - WARNING - Low memory\n")
        file.write("2024-01-01 10:10:00 - ERROR - Connection failed\n")

def parse_log(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) == 3:
                    timestamp, level, message = parts
                    print(f"[{level}] {timestamp}: {message}")
    except FileNotFoundError:
        print("Log file not found")

create_log()
parse_log("app.log")
