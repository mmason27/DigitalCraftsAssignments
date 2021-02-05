# File path: Desktop/DigitalCrafts/Week-1/Python
# Assignment 1 - Calculator

first_number = float(input("Please enter a number: "))
operand = input("Please enter an operand: ")
second_number = float(input("Please enter another number: "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

if operand == "+":
    print(add(first_number, second_number))
elif operand == "-":
    print(subtract(first_number, second_number))
elif operand == "*":
    print(multiply(first_number, second_number))
elif operand == "/":
    print(divide(first_number, second_number))
else:
    print("Sorry, that is not a valid input.")


# Assignment 2 - Even or Odd

number = int(input("Enter a number to see if it's even or odd: "))
if number % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")

# Assignment 3 - Write a Fizz Buzz Application

user_input = int(input("Enter a number: "))

if user_input % 3 == 0 and user_input % 5 == 0:
    print("Fizz Buzz")
elif user_input % 5 == 0:
    print("Buzz")
elif user_input % 3 == 0:
    print("Fizz")
else:
    print("This is a fizz buzzst! This number is not divisible by 3 or 5.")




        
