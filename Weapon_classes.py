class weapon:
    # Class attribute

    # Instance attributes
    def __init__(weapon, name, ammo, damage, ):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return "Woof!"

    # Another instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Creating instances (objects) of the Dog class
buddy = Dog("Buddy", 3)
miles = Dog("Miles", 5)

# Accessing attributes and methods
print(f"{buddy.name}'s species is {buddy.species}") # Output: Buddy's species is Canis familiaris
print(miles.description()) # Output: Miles is 5 years old
print(buddy.bark()) # Output: Woof!