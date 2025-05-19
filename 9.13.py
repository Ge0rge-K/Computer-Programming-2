import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# 6-sided die
die6 = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(die6.roll_die(), end=' ')
print("\n")

# 10-sided die
die10 = Die(10)
print("Rolling a 10-sided die 10 times:")
for _ in range(10):
    print(die10.roll_die(), end=' ')
print("\n")

# 20-sided die
die20 = Die(20)
print("Rolling a 20-sided die 10 times:")
for _ in range(10):
    print(die20.roll_die(), end=' ')
print("\n")
