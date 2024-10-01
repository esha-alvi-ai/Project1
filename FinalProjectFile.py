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
    

# coded by cybil
# Function to display room details
def describe_room():
    print(rooms[current_room]["description"])
    random_sounds()
    print("Exits are: " + ", ".join(rooms[current_room]["exits"].keys()))
    
    if rooms[current_room]["items"]:
        print("Items in this room: " + ", ".join(rooms[current_room]["items"]))
    else:
        print("There are no items in this room.")
        

# Display and update score
score = 0
highest_score = 0

def display_score():
    print(f"Your current score is: {score}")

def update_score(points):
    global score
    score += points
    display_score()



def update_highest_score():
    global score, highest_score
   
    if path.exists("score.json"):
        try:
            with open("score.json", "r") as file:
                data = json.load(file)
                highest_score = data.get("highest_score", 0)
        except (json.JSONDecodeError, FileNotFoundError):
            highest_score = 0
    else:
        highest_score = 0
    
   
    if score > highest_score:
        with open("score.json", "w") as file:
            json.dump({"highest_score": score}, file)
        highest_score = score
        print(f"Your new high score is {highest_score}!")
    else:
        print(f"Your score: {score}, Highest score: {highest_score}")


# Random creepy sounds
def random_sounds():
    sounds = [
        "You hear heavy breathing, but it's not coming from you.",
        "A door slams shut behind you!",
        "The sound of dripping water intensifies, even though there’s no leak.",
        "A faint voice whispers your name, sending a chill down your spine.",
        "Your flashlight flickers, then goes out for a second.",
        "Suddenly, all the furniture shifts a few inches on its own."
    ]
    print(random.choice(sounds))
    

# Item handling functions
def take_items(item):
    if item in rooms[current_room]["items"]:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        update_score(2)
        print(f"The {item} is picked up.")
    else:
        print(f"The {item} is not available to pick up.")
    
# Move between rooms
def move(direction):
    global current_room  
    if direction in rooms[current_room]['exits']:
        next_room_name = rooms[current_room]['exits'][direction]
        if next_room_name is None:
            print("There is no room in that direction!")
            return
        current_room = next_room_name
        describe_room()
        update_score(5)
        random_sounds()
    else:
        print("Can't go this way! Try again.")