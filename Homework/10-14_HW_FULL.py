import json
import os

FILENAME = "user_profile.json"

def load_user_data():
    """Load user data from file if it exists."""
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_user_data(user_data):
    """Save user data to the file."""
    with open(FILENAME, "w") as f:
        json.dump(user_data, f)

def get_new_user_data():
    """Prompt for new user information and return as a dictionary."""
    user_data = {}
    user_data["name"] = input("What is your name? ")
    user_data["age"] = input("What is your age? ")
    user_data["favorite_color"] = input("What is your favorite color? ")
    user_data["favorite_number"] = input("What is your favorite number? ")
    return user_data

def greet_user():
    user_data = load_user_data()

    if user_data:
        confirm = input(f"Are you {user_data['name']}? (y/n): ").lower()
        if confirm == 'y':
            print(f"\nWelcome back, {user_data['name']}!")
            print("This is the data we have stored:")
            for key, value in user_data.items():
                print(f"{key.title()}: {value}")
        else:
            user_data = get_new_user_data()
            save_user_data(user_data)
            print(f"\nThanks {user_data['name']}, your info has been saved!")
    else:
        user_data = get_new_user_data()
        save_user_data(user_data)
        print(f"\nThanks {user_data['name']}, your info has been saved!")

greet_user()
