# Lesson 5: Data Structures

## Lists
Lists are ordered, mutable collections that can store multiple items.

### Creating Lists
```python
# Empty list
empty_list = []

# List with items
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Lists can contain different types
```

### Accessing List Elements
```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])      # First element: apple
print(fruits[1])      # Second element: banana
print(fruits[-1])     # Last element: date
print(fruits[-2])     # Second to last: cherry
```

### List Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])   # [2, 3, 4]
print(numbers[:3])    # [0, 1, 2] - from start to index 3
print(numbers[5:])    # [5, 6, 7, 8, 9] - from index 5 to end
print(numbers[::2])   # [0, 2, 4, 6, 8] - every 2nd element
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reversed
```

### Modifying Lists
```python
fruits = ["apple", "banana", "cherry"]

# Add elements
fruits.append("date")           # Add at end
fruits.insert(1, "blueberry")   # Insert at index 1
fruits.extend(["elderberry", "fig"])  # Add multiple items

# Remove elements
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last item
popped_index = fruits.pop(0)    # Remove and return item at index 0
del fruits[1]                   # Delete by index

# Modify elements
fruits[0] = "apricot"           # Change first element
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sorting
numbers.sort()                  # Sort in place
sorted_nums = sorted(numbers)   # Return new sorted list

# Reversing
numbers.reverse()               # Reverse in place
reversed_nums = numbers[::-1]   # Return new reversed list

# Other useful methods
print(numbers.count(1))         # Count occurrences of 1
print(numbers.index(4))         # Find index of first 4
numbers.clear()                 # Remove all elements
```

### List Comprehension
A concise way to create lists:

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(10)]

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

## Tuples
Tuples are ordered, immutable collections.

```python
# Creating tuples
point = (3, 4)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single-item tuple

# Accessing elements
print(colors[0])      # red
print(colors[-1])     # blue

# Tuples are immutable
# colors[0] = "yellow"  # This would cause an error

# Tuple unpacking
x, y = point
print(f"x: {x}, y: {y}")  # x: 3, y: 4

# Multiple return values are tuples
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
```

## Dictionaries
Dictionaries store key-value pairs.

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}

# Dictionary with items
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Dictionary with different value types
student = {
    "name": "Bob",
    "grades": [85, 90, 92],
    "is_enrolled": True
}
```

### Accessing Dictionary Values
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

print(person["name"])           # Alice
print(person.get("age"))        # 25
print(person.get("country", "USA"))  # USA (default if key doesn't exist)
```

### Modifying Dictionaries
```python
person = {"name": "Alice", "age": 25}

# Add or update
person["city"] = "New York"     # Add new key-value
person["age"] = 26              # Update existing value
person.update({"country": "USA", "job": "Engineer"})

# Remove
del person["age"]               # Remove by key
popped = person.pop("city")     # Remove and return value
person.clear()                  # Remove all items
```

### Dictionary Methods
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Get all keys, values, or items
print(person.keys())            # dict_keys(['name', 'age', 'city'])
print(person.values())          # dict_values(['Alice', 25, 'New York'])
print(person.items())           # dict_items([('name', 'Alice'), ...])

# Loop through dictionary
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehension
```python
# Create dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
# Result: {'a': 1, 'b': 2, 'c': 3}

# Squares dictionary
squares = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Sets
Sets are unordered collections of unique elements.

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates an empty dict, not set

# Add and remove
fruits.add("date")
fruits.remove("banana")       # Raises error if not found
fruits.discard("elderberry")  # No error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)   # Union: {1, 2, 3, 4, 5, 6}
print(set1 & set2)   # Intersection: {3, 4}
print(set1 - set2)   # Difference: {1, 2}
print(set1 ^ set2)   # Symmetric difference: {1, 2, 5, 6}
```

## Practice Exercises
1. Create a list of your 5 favorite movies and print the third one
2. Write a program that removes duplicates from a list
3. Create a dictionary to store student information (name, age, grades)
4. Write a program that counts how many times each word appears in a sentence
5. Create a function that takes a list of numbers and returns a new list with only the even numbers
6. Write a program that merges two dictionaries

Next: [Lesson 6: File Operations](06_file_operations.md)
