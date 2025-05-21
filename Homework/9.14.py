import random

# List of 10 numbers and 5 letters
lottery_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 unique items
winning_ticket = random.sample(lottery_elements, 4)
print("The winning ticket is:", winning_ticket)

# Fixed Ticket
my_ticket = [3, 'A', 7, 'C']

attempts = 0
won = False

while not won:
    attempts += 1
    drawn_ticket = random.sample(lottery_elements, 4)
    
    if sorted(drawn_ticket, key=lambda x: (str(type(x)), x)) == sorted(my_ticket, key=lambda x: (str(type(x)), x)):
        won = True
        print(f"You won after {attempts} attempts! Your ticket: {my_ticket}")
