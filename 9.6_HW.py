# Base class
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

# Subclass
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine="Ice Cream"):
        super().__init__(name, cuisine)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"]

    def display_flavors(self):
        print(f"{self.name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"{flavor}")

# Create an instance and call method
my_ice_cream_stand = IceCreamStand("Sweet Treats")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()
