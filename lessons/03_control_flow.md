# Lesson 3: Control Flow

## Conditional Statements (if/elif/else)

### Basic if Statement
```python
age = 18

if age >= 18:
    print("You are an adult")
```

### if-else Statement
```python
temperature = 25

if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")
```

### if-elif-else Statement
```python
score = 85

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
```

### Logical Operators
```python
age = 25
has_license = True

# AND operator
if age >= 18 and has_license:
    print("You can drive")

# OR operator
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("You can relax!")

# NOT operator
is_raining = False

if not is_raining:
    print("You don't need an umbrella")
```

## Loops

### for Loop
Use for loops to iterate over a sequence (like a range, list, or string):

```python
# Loop through a range
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop through a range with start and end
for i in range(1, 6):
    print(i)  # Prints 1, 2, 3, 4, 5

# Loop through a range with step
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8

# Loop through a string
for letter in "Python":
    print(letter)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### while Loop
Use while loops to repeat code as long as a condition is true:

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count

# While loop with user input
password = ""
while password != "secret":
    password = input("Enter password: ")

print("Access granted!")
```

### Loop Control Statements

#### break - Exit the loop
```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)  # Prints 0, 1, 2, 3, 4
```

#### continue - Skip current iteration
```python
for i in range(6):
    if i == 3:
        continue  # Skip when i is 3
    print(i)  # Prints 0, 1, 2, 4, 5
```

### Nested Loops
```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Empty line after each row
```

## Practice Exercises
1. Write a program that checks if a number is positive, negative, or zero
2. Create a program that prints all even numbers from 1 to 20
3. Write a program that calculates the sum of numbers from 1 to 100
4. Create a program that prints a simple pattern using nested loops:
   ```
   *
   **
   ***
   ****
   *****
   ```
5. Write a program that asks the user to guess a number (1-10) and keeps asking until they guess correctly

Next: [Lesson 4: Functions](04_functions.md)
