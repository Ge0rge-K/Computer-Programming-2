
print("Enter two numbers to add. Type 'q' to quit.")

while True:
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
    else:
        print(f"The sum is: {result}\n")
