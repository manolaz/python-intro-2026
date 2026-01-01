# Python Quick Reference Guide

A handy reference for Python syntax and common operations.

## Basic Syntax

### Print Output
```python
print("Hello")
print("Value:", 42)
print(f"Name: {name}")
```

### Comments
```python
# Single line comment
"""Multi-line comment"""
```

## Variables and Data Types

### Numbers
```python
integer = 42
floating = 3.14
result = 10 + 5 - 2 * 3 / 4
power = 2 ** 3  # 8
```

### Strings
```python
text = "Hello"
text.upper()      # HELLO
text.lower()      # hello
text[0]          # H
text[:3]         # Hel
len(text)        # 5
```

### Type Conversion
```python
int("42")        # String to int
str(42)          # Int to string
float("3.14")    # String to float
```

## Control Flow

### If Statements
```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code
```

### For Loops
```python
for i in range(5):          # 0 to 4
    print(i)

for item in list:
    print(item)
```

### While Loops
```python
while condition:
    # code
```

## Functions

### Basic Function
```python
def function_name(param1, param2):
    result = param1 + param2
    return result
```

### Default Parameters
```python
def greet(name="World"):
    return f"Hello, {name}!"
```

### Lambda Functions
```python
square = lambda x: x ** 2
add = lambda a, b: a + b
```

## Lists

### Creation and Access
```python
my_list = [1, 2, 3, 4, 5]
my_list[0]       # First: 1
my_list[-1]      # Last: 5
my_list[1:3]     # Slice: [2, 3]
```

### Modification
```python
my_list.append(6)           # Add to end
my_list.insert(0, 0)        # Insert at index
my_list.remove(3)           # Remove by value
my_list.pop()               # Remove last
my_list.sort()              # Sort in place
```

### List Comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

## Dictionaries

### Creation and Access
```python
person = {"name": "Alice", "age": 25}
person["name"]              # Access by key
person.get("city", "NYC")   # With default
```

### Modification
```python
person["age"] = 26          # Update
person["city"] = "Boston"   # Add new
del person["age"]           # Remove
```

### Iteration
```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

## Tuples
```python
coords = (10, 20)
x, y = coords               # Unpacking
```

## Sets
```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
set1 | set2                 # Union
set1 & set2                 # Intersection
```

## File Operations

### Reading
```python
with open("file.txt", "r") as f:
    content = f.read()
    # or
    lines = f.readlines()
    # or
    for line in f:
        print(line)
```

### Writing
```python
with open("file.txt", "w") as f:
    f.write("text\n")
```

### JSON
```python
import json

# Read
with open("data.json", "r") as f:
    data = json.load(f)

# Write
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### CSV
```python
import csv

# Read
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Write
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", "25"])
```

## Common Built-in Functions

```python
len(collection)             # Length
max(1, 2, 3)               # Maximum
min(1, 2, 3)               # Minimum
sum([1, 2, 3])             # Sum
range(5)                   # 0 to 4
sorted([3, 1, 2])          # Returns sorted list
enumerate(list)            # Index and value
zip(list1, list2)          # Combine lists
```

## String Formatting

```python
# f-strings (recommended)
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")

# format()
print("Name: {}, Age: {}".format(name, age))

# % formatting (old style)
print("Name: %s, Age: %d" % (name, age))
```

## Exception Handling

```python
try:
    # code that might fail
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always runs")
```

## Useful String Methods

```python
text.strip()               # Remove whitespace
text.split()               # Split into list
text.replace("a", "b")     # Replace
text.startswith("Hi")      # Check start
text.endswith(".txt")      # Check end
text.isdigit()             # Check if all digits
text.isalpha()             # Check if all letters
```

## Useful List Methods

```python
list.count(item)           # Count occurrences
list.index(item)           # Find index
list.reverse()             # Reverse in place
list.clear()               # Remove all
list.copy()                # Shallow copy
list.extend([4, 5])        # Add multiple items
```

## Boolean Logic

```python
True and False             # False
True or False              # True
not True                   # False
5 > 3                      # True
10 == 10                   # True
5 != 5                     # False
```

## Common Operators

```python
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division
//  # Floor division
%   # Modulus (remainder)
**  # Exponentiation
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater or equal
<=  # Less or equal
```

---

Keep this guide handy while coding!
