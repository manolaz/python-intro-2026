"""
Solutions for Exercise 5: Data Structures
==========================================
"""

# Exercise 5.1: Create and access list
movies = ["The Matrix", "Inception", "Interstellar", "The Shawshank Redemption", "Pulp Fiction"]
print(movies[2])  # Third movie (index 2)

# Exercise 5.2: Modify list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
print(numbers)  # [0, 1, 2, 3, 4, 5, 6]

# Exercise 5.3: Remove duplicates
original = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(original))
print(sorted(unique))  # [1, 2, 3, 4, 5]

# Exercise 5.4: List slicing
numbers = list(range(10))
even_numbers = numbers[::2]
print(even_numbers)  # [0, 2, 4, 6, 8]

# Exercise 5.5: List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 5.6: Filter list
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
filtered = [x for x in numbers if x > 5]
print(filtered)  # [7, 9, 6, 8, 10]

# Exercise 5.7: Create dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 92, 88]
}

# Exercise 5.8: Access dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Exercise 5.9: Update dictionary
student["city"] = "New York"
print(student)

# Exercise 5.10: Word counter
text = "hello world hello python world"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'hello': 2, 'world': 2, 'python': 1}

# Exercise 5.11: Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Exercise 5.12: Tuple unpacking
coords = (10, 20, 30)
x, y, z = coords
print(f"x={x}, y={y}, z={z}")

# Exercise 5.13: Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Exercise 5.14: Nested data structures
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]
print(students)

# Exercise 5.15: Sort list of dictionaries
students_sorted = sorted(students, key=lambda x: x["age"])
print(students_sorted)

# Exercise 5.16: Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)  # [3, 4]

# Exercise 5.17: Group by
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
grouped = {"even": [], "odd": []}
for num in numbers:
    if num % 2 == 0:
        grouped["even"].append(num)
    else:
        grouped["odd"].append(num)
print(grouped)

# Exercise 5.18: Frequency counter
text = "hello world"
frequency = {}
for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1
print(frequency)
