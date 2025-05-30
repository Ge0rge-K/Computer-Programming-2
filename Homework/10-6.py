
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    result = int(num1) + int(num2)
    print(f"The sum is: {result}")

except ValueError:
    print("Oops! Please enter only numbers.")
