"""
Solutions for Exercise 2: Variables and Data Types
===================================================
"""

# Exercise 2.1: Variable assignment
name = "Alice"
age = 25
height = 1.75
is_student = True

# Exercise 2.2: Arithmetic operations
length = 15
width = 8
area = length * width
print(f"Area of rectangle: {area}")

# Exercise 2.3: String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Exercise 2.4: String methods
text = "python programming"
uppercase_text = text.upper()
print(uppercase_text)

# Exercise 2.5: Type conversion
number_string = "42"
number = int(number_string)
result = number + 58
print(result)  # 100

# Exercise 2.6: String slicing
text = "Hello World"
first_five = text[:5]
print(first_five)  # "Hello"

# Exercise 2.7: Calculate BMI
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

# Exercise 2.8: Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Exercise 2.9: String formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# Exercise 2.10: Check data types
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
