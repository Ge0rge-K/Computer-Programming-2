class Human:
    def __init__(self, name, sleep, eating, drinking):
        self.name = name
        self.is_asleep = sleep
        self.is_eating = eating
        self.is_drinking = drinking
    
    def eat(self):
        print(f"{self.name} is eating...")


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating... ")
    
    def sleep(self):
        print(f"{self.name} is not sleeping...")

class Dog(Animal):
        def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is not eating... ")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")

class Cat(Animal):
        def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating... ")
    
    def sleep(self):
        print(f"{self.name} is not asleep...")

class Hampster(Animal):
        def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is not eating... ")
    
    def sleep(self):
        print(f"{self.name} is Awake...")

dog = Dog("Lula")
cat = Cat("Scoobert")
hampster = Hampster("Pine Cone")

print(dog.name)
print(dog.is_alive)