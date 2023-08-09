#!/usr/bin/env python3

# define the basic calculation functions
def add(a, b):
    result = a + b
    equation = f"{a} + {b} = {result}"
    print(equation)

def subtract(a, b):
    result = a - b
    equation = f"{a} - {b} = {result}"
    print(equation)

def multiply(a, b):
    result = a * b
    equation = f"{a} * {b} = {result}"
    print(equation)

def divide(a, b):
    result = a / b
    equation = f"{a} / {b} = {result}"
    print(equation)

# entry point of the program
def main():
    print("Welcome! This program enables you to do basic calculations.")

    while True:
        print("\nOptions:")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")

        choice = input("Enter your choice: ").lower()
        
        if choice == 'a':
            print('Addition')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            add(a, b)

        elif choice == 'b':
            print('Subtraction')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            subtract(a, b)

        elif choice == 'c':
            print('Multiplication')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            multiply(a, b)

        elif choice == 'd':
            print('Division')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            divide(a, b)

        elif choice == 'e':
            print('Program ended. Bye!!!')
            break

if __name__ == "__main__":
    main()
