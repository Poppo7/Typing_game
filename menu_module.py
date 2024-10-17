'''
Typing/Stealth Game
By: Poppo7
'''
# menu_module.py

def display_menu():
    # Display the main menu
    print("\n .d8888.d888888b d88888b  .d8b.  db      d888888b db   db       d888b   .d8b.  .88b  d88. d88888b ")
    print("88'  YP `~~88~~' 88'     d8' `8b 88      `~~88~~' 88   88      88' Y8b d8' `8b 88'YbdP`88 88'")     
    print("`8bo.      88    88ooooo 88ooo88 88         88    88ooo88      88      88ooo88 88  88  88 88ooooo")
    print("  `Y8b.    88    88~~~~~ 88~~~88 88         88    88~~~88      88  ooo 88~~~88 88  88  88 88~~~~~")
    print("db   8D    88    88.     88   88 88booo.    88    88   88      88. ~8~ 88   88 88  88  88 88.")     
    print("`8888Y'    YP    Y88888P YP   YP Y88888P    YP    YP   YP       Y888P  YP   YP YP  YP  YP Y88888P")
    print("\n1. Start Game")
    print("2. How To Play/Rules")
    print("3. Change Difficulty (Easy/Normal/Hard)")
    print("4. Quit")

def get_user_choice(prompt="Select an option (1/2/3/4): ", display_prompt=True):
    # Display the prompt if display_prompt is True
    if display_prompt:
        print(prompt, end='')
    # Get user input for menu choice
    return input()

def display_menu_message(message):
    # Display a message in the menu
    print(message)

def display_go_back_message():
    # Display a message to go back to the menu
    print("\nType anything to return to main menu: ")

def display_instructions():
    # Display game instructions
    print("\nInstructions:")
    print("-Type the displayed sentence within the time limit to avoid detection.")
    print("-Score points for each correct sentence. You have three attempts; run out of attempts, and the game ends.")
    print("-Easy mode will give you a 20-second timer, normal mode will give you a 15-second timer, and hard mode will give you a 10-second timer.")
    print("-If the timer runs out, you lose an attempt.")
    print("-Before starting, install \033[93mpip install inputimeout\033[0m in the terminal in order for the game to work.")