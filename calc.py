print("Welcome to My Calculator!")

def calculate():
    """A simple Python program that acts as a calculator.
    It prompts the user for two numbers and an operation, then performs the calculation and prints the result. """

    # Get the first number from the user
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str)

    # Get the second number from the user
    num2_str = input("Enter the second number: ")
    num2 = float(num2_str)

    # Get the operation from the user
    operation = input("Enter the operation (+, -, *, /): ").strip()

    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

calculate()