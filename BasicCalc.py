# Function to perform the operation
#def calculate(num1, num2, operation):

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the Second number:"))
operation = input("Enter a mathematical operation(+, *, -, /): ")

if operation == "+":
    results = num1 + num2
elif operation == "-":
    results = num1 - num2
elif operation == "-":
    results = num1 - num2
elif operation == "*":
    results = num1 * num2
elif operation == "/":
    results = num1 / num2
    if num2 != 0:
        results = num1 / num2
    else:
        results = "Error! Division by zero."
else:
    results = "Invalid operation!"

print("Results:", results)



   
