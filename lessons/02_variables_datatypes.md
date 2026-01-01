# Lesson 2: Variables and Data Types

## Variables
Variables are containers for storing data values. In Python, you don't need to declare variable types explicitly.

### Variable Assignment
```python
# Numbers
age = 25
height = 5.9

# Strings
name = "Alice"
message = 'Hello, World!'

# Boolean
is_student = True
has_graduated = False
```

### Variable Naming Rules
- Variable names must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Are case-sensitive (`age` and `Age` are different)
- Cannot use Python keywords (like `if`, `for`, `while`)

```python
# Good variable names
user_name = "Bob"
age_2023 = 30
_private_var = 100

# Bad variable names (will cause errors)
# 2nd_name = "Invalid"
# my-name = "Invalid"
# class = "Invalid"  # 'class' is a keyword
```

## Data Types

### Numbers
```python
# Integer
count = 10
negative_num = -5

# Float
price = 19.99
temperature = -3.5

# Arithmetic operations
sum_result = 10 + 5      # Addition: 15
difference = 10 - 5      # Subtraction: 5
product = 10 * 5         # Multiplication: 50
quotient = 10 / 5        # Division: 2.0
floor_div = 10 // 3      # Floor division: 3
modulus = 10 % 3         # Modulus: 1
power = 2 ** 3           # Exponentiation: 8
```

### Strings
```python
# String creation
first_name = "John"
last_name = 'Doe'
full_name = first_name + " " + last_name  # Concatenation

# String methods
text = "Hello World"
print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.replace("World", "Python"))  # "Hello Python"
print(len(text))         # 11

# String indexing and slicing
message = "Python"
print(message[0])        # 'P' - first character
print(message[-1])       # 'n' - last character
print(message[0:3])      # 'Pyt' - slice from 0 to 3
print(message[2:])       # 'thon' - slice from 2 to end
```

### Booleans
```python
is_active = True
is_logged_in = False

# Comparison operators return booleans
print(5 > 3)             # True
print(10 == 10)          # True
print(7 != 7)            # False
print(3 <= 5)            # True
```

### Type Conversion
```python
# Convert between types
num_str = "42"
num_int = int(num_str)        # String to integer
num_float = float(num_str)    # String to float

age = 25
age_str = str(age)            # Integer to string

# Check type
print(type(42))               # <class 'int'>
print(type(3.14))             # <class 'float'>
print(type("Hello"))          # <class 'str'>
print(type(True))             # <class 'bool'>
```

## Practice Exercise
1. Create variables to store your name, age, and favorite number
2. Calculate the area of a rectangle (length * width)
3. Combine first name and last name with a space between them
4. Convert a string "100" to an integer and add 50 to it

Next: [Lesson 3: Control Flow](03_control_flow.md)
