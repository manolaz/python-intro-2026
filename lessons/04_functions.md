# Lesson 4: Functions

## What are Functions?
Functions are reusable blocks of code that perform a specific task. They help organize code and avoid repetition.

## Defining Functions

### Basic Function
```python
def greet():
    print("Hello!")
    print("Welcome to Python!")

# Call the function
greet()
```

### Functions with Parameters
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!
```

### Functions with Multiple Parameters
```python
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)      # Output: 5 + 3 = 8
add_numbers(10, 20)    # Output: 10 + 20 = 30
```

## Return Values
Functions can return values using the `return` keyword:

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20

# Use directly in expressions
total = multiply(3, 7) + 10
print(total)  # Output: 31
```

### Multiple Return Values
```python
def get_user_info():
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city

# Unpack returned values
user_name, user_age, user_city = get_user_info()
print(f"{user_name} is {user_age} years old and lives in {user_city}")
```

## Default Parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Output: Hello, Alice!
greet("Bob", "Hi")          # Output: Hi, Bob!
greet("Charlie", "Hey")     # Output: Hey, Charlie!
```

## Keyword Arguments
```python
def display_info(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Call with keyword arguments (order doesn't matter)
display_info(age=30, name="Alice", city="Boston")
```

## Variable Scope

### Local Variables
```python
def my_function():
    local_var = 10  # Only exists inside the function
    print(local_var)

my_function()
# print(local_var)  # This would cause an error
```

### Global Variables
```python
global_var = 100  # Available everywhere

def show_global():
    print(global_var)  # Can read global variable

show_global()  # Output: 100
```

## Lambda Functions (Anonymous Functions)
Short, one-line functions:

```python
# Regular function
def square(x):
    return x * x

# Lambda function
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7
```

## Built-in Functions
Python provides many useful built-in functions:

```python
# Math functions
print(abs(-10))        # Absolute value: 10
print(max(5, 10, 3))   # Maximum: 10
print(min(5, 10, 3))   # Minimum: 3
print(pow(2, 3))       # Power: 8
print(round(3.7))      # Round: 4

# String/List functions
numbers = [1, 2, 3, 4, 5]
print(len(numbers))    # Length: 5
print(sum(numbers))    # Sum: 15

# Type conversion
print(int("42"))       # String to int
print(str(42))         # Int to string
print(list("hello"))   # String to list
```

## Practice Exercises
1. Write a function that takes a name and returns a greeting message
2. Create a function that calculates the area of a rectangle (length × width)
3. Write a function that checks if a number is even or odd and returns True/False
4. Create a function that takes a list of numbers and returns their average
5. Write a function that converts temperature from Celsius to Fahrenheit
   Formula: F = (C × 9/5) + 32
6. Create a function that takes a string and returns it reversed

Next: [Lesson 5: Data Structures](05_data_structures.md)
