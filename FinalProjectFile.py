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
# coded by esha alvi sp23-bai-015
#coded by esha alvi sp23-bai-015



def drop_items(item):
    if item in inventory:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        update_score(-2)
        print(f"The {item} is dropped.")
    else:
        print(f"The {item} is not available to drop down.")

def use_items(item):
    if item in inventory:
        print(f"You used the {item}")
        update_score(10)
        random_sounds()

        if item == "key" and current_room == "Basement":
            
            print(f"You unlocked the door. You can escape from the game.")
            rooms["Basement"]["locked"] = False
            update_score(10)

        elif item == "journal":
            print("You read the journal. It contains notes about the castle's history and hidden passages.")
            update_score(5)
        elif item == "knife":
            print("You wave the knife menacingly. It might help in dangerous situations.")
            update_score(5)
    else:
        print(f"You can't use the {item}.")

# Examine items
def examine(item):
    if item in inventory:
        if item == "key":
            print("A small, rusty key. It might open a locked door somewhere.")
        elif item == "knife":
            print("A sharp knife, still in good condition. It can be useful in dangerous situations.")
        elif item == "journal":
            print("An old journal filled with notes and sketches. It might contain clues about the castle's secrets.")
        elif item == "mirror shard":
            print("A broken shard of a mirror. It could be sharp or useful for reflecting light.")
    elif item in rooms[current_room]["items"]:
        if item == "key":
            print("You see a small key lying on the ground. It looks like it could open something.")
        elif item == "knife":
            print("A knife is lying on the counter. It looks sharp and dangerous.")
        elif item == "journal":
            print("An old journal is on the table. It appears to be filled with handwritten notes.")
        elif item == "mirror shard":
            print("A shard of a broken mirror is on the floor. It glints in the dim light.")
    else:
        print("You don't see anything special about that.")

def puzzle():
    with open("riddle.txt", "r") as file:
        riddle = file.readlines()
        selection = random.choice(riddle).strip()
        question, correct_answer = selection.split("||")
        user_answer = input(f"What is the answer to the riddle: {question}? ")
        if user_answer.lower() == correct_answer.strip().lower():
            print("Correct! You unlocked the door.")
            inventory.append("Map")
            update_score(50)
            return True
        else:
            print("Incorrect. Try again.")
            return False


# Main game loop
if start_game():
    current_room = "Entrance Hall"
    inventory = []
    visited_rooms = set()
    visited_rooms.add(current_room)

    load_game()

    while True:
        describe_room()
        display_score()

        exit_display = ", ".join(f"{direction}: {room}" for direction, room in rooms[current_room]["exits"].items())
        print("Exits are: " + exit_display)

        if rooms[current_room]["items"]:
            print("Items in this room: " + ", ".join(rooms[current_room]["items"]))

        if inventory:
            print("Your inventory: " + ", ".join(inventory))
        else:
            print("Your inventory is empty.")

        print("\nAvailable commands:")
        if not (current_room == "Basement" and "key" in inventory): 
            print("1: Go [direction] (e.g., go north)")
        else:
            print("You have the key to unlock the door. You cannot move to other rooms now.")
        
        print("2: Look")
        print("3: Inventory")
        print("4: Take [item] (e.g.,take knife)")
        print("5: Drop [item] (e.g., drop knife)")
        print("6: Use [item] (e.g.,use knife)")
        print("7: Examine [object] (e.g., examine knife)")
        print("8: puzzle")
        print("9: Save")
        print("10: Load")
        print("11: Quit")
        print("12: Help")
        print("13: Delete")

        action = input("What do you want to do? ").strip().lower()

        if action.startswith("go "):
            direction = action.split(" ")[1]
            move(direction)
        elif action == "look":
            describe_room()
        elif action == "inventory":
            if inventory:
                print("You have the following items: " + ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif action.startswith("take "):
            item = action.split(" ", 1)[1]
            take_items(item)
        elif action.startswith("drop "):
            item = action.split(" ", 1)[1]
            drop_items(item)
        elif action.startswith("use "):
            item = action.split(" ", 1)[1]
            use_items(item)
        elif action.startswith("examine "):
            item = action.split(" ", 1)[1]
            examine(item)
        elif action =="puzzle":
            puzzle()
        elif action == "save":
            save_game()
        elif action == "load":
            load_game()
        elif action == "delete":
            delete_game()
        elif action == "quit":
            print("Thank you for playing!")
            update_highest_score()
            break
        elif action == "help":
            print("\nAvailable commands:")
            print("1: Go [direction] (e.g., go north)")
            print("2: Look")
            print("3: Inventory")
            print("4: Take [item]  (e.g.,take knife)")
            print("5: Drop [item](e.g.,drop knife)")
            print("6: Use [item](e.g.,use knife)")
            print("7: Examine [object](e.g.,examine knife)")
            print("8: puzzle")
            print("9: Save")
            print("10: Load")
            print("11: Quit")
            print("12: Help")
            print("13:  Delete")


        else:
            print("Invalid action. Type 'help' for the list of commands.")
