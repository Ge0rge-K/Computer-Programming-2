
print("Enter 'quit' to stop.")

while True:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")
    print(f"Welcome, {name}!")
