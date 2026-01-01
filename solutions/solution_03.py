"""
Solutions for Exercise 3: Control Flow
=======================================
"""

# Exercise 3.1: Check if number is positive
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 3.2: Grade calculator
score = int(input("Enter score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Exercise 3.3: Even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 3.4: Largest of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
largest = max(a, b, c)
print(f"Largest: {largest}")

# Exercise 3.5: Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# Exercise 3.6: Print even numbers
for i in range(2, 21, 2):
    print(i)

# Exercise 3.7: Sum of numbers
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")

# Exercise 3.8: Multiplication table
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Exercise 3.9: Countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Exercise 3.10: Find numbers
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Exercise 3.11: Pattern printing
for i in range(1, 6):
    print("*" * i)

# Exercise 3.12: Number guessing game
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess a number (1-10): "))
    if guess != secret:
        print("Try again!")
print("Correct!")

# Exercise 3.13: FizzBuzz
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
