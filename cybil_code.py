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
