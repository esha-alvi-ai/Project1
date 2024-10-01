Documentation for the Adventure Game Code




By: Cybil Fatima (SP23-BAI-013)

Esha Alvi(SP23-BAI-015)

Overview



game allows players to navigate through various rooms, collect items, solve puzzles, and interact with the environment. It incorporates elements of exploration, inventory management, and score tracking, enhancing the player's experience in a horror-themed setting.
Room Interaction Logic
•	Conditional Movement Logic: The game restricts movement based on item possession, specifically for the locked room (Basement), which adds an additional layer of challenge.
•	Dynamic Inventory Updates: The game dynamically updates the inventory based on player actions, ensuring that the state reflects the player's choices.

Key Components
1. Data Structure
•	Rooms Dictionary: Defines the game environment with key details for each room:
o	Description: A narrative for the room.
o	Exits: Possible directions the player can move to other rooms.
o	Items: List of items present in the room.
o	Locked Status: Indicates whether a room (e.g., Basement) is locked.



3. Game Flow
•	start_game(): Initiates the game by welcoming the player and checking if they want to proceed.
•	load_game(): Loads the game state from a JSON file if it exists, restoring the player’s current room, inventory, visited rooms, and score.
•	save_game(): Saves the current game state to a JSON file for future retrieval.



4. Room Navigation
•	describe_room(): Provides a detailed description of the current room, including items and exits. It also plays random creepy sounds to enhance immersion.
•	move(direction): Updates the current room based on player input, checks for valid exits, and provides room descriptions and updates scores.


5. Inventory Management
•	take_items(item): Allows players to collect items from the room and updates the score.
•	drop_items(item): Enables players to drop items from their inventory back into the room.
•	use_items(item): Facilitates item usage, including unlocking doors or utilizing items for their intended purposes.
•	examine(item): Provides detailed descriptions of items in the player’s inventory or within the current room.


6. Scoring System
•	display_score(): Displays the player's current score.
•	update_score(points): Updates the score based on player actions.
•	update_highest_score(): Tracks and saves the highest score achieved in the game.


7. Random Events
•	random_sounds(): Generates random eerie sound effects to heighten the game's horror atmosphere.



8. Puzzle Functionality
•	puzzle(): Engages players in solving a riddle read from an external text file. Correct answers reward players with items and additional points.




9. User Commands

   
The game supports various user commands:
•	Movement: go [direction]
•	Room description: look
•	Inventory management: inventory, take [item], drop [item], use [item], examine [item]
•	Game state management: save, load, delete, quit
•	Puzzle engagement: puzzle
•	Help menu: help
10. File Management
•	delete_save_game(): Deletes the saved game file, freeing up memory.
Error Handling
•	Error Management: The code includes basic error handling for file operations (e.g., loading game state and saving scores) to ensure smooth gameplay even when issues arise (like missing files).
•	Invalid Command Feedback: The game prompts users with clear messages if they enter invalid commands, helping improve user experience.


Conclusion
This adventure game code provides a comprehensive framework for an engaging, interactive experience. It allows players to explore a spooky environment, manage an inventory, solve puzzles, and track their scores while enjoying immersive sound effects. The structured approach to room navigation, item management, and game state saving enhances replayability and player engagement.
_____________________________________________________________________________________
  Sample Game Walkthrough / Gameplay


  
Sample Output 1


Welcome to the Adventure Game!
Enter your name: Esha
Hello, Esha! Are you ready to join this adventure? (yes/no)
yes
Let's begin!
You are in the entrance hall. Exits are to the north, east, and west.
You hear heavy breathing, but it's not coming from you.
Exits are: north, east, west
Items in this room: 

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go north
You are in the Living Room with dim lighting. Exits are to the south and west.
The sound of dripping water intensifies, even though there’s no leak.
Exits are: south, west
Items in this room: key

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): take key
The key is picked up.
Your current score is: 2

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go south
You are in the Entrance Hall. Exits are to the north, east, and west.
A faint voice whispers your name, sending a chill down your spine.
Exits are: north, east, west
Items in this room: 

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go east
You are in the Kitchen. Exits are to the west and north.
Suddenly, all the furniture shifts a few inches on its own.
Exits are: west, north
Items in this room: knife

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): take knife
The knife is picked up.
Your current score is: 4

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go north
You are in the Basement. The exit is to the south. You see a locked door to the north.
You hear heavy breathing, but it's not coming from you.
Exits are: south
Items in this room: 
You can't go this way! Try again.

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): use key
You used the key
Your current score is: 14
You unlocked the door. You can escape from the game.

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): exit
Your score: 14, Highest score: 0





Sample Output 2




Welcome to the Adventure Game!
Enter your name: Cybil
Hello, Cybil! Are you ready to join this adventure? (yes/no)
yes
Let's begin!
You are in the entrance hall. Exits are to the north, east, and west.
A door slams shut behind you!
Exits are: north, east, west
Items in this room: 

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go east
You are in the Kitchen. Exits are to the west and north.
The sound of dripping water intensifies, even though there’s no leak.
Exits are: west, north
Items in this room: knife

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): take knife
The knife is picked up.
Your current score is: 2

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go north
You are in the Basement. The exit is to the south. You see a locked door to the north.
A faint voice whispers your name, sending a chill down your spine.
Exits are: south
Items in this room: 

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go south
You are in the Kitchen. Exits are to the west and north.
You hear heavy breathing, but it's not coming from you.
Exits are: west, north
Items in this room: knife

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go west
You are in the Living Room. Exits are to the south and west.
Suddenly, all the furniture shifts a few inches on its own.
Exits are: south, west
Items in this room: key

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): take key
The key is picked up.
Your current score is: 4

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go south
You are in the Entrance Hall. Exits are to the north, east, and west.
A door slams shut behind you!
Exits are: north, east, west
Items in this room: 

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): go north
You are in the Living Room. Exits are to the south and west.
The sound of dripping water intensifies, even though there’s no leak.
Exits are: south, west
Items in this room: 

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): use key
You used the key
Your current score is: 14
You unlocked the door. You can escape from the game.

Enter your command (go, take, drop, use, examine, save, load, delete, or exit): exit
Your score: 14, Highest score: 0



