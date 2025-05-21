import time, sys
import random
from ascii_magic import AsciiArt
from PIL import Image as PILImage

try:
    img = PILImage.open("/workspaces/Computer-Programming-2/download.jpg")
    ascii_art = AsciiArt.from_pillow_image(img)
    ascii_art.to_terminal()
except FileNotFoundError:
    print("Image file not found. Skipping ASCII art.")

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def falling_tree_animation():
    print("🌳 CRASH!")
    try:
        img = PILImage.open("/workspaces/Computer-Programming-2/download.jpg")
        ascii_art = AsciiArt.from_pillow_image(img)
        ascii_art.to_terminal()
    except FileNotFoundError:
        print("Tree image not found. Imagine a tree falling!")
    time.sleep(0.5)

class Weapon:
    def __init__(self, name, ammo, damage_per_bullet, accuracy):
        self.name = name
        self.ammo = ammo
        self.damage_per_bullet = damage_per_bullet
        self.accuracy = accuracy

    def shoot(self, player, animal):
        print(f"Attempting to shoot the {animal['name']} with {self.name}...")
        if self.ammo <= 0:
            print(f"Out of ammo for {self.name}! Visit the shop to buy more.")
            return False
        self.ammo -= 1
        player['weapon_ammo'] = self.ammo
        print(f"Aiming at the {animal['name']}...")
        time.sleep(1)
        if random.randint(1, 100) <= self.accuracy:
            damage = self.damage_per_bullet
            print(f"You hit the {animal['name']} for {damage} damage!")
            return animal_take_damage(animal, damage)
        else:
            print(f"You missed the {animal['name']}!")
            print("\nTree falls with each shot...")
            falling_tree_animation()
            return False

    def description(self):
        return f"Weapon: {self.name}, Ammo: {self.ammo}, Damage: {self.damage_per_bullet}, Accuracy: {self.accuracy}%"

class Pistol(Weapon):
    def __init__(self, ammo=24):
        super().__init__(name="Pistol", ammo=ammo, damage_per_bullet=25, accuracy=80)

class M60(Weapon):
    def __init__(self, ammo=300):
        super().__init__(name="M60", ammo=ammo, damage_per_bullet=150, accuracy=35)
        self.bullets_per_shot = 20

    def shoot(self, player, animal):
        print(f"Firing the {self.name}...")
        if self.ammo < self.bullets_per_shot:
            print("Not enough ammo for a full burst! Visit the shop to buy more.")
            return False
        self.ammo -= self.bullets_per_shot
        player['weapon_ammo'] = self.ammo
        time.sleep(1)
        total_damage = 0
        for _ in range(self.bullets_per_shot):
            if random.randint(1, 100) <= self.accuracy:
                total_damage += self.damage_per_bullet
        print(f"You hit the {animal['name']} for {total_damage} total damage with the {self.name}!")
        return animal_take_damage(animal, total_damage)

class SemiAutoRifle(Weapon):
    def __init__(self, ammo=100):
        super().__init__(name="Semi-Auto Rifle", ammo=ammo, damage_per_bullet=70, accuracy=70)

    def shoot(self, player, animal):
        print(f"Firing the {self.name}... BANG!")
        if self.ammo <= 0:
            print(f"Out of ammo for {self.name}! Visit the shop to buy more.")
            return False
        self.ammo -= 20
        player['weapon_ammo'] = self.ammo
        time.sleep(1)
        if random.randint(1, 100) <= self.accuracy:
            total_damage = self.damage_per_bullet
            print(f"You hit the {animal['name']} for {total_damage} damage with the {self.name}!")
            return animal_take_damage(animal, total_damage)
        else:
            print("You missed!")
            print("\nTree falls with each shot...")
            falling_tree_animation()
            return False

class RPG(Weapon):
    def __init__(self, ammo=5):
        super().__init__(name="RPG", ammo=ammo, damage_per_bullet=1000, accuracy=85)

    def shoot(self, player, animal):
        print(f"Firing the {self.name}... BOOM!")
        if self.ammo <= 0:
            print(f"Out of ammo for {self.name}! Visit the shop to buy more.")
            return False
        self.ammo -= 1
        player['weapon_ammo'] = self.ammo
        time.sleep(1)
        if random.randint(1, 100) <= self.accuracy:
            total_damage = self.damage_per_bullet
            print(f"You hit the {animal['name']} for {total_damage} damage with the {self.name}!")
            return animal_take_damage(animal, total_damage)
        else:
            print("You missed!")
            print("\nTree falls with each shot...")
            falling_tree_animation()
            return False

class HuntingRifle(Weapon):
    def __init__(self, ammo=25):
        super().__init__(name="Hunting Rifle", ammo=ammo, damage_per_bullet=150, accuracy=97)

    def shoot(self, player, animal):
        print(f"Firing the {self.name}... CRACK!")
        if self.ammo <= 0:
            print(f"Out of ammo for {self.name}! Visit the shop to buy more.")
            return False
        self.ammo -= 1
        player['weapon_ammo'] = self.ammo
        time.sleep(1)
        if random.randint(1, 100) <= self.accuracy:
            total_damage = self.damage_per_bullet
            print(f"You hit the {animal['name']} for {total_damage} damage with the {self.name}!")
            return animal_take_damage(animal, total_damage)
        else:
            print("You missed!")
            print("\nTree falls with each shot...")
            falling_tree_animation()
            return False

def create_player():
    return {
        'health': 100,
        'ammo': 10,
        'inventory': {'food': 5},
        'money': 250,
        'alive': True,
        'weapon': Pistol(),
        'weapon_ammo': 24,
        'money_found': 500,
        'kills': 0
    }

def create_animal(name, tier, money_reward, health, damage):
    return {
        'name': name,
        'tier': tier,
        'money_reward': money_reward,
        'health': health,
        'attack_damage': damage
    }

def take_damage(player, amount):
    player['health'] -= amount
    if player['health'] <= 0:
        player['health'] = 0
        player['alive'] = False

def heal(player):
    if 'food' in player['inventory'] and player['inventory']['food'] > 0:
        player['health'] += 30
        player['inventory']['food'] -= 1
        print("You ate food and healed 30 health!")
    else:
        print("You don't have any food!")

def buy_item(player, item, cost):
    if player['money'] >= cost:
        player['money'] -= cost
        if item == 'ammo':
            player['weapon'].ammo += 5
            player['weapon_ammo'] = player['weapon'].ammo
        elif item == 'food':
            player['inventory']['food'] += 1
        elif item == 'm60':
            player['weapon'] = M60(ammo=500)
            player['weapon_ammo'] = player['weapon'].ammo
            print("You bought the M60 machine gun!")
        elif item == 'rpg':
            player['weapon'] = RPG(ammo=5)
            player['weapon_ammo'] = player['weapon'].ammo
            print("You bought the RPG!")
        elif item == 'semi_auto_rifle':
            player['weapon'] = SemiAutoRifle(ammo=100)
            player['weapon_ammo'] = player['weapon'].ammo
            print("You bought the Semi-Auto Rifle with 100 rounds!")
        elif item == 'hunting_rifle':
            player['weapon'] = HuntingRifle(ammo=25)
            player['weapon_ammo'] = player['weapon'].ammo
            print("You bought the Hunting Rifle with 25 rounds!")
        print(f"Purchased {item} for {cost} money.")
    else:
        print("Not enough money!")

def is_alive(player):
    return player['alive']

def animal_take_damage(animal, amount):
    animal['health'] -= amount
    if animal['health'] <= 0:
        animal['health'] = 0
        return True
    return False

def animal_attack(animal):
    return animal['attack_damage']

def shoot(player, animal):
    return player['weapon'].shoot(player, animal)

def bear_turn(player, animal):
    print(f"The {animal['name']} attacks!")
    damage = animal_attack(animal)
    take_damage(player, damage)
    print(f"The {animal['name']} dealt {damage} damage to you.")

def show_status(player):
    print(f"\nPlayer Health: {player['health']} | Ammo: {player['weapon_ammo']} | Money: {player['money']}")
    print(f"Food: {player['inventory'].get('food', 0)} | Weapon: {player['weapon'].name} ({player['weapon_ammo']} ammo)")

def shop(player):
    print("\nWelcome to the Shop!")
    print("1. Buy Ammo (5 bullets) - 20 money")
    print("2. Buy Food (heals 30 health) - 15 money")
    print("3. Buy M60 Machine Gun (500 ammo) - 650 money")

    print("4. Buy RPG (5 ammo) - 500 money")
    print("5. Buy Semi-Auto Rifle (100 ammo) - 400 money")
    print("6. Buy Hunting Rifle (25 ammo) - 250 money")
    print("9. Exit Shop")
    choice = input("Choose an option: ")
    if choice == "1":
        buy_item(player, 'ammo', 20)
    elif choice == "2":
        buy_item(player, 'food', 15)
    elif choice == "3":
        buy_item(player, 'm60', 650)
    elif choice == "4":
        buy_item(player, 'rpg', 500)
    elif choice == "5":
        buy_item(player, 'semi_auto_rifle', 400)
    elif choice == "6":
        buy_item(player, 'hunting_rifle', 250)
    elif choice == "9":
        print("Exiting the shop.")
        return
    else:
        print("Invalid choice. Try again.")
    time.sleep(1)

def encounter_animal(player):
    animals = [
        create_animal('Deer', 'Tier 1', 10, 30, 5),
        create_animal('Deer', 'Tier 1', 10, 30, 5),
        create_animal('Deer', 'Tier 1', 10, 30, 5),
        create_animal('Deer', 'Tier 1', 10, 30, 5),
        create_animal('Raccoon', 'Tier 1', 15, 20, 4),
        create_animal('Coyote', 'Tier 2', 25, 40, 7),
        create_animal('Polar Bear', 'Tier 3', 250, 250, 30),
        create_animal('Honey Badger', 'Tier 3', 200, 80, 25),
        create_animal('Bear', 'Tier 3', 100, 125, 20),
        create_animal('Moose', 'Tier 3', 60, 70, 15),
        create_animal('Dragon', 'Tier 5', 500, 1000, 40),
        create_animal('Gigantopithecus', 'Tier 4', 200, 200, 25),
        create_animal('Bird', 'Tier 1', 5, 10, 2)
    ]
    animal = random.choice(animals)
    print(f"\nA wild {animal['name']} appears!")
    return animal

def game_loop():
    try:
        img = PILImage.open("/workspaces/Computer-Programming-2/Hunting_Game_Cover.png")
        ascii_art = AsciiArt.from_pillow_image(img)
        ascii_art.to_terminal()
        print("Welcome to Wilderness Hunt Game!")
    except FileNotFoundError:
        print("Welcome image not found. Starting the game...")
    print("Game loop is running...")
    player = create_player()
    print("You find a Semi-Auto Rifle with 100 rounds of ammo. Do you want to pick it up?")
    choice = input("Enter 'yes' to pick up the Semi-Auto Rifle or 'no' to leave it: ").lower()
    if choice == 'yes':
        player['weapon'] = SemiAutoRifle(ammo=100)
        player['weapon_ammo'] = player['weapon'].ammo
        print("You have picked up the Semi-Auto Rifle.")
    while is_alive(player):
        show_status(player)
        print("\nWalking through the forest...")
        time.sleep(2)
        print("Trees slowly sway as you walk through the forest...")
        print("You encounter an animal!")
        animal = encounter_animal(player)
        time.sleep(1)
        while animal['health'] > 0 and is_alive(player):
            show_status(player)
            print(f"\nAnimal: {animal['name']} | Health: {animal['health']}")
            shoot(player, animal)
            if animal['health'] > 0:
                bear_turn(player, animal)
        if animal['health'] <= 0:
            print(f"You defeated the {animal['name']}!")
            player['money'] += animal['money_reward']
            print(f"You earned {animal['money_reward']} money!")
            print(f"Current Money: {player['money']}")
            player['kills'] += 1
        if not is_alive(player):
            break
        print("\nWould you like to visit the shop? (yes/no)")
        buy_choice = input().lower()
        if buy_choice == 'yes':
            shop(player)
        
        print("\nWould you like to eat 1 food (heal)? (yes/no)")
        heal_choice = input().lower()
        if heal_choice == 'yes':
            heal(player)
        
        print("Do you want to leave the forest? (yes/no)")
        leave_choice = input().lower()
        if leave_choice == 'yes':
            print("You safely leave the forest.")
            break
    if not is_alive(player):
        print("Game Over! You died.")
    else:
        print("Game Over! You survived the hunt.")

game_loop()