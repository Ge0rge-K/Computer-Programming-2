import time, sys

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


from ascii_magic import AsciiArt
from PIL import Image

Image = Image.open("/workspaces/Computer-Programming-2/download.jpg")

ascii_art = AsciiArt.from_pillow_image(Image)
ascii_art.to_terminal()

#Blurb /workspaces/Computer-Programming-2/image copy.png
#Zoe /workspaces/Computer-Programming-2/image.png
# Bobidilo /workspaces/Computer-Programming-2/image copy 2.png

import random
import time

# Player attributes stored in a dictionary
def create_player():
    return {
        'health': 100,
        'ammo': 10,
        'inventory': {'food': 2},
        'money': 50,
        'alive': True,
        'weapon': 'pistol',
        'weapon_ammo': 5,
        'money_found': 500,
        'kills': 0
    }

# Animal attributes stored in a dictionary
def create_animal(name, tier, money_reward, health, damage):
    return {
        'name': name,
        'tier': tier,
        'money_reward': money_reward,
        'health': health,
        'attack_damage': damage
    }

# Function to handle taking damage
def take_damage(player, amount):
    player['health'] -= amount
    if player['health'] <= 0:
        player['health'] = 0
        player['alive'] = False

# Function for healing the player
def heal(player):
    if 'food' in player['inventory'] and player['inventory']['food'] > 0:
        player['health'] += 30  # Food restores 30 health
        player['inventory']['food'] -= 1
        print("You ate food and healed 30 health!")
    else:
        print("You don't have any food!")

# Function for buying items
def buy_item(player, item, cost):
    if player['money'] >= cost:
        player['money'] -= cost
        if item == 'ammo':
            player['ammo'] += 5
        elif item == 'food':
            player['inventory']['food'] += 1
        elif item == 'm60':
            player['weapon'] = 'm60'
            player['weapon_ammo'] = 500
            print("You bought the M60 machine gun!")
        elif item == 'semi_auto_rifle':
            player['weapon'] = 'semi_auto_rifle'
            player['weapon_ammo'] = 100
            print("You picked up the Semi-Auto Rifle with 100 rounds!")
        print(f"Purchased {item} for {cost} money.")
    else:
        print("Not enough money!")

# Function to check if player is alive
def is_alive(player):
    return player['alive']

# Function to handle animal taking damage
def animal_take_damage(animal, amount):
    animal['health'] -= amount
    if animal['health'] <= 0:
        animal['health'] = 0
        print(f"You defeated the {animal['name']}!")
        return True
    return False

# Function to handle animal attack
def animal_attack(animal):
    return animal['attack_damage']

# Function to handle shooting the player
def shoot(player, animal):
    print(f"Attempting to shoot the {animal['name']} with {player['weapon']}...")
    if player['weapon'] == 'pistol':
        if player['ammo'] <= 0:
            print("Out of ammo! Visit the shop to buy more.")
            return False

        player['ammo'] -= 1
        print("Aiming at the animal...")
        time.sleep(1)

        chance_to_hit = random.randint(1, 100)

        if chance_to_hit <= 50:  # 75% chance to hit
            damage = random.randint(10, 25)  # Random damage between 10 and 25
            print(f"You hit the {animal['name']} for {damage} damage!")
            return animal_take_damage(animal, damage)
        else:
            print(f"You missed the {animal['name']}!")
            print("\nTree falls with each shot...")            
            return False
            falling_tree_animation()

    elif player['weapon'] == 'm60':
        m60 = {
            'damage_per_bullet': 25,
            'accuracy': 50,
            'bullets_per_shot': 20,
            'ammo': 500
        }
        return m60_shoot(player, animal, m60)
    elif player['weapon'] == 'semi_auto_rifle':
        semi_auto_rifle = {
            'damage_per_bullet': 20,
            'accuracy': 70,
            'ammo': 100
        }
        return semi_auto_rifle_shoot(player, animal, semi_auto_rifle)

# Function for shooting with M60
def m60_shoot(player, animal, m60):
    if m60['ammo'] < m60['bullets_per_shot']:
        print("Not enough ammo for a full burst! Visit the shop to buy more.")
        return False

    m60['ammo'] -= m60['bullets_per_shot']
    print("Firing the M60...")

    time.sleep(1)

    total_damage = 0
    for _ in range(m60['bullets_per_shot']):
        if random.randint(1, 100) <= m60['accuracy']:  # 50% chance to hit each bullet
            total_damage += m60['damage_per_bullet']
    print(f"You hit the {animal['name']} for {total_damage} total damage with the M60!")
    return animal_take_damage(animal, total_damage)

# Function for shooting with Semi-Auto Rifle
def semi_auto_rifle_shoot(player, animal, semi_auto_rifle):
    if semi_auto_rifle['ammo'] <= 0:
        print("Out of ammo for the Semi-Auto Rifle! Visit the shop to buy more.")
        return False

    semi_auto_rifle['ammo'] -= 20
    print("Firing the Semi-Auto Rifle... BANG!")
    time.sleep(1)

    if random.randint(1, 100) <= semi_auto_rifle['accuracy']:
        total_damage = semi_auto_rifle['damage_per_bullet']
        print(f"You hit the {animal['name']} for {total_damage} damage with the Semi-Auto Rifle!")
        animal_take_damage(animal, total_damage)
    else:
        print("You missed!")

    print("\nTree falls with each shot...")
    falling_tree_animation()

    return True

# Function for falling tree animation
Image = Image.open("/workspaces/Computer-Programming-2/download.jpg")

# Function to handle the bear's turn
def bear_turn(player, animal):
    print(f"The {animal['name']} attacks!")
    damage = animal_attack(animal)
    take_damage(player, damage)
    print(f"The {animal['name']} dealt {damage} damage to you.")

# Function to display the player's status
def show_status(player):
    print(f"\nPlayer Health: {player['health']} | Ammo: {player['ammo']} | Money: {player['money']}")
    print(f"Food: {player['inventory'].get('food', 0)} | Weapon: {player['weapon']} ({player['weapon_ammo']} ammo)")

# Function shop menu
def shop(player):
    print("\nWelcome to the Shop!")
    print("1. Buy Ammo (5 bullets) - 20 money")
    print("2. Buy Food (heals 30 health) - 15 money")
    print("3. Buy M60 Machine Gun (500 ammo) - 200 money")
    print("4. Exit Shop")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        buy_item(player, 'ammo', 20)
    elif choice == "2":
        buy_item(player, 'food', 15)
    elif choice == "3":
        buy_item(player, 'm60', 200)
    elif choice == "4":
        print("Exiting the shop.")
        return
    else:
        print("Invalid choice. Try again.")
    time.sleep(1)

# Function to encounter animals
def encounter_animal(player):
    animals = [
        create_animal('Deer', 'Tier 1', 10, 30, 5),
        create_animal('Raccoon', 'Tier 1', 15, 20, 4),
        create_animal('Coyote', 'Tier 2', 25, 40, 7),
        create_animal('Bear', 'Tier 3', 50, 50, 15),
        create_animal('Moose', 'Tier 3', 60, 70, 20),
        create_animal('Bird', 'Tier 1', 5, 10, 2)
    ]
    animal = random.choice(animals)
    print(f"\nA wild {animal['name']} appears!")
    return animal

# Main game loop
def game_loop():
    print("Game script is running...")
    player = create_player()

    print("You find a Semi-Auto Rifle with 100 rounds of ammo. Do you want to pick it up?")
    choice = input("Enter 'yes' to pick up the Semi-Auto Rifle or 'no' to leave it: ").lower()
    if choice == 'yes':
        player['weapon'] = 'semi_auto_rifle'
        player['weapon_ammo'] = 100
        print("You have picked up the Semi-Auto Rifle.")

    while is_alive(player):
        show_status(player)

        print("\nWalking through the forest...")
        time.sleep(2)

        print("Trees slowly sway as you walk through the forest...")
        print("You encounter an animal!")
        
        animal = encounter_animal(player)
        time.sleep(1)

        if shoot(player, animal):
            player['money'] += animal['money_reward']
            print(f"You earned {animal['money_reward']} money!")
            print(f"Current Money: {player['money']}")
            player['kills'] += 1
        else:
            bear_turn(player, animal)

        if player['kills'] >= 3:
            print("You've killed 3 animals.")
            print("Would you like to buy anything? (yes/no)")
            buy_choice = input().lower()
            if buy_choice == 'yes':
                shop(player)
            else:
                print("Do you want to leave the forest? (yes/no)")
                leave_choice = input().lower()
                if leave_choice == 'yes':
                    print("You leave the forest.")
                    break

    print("Game Over! You died.")

game_loop()