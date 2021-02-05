# # Factorial

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,number + 1):
        factorial = factorial * i
print(f"The factorial of {number} is {factorial}")



# # Palindrome - create an app which detects if the input word is a palindrome or not

def is_palindrome():
    word = input("Enter a word to determine if it is a palindrome: ")
    if word == word[::-1]:
        print("Awesome! This is a palindrome")
    else:
        print("Not a palindrome")

is_palindrome()

#go back and rework through this code to do it with a for loop

# Prime or Not

def is_prime():
    number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number,"is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    
is_prime()








