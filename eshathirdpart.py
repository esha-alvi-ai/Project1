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
