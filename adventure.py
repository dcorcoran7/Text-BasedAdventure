# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: David Corcoran
"""
__version__ = 8
import random

"""In this project, You have been hired to discover the truths about the Egyptian pyramids.
You will go through the pyramid making choices taht will either benefit you or punish you.
If you lose all of your ealth then you lose the game and you can quit at any time by typing quit.
Youre goal is to make it through alive and to complete your mission.
"""

# 2) print_introduction: Print a friendly welcome message for your game
"""This function prints a welcome message and inputs your name in the message after you type it in
Consumes: Nothing
Returns: Nothing
"""
def print_introduction():
    user_name = input("Enter your name")
    print("""
Welcome """ + str(user_name) + """! Virginia Tech has flown you out to Egypt
in order to discover the mysteries of the ancient pyramids.
You have been assigned to travel into the Great Pyramid of Giza
and find artifacts and uncover centuries of history.
But beware, there is a rumor that the pyramid is cursed. Good Luck!
""")

# 3) get_initial_state: Create the starting player state dictionary
"""This function sets an intial player state with game status, location, health, score, and inventory.
Consumes: Nothing
Returns: Intial Dictionary
"""
def get_initial_state():
    initial_dictionary = {
        "game status": "playing",
        "location": "Pyramid Entrance",
        "health": 100,
        "score": 0,
        "inventory": []
        }
    return initial_dictionary

# 4) print_current_state: Print some text describing the current game world
"""This function prints out the players current state after it gets updated throughout the program. After every choice, it prints.
Consumes: Current State
Returns: Nothing
Prints: Location, Score, Health, and inventory
"""
def print_current_state(current_state):
    print("")
    print("LOCATION: " + str(current_state["location"]))
    print("""HEALTH: """ + str(current_state["health"]) + """
SCORE: """ + str(current_state["score"]) + """
INVENTORY: """ + str(current_state["inventory"]))
    
# 5) get_options: Return a list of commands available to the player right now
"""This function prints an brief explanation of where you are and also stores the choices the payer has at the moment.
Consumes: Current State
Returns: Options
"""
def get_options(current_state):
    if current_state["location"] == "Pyramid Entrance":
        print("""
As you approach the pyramid, you begin to look around for an entrance.
Upon further inspection you find a secret opening.""")
        options = ["Enter Pyramid", "Run Away", "quit"]
        return options
    elif current_state["location"] == "Inside Pyramid":
        print("""
After crawling through the opening, you find two paths.""")
        options = ["Go Left", "Go Right", "quit"]
        return options
    elif current_state["location"] == "Mummy Room":
        print("""
You enter a dark room with a golden casket in the middle and a ladder to the side.""")
        options = ["Open the Casket", "Climb the Ladder", "quit"]
        return options
    elif current_state["location"] == "Treasure Room":
        print("""
You climb into a room full of gold, jewels, and many other various valuable items.""")
        options = ["Take Treasure", "Leave Treasure", "quit"]
        return options
    elif current_state["location"] == "Pyramid Exit":
        print("""
You have reached the outside of the pyramid! What would you like to do with the information you have acquired?""")
        options = ["Keep Info", "Share Info", "quit"]
        return options
    
# 6) print_options: Print out the list of commands available
"""This functions uses the options given and prints them for the player to see and respond to. It also tells you how many choices the player has.
Consumes: Currrent Options
Returns: Nothing
Prints: Current Options and Number of Options
"""
def print_options(current_options):
    list_length = len(current_options)
    print("")
    print("You have " + str(list_length) + " available choices.")
    index = 0
    while index < list_length:
        print("\t" + current_options[index])
        index += 1
               
# 7) get_user_input: Repeatedly prompt the user to choose a valid command
"""This functions give the player an input option. If their input equals a current option, returns the choice.
If it doesnt, the game repeats the step. If it equals quit, it returns quit.
Consumes: Commands
Returns: Choice Made, Pass, or Quit
"""
def get_user_input(commands):
    while True:
        print("")
        choice = input("What would you like to do?")
        if choice in commands:
            return choice
            break
        elif "quit" in choice:
            return "quit"
        else:
            pass

# 8) process_command: Change the player state dictionary based on the command
"""This funtion processess what to do with the command given in get_use_input. If the choice matches the option then it moves the game on to the next step with
appropriate consequences by changing various aspects of the current player state dictionary. If the choice was quit, then it changes the game status to quit.
Consumes: Input Commands and Current State Dictionary
Returns: Nothing
Prints: Appropriate descirtion of the consequence of the players current action
"""
def process_command(command, current_state):
    if command == "quit":
        current_state["game status"] = "quit"
    elif current_state["location"] == "Pyramid Entrance":
        if command == "Enter Pyramid":
            print("""You enter the pyramid""")
            current_state["location"] = "Inside Pyramid"
            current_state["score"] += 10
        if command == "Run Away":
            print("""
A magical force prevents you from running away, you must enter the pyramid.""")
            current_state["location"] = "Inside Pyramid"
            current_state["score"] -= 10
    elif current_state["location"] == "Inside Pyramid":
        if command == "Go Left":
            print("""
You go left
You ran into a snake! It bites you dealing 25 damage.
You run back and go toward the right path.""")
            current_state["inventory"].append("Snake Tooth")
            current_state["health"] -= 25
            current_state["score"] -= 10
            current_state["location"] = "Mummy Room"
        if command == "Go Right":
            print("""
You go right""")
            current_state["location"] = "Mummy Room"
            current_state["score"] += 10
    elif current_state["location"] == "Mummy Room":
        if command == "Open the Casket":
            mummy_damage = random.randint(25, 75)
            print("""
As you open the casket, a mummified hand reaches out and grabs you!
It deals """ + str(mummy_damage) + """ damage and you quickly close the casket
before anything more can happen.""")
            current_state["health"] -= int(mummy_damage)
            current_state["score"] -= 20
            if current_state["health"] <= 0:
                print("You lost all of your health")
                current_state["game status"] = "lose"
            else:
                print("""Luckily, you were able to take a gold statue before closing the casket.
You then climb up the ladder.""")
                current_state["inventory"].append("Gold Statue")
                current_state["location"] = "Treasure Room"
        if command == "Climb the Ladder":
            print("""
You climb up the ladder.""")
            current_state["location"] = "Treasure Room"
            current_state["score"] += 20
    elif current_state["location"] == "Treasure Room":
        if command == "Take Treasure":
            pyramid_damage = random.randint(5, 30)
            print("""
After taking the treasure, the entire pyramid starts to shake. Blocks from the ceiling
begin to fall. While running away, falling rubble hits you dealing """ + str(pyramid_damage) + """
damage!""")
            current_state["health"] -= int(pyramid_damage)
            if current_state["health"] <= 0:
                current_state["score"] -= 20
                print("You lost all of your health")
                current_state["game status"] = "lose"
            else:
                print("""
You took the treasure and escaped the Treasure Room collapse by
finding a small opening at the end of the room.""")
                current_state["inventory"].append("Pharoah's Treasure")
                current_state["score"] += 30
                current_state["location"] = "Pyramid Exit"
        if command == "Leave Treasure":
            current_state["score"] += 60
            print("""
You leave the treasure as it is and begin walking toward the crevace that you spot in the corner of the room.
Once you get there, you spot a slab of hieroglyphics that you presume tell the history
of the pyramid and decide to take them to complete your mission.""")
            current_state["location"] = "Pyramid Exit"
            current_state["inventory"].append("Hieroglyphics")
    elif current_state["location"] == "Pyramid Exit":
        inventory_size = len(current_state["inventory"])
        if command == "Keep Info":
            current_state["score"] -= 50
            print("""
Virginia Tech is not happy with your decision to keep the knowledge of the pyramid all for yourself.
As a result, they fire you from the job and hire a new person.""")
            if inventory_size >= 2:
                current_state["score"] += 50
            current_state["game status"] = "lose"
        if command == "Share Info":
            print("""
Virginia Tech is pleased with your decision to share the information about the pyramid with them as agreed at the beginning
of your mission. As a result, they promote you, give you a raise, and will confront you about any future expeditions!""")
            current_state["score"] += 50
            if inventory_size >= 2:
                current_state["score"] += 50
            current_state["game status"] = "win"
                
# 9) print_game_ending: Print a victory, lose, or quit message at the end
"""This function takes the prgrom out of the while loop by changing the game status from playing. It can cahnge the game status to win, lose, or quit.
Then it prints an appropriate end game message and displays the players score from the ending current state dictionary.
Consumes: Current State Dicionary
Return: Nothing
Prints: End Game Message, Score from Current State Dicitonary
"""

def print_game_ending(current_state):
    if current_state["game status"] == "quit":
        print("""
You Quit the Game!""")
        print("Your score was " + str(current_state["score"]) + " out of 200 points!")
    elif current_state["game status"] == "win":
        print("""
Congratulations, You Won the Game!""")
        print("Your score was " + str(current_state["score"]) + " out of 200 points!")
    elif current_state["game status"] == "lose":
        print("""
You Lost the Game""")
        print("Your score was " + str(current_state["score"]) + " out of 200 points!")
    elif current_state == get_initial_state():
        print(current_state["game status"])
        
# Command Paths to give to the unit tester
"""The win path is a series of srtings that tells the computer how to consistnety win the game.
The lose path is a series of strings that tells the computer how to consistently lose the game.
"""

WIN_PATH = ["Enter Pyramid", "Go Right", "Climb the Ladder", "Leave Treasure", "Share Info"]
LOSE_PATH = ["Run Away", "Go Left", "Open the Casket", "Take Treasure", "Keep Info"]

# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
"""This finctions runs the etnire program by organizaing thefunstions in a logical order. It uses a while loop for players current state of game status and
must equal playing. If it doesn, the program goes out of the loop and prints a game-ending message with your score.
Consumes: Nothing
Returns: Nothing
"""
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)  
    # Give user message
    print_game_ending(the_player)


# Executes the main function
if __name__ == "__main__":
    #You might comment out the main function and call each function
    #one at a time below to try them out yourself'''
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # print_introduction()
    # print(get_initial_state())
    # ...
    