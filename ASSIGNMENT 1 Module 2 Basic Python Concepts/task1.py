# Take two numbers as input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# Division with zero check
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")
