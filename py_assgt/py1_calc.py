# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation based on operation
result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed!")
        exit()
else:
    print("Error: Invalid operation entered!")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")