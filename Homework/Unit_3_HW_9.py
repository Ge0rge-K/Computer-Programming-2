from pathlib import Path
import json, requests

POKE_URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

resp = requests.get(POKE_URL, timeout=10) # gets a url response 
try:
    resp.raise_for_status() # Prevents crashes form the 404 error
    data = resp.json()
    moves = data.get("moves", [])  # Get the pikachu's moves field
    
    # Print all move names from data and then the moves variable
    for move in moves:
        print(move["move"]["name"])
except requests.HTTPError:
    print("404 Error")