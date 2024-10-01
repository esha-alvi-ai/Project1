# Coded by Esha
import random
import json

# Dictionary to store room details
# Coded by Esha
#sp23-bai-015
rooms = {
    "Entrance Hall": {
        "description": "You are in the entrance hall. Exits are to the north, east, and west.",
        "exits": {"north": "Living Room", "east": "Kitchen", "west": "Toilet"},
        "items": []
    },
    "Living Room": {
        "description": "A creepy living room with dim lighting. Exits are to the south and west.",
        "exits": {"south": "Toilet", "west": "Master Room"},
        "items": ["key"]
    },
    "Toilet": {
        "description": "A small, grimy toilet. The exit is to the east.",
        "exits": {"east": "Kitchen", "west": "Basement"},
        "items": ["mirror shard"]
    },
    "Master Room": {
        "description": "A large master room with old furniture. Exits are to the east.",
        "exits": {"east": "Kitchen", "south": "Basement"},
        "items": ["journal"]
    },
    "Kitchen": {
        "description": "An old, abandoned kitchen. Exits are to the west and north.",
        "exits": {"west": "Toilet", "north": "Basement", "south": "Master Room"},
        "items": ["knife"]
    },
    "Basement": {
        "description": "A dark basement. The exit is to the south. You see a locked door to the north.",
        "exits": {"south": "Kitchen", "north": None},
        "items": [],
        "locked": True
    }
}
#start sturture of game
def start_game():
    print("Welcome to the Adventure Game!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Are you ready to join this adventure? (yes/no)")

    if input().lower() == 'yes':
        print("Let's begin!")
        return True
    else:
        print("Thanks for playing! Goodbye!")
        return False
#to delete file (clean memory)
def delete_save_game():
    if path.exists("save_game.json"):
        remove("save_game.json")
        print("Your saved game has been deleted.")
    else:
        print("No saved game found to delete.")
#to show the structure of rooms
def describe_room():
    print(rooms[current_room]["description"])
    random_sounds()
    print("Exits are: " + ", ".join(rooms[current_room]["exits"].keys()))
    
    if rooms[current_room]["items"]:
        print("Items in this room: " + ", ".join(rooms[current_room]["items"]))
    else:
        print("There are no items in this room.")

# to load file data
def load_game():
    global current_room, inventory, visited_rooms, score
    try:
        with open("save_game.json", "r") as file:
            game_state = json.load(file)
            current_room = game_state['current_room']
            inventory = game_state['inventory']
            visited_rooms = set(game_state['visited_rooms'])
            score = game_state.get('score', 0)
        print("Game loaded successfully!")
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        current_room = "Entrance Hall"
        inventory = []
        visited_rooms = set()
        score = 0

# to save data
def save_game():
    game_state = {
        "current_room": current_room,
        "inventory": inventory,
        "visited_rooms": list(visited_rooms),
        "score": score
    }
    with open('save_game.json', 'w') as save_file:
        json.dump(game_state, save_file)
    print("Your game is saved successfully!")
    random_sounds()