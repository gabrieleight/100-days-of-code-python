"""
Basic Input and Output:
Write a program that reads a single input from the user and prints it to the console. For example, if the user enters their name, the program should output: ""Hello, {name}""

Handling Different Data Types:
Extend the program to read and print different types of inputs. Ensure the inputs are properly converted to their respective types and then printed. The program should ask the user to enter:    
"""

# Solution
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = bool(input("Are you a student? "))
print()
print(f"Hello, {name}")
print(f"Your age is {age}!")
print(f"Your height is {height}")
print(f"Are you a student? {is_student}")