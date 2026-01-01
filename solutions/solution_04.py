"""
Solutions for Exercise 4: Functions
====================================
"""

# Exercise 4.1: Simple greeting function
def greet():
    print("Hello, World!")

greet()

# Exercise 4.2: Personalized greeting
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Exercise 4.3: Add two numbers
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# Exercise 4.4: Calculate area of rectangle
def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)
print(f"Area: {area}")

# Exercise 4.5: Check even or odd
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# Exercise 4.6: Find maximum
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 25, 15))

# Exercise 4.7: Temperature conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_f = celsius_to_fahrenheit(25)
print(f"25°C = {temp_f}°F")

# Exercise 4.8: Calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120

# Exercise 4.9: Reverse a string
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))  # "olleh"

# Exercise 4.10: Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  # 3

# Exercise 4.11: Check palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# Exercise 4.12: Calculate average
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

avg = calculate_average([10, 20, 30, 40])
print(f"Average: {avg}")

# Exercise 4.13: Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# Exercise 4.14: Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

# Exercise 4.15: Lambda function
square = lambda x: x ** 2
print(square(5))  # 25
