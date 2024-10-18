'''
Typing/Stealth Game
By: Poppo7
'''
# !BEFORE STARTING! in the terminal type: "pip install inputimeout" in order for the game to work.
# inputimeout is used by allowing you to specify a timeout.

# Import necessary libraries and modules
import time
import random
from inputimeout import inputimeout, TimeoutOccurred
from menu_module import display_menu, get_user_choice, display_menu_message, display_instructions, display_go_back_message

# Display introduction
def display_intro(difficulty):
    print("\nWelcome to Stealth Typing Game!")
    print("Type quietly to avoid detection.")
    print(f"Difficulty: {difficulty.capitalize()}.")
# Display sentences 
def generate_sentence():
    sentences = [
        "Hi there, hope you are doing great!",
        "The quick brown fox jumps over the lazy dog.",
        "How is your progress so far?",
        "Python is a versatile programming language.",
        "Stealth is the key to success.",
        "Type your way to victory.",
        "You can master anything if you discipline yourself.",
        "Nope.",
        "Monday, Tuesday, Wednesday",
        "The classical guitar is different than an acoustic.",
        "The hands find a way to do what the heart wants to say.",
        "Embrace your flaws, for they are the key to greatness.",
        "No drinking! No swimming!",
        "Caution! Chimera crossing!",
        "Failure is not the end.",
        "What's your favorite type of candy?",
        "A, B, C, D, E, F, G",
        "Sesquipedalianism",
        "Type the space key twice  !",
        "Ice baths or showers can improve your cognitive functionality.",
        "I used to play piano by ear, but now I use my hands.",
        "The only person who can truly change you is yourself.",
        "Mozart composed his first piece in 1761.",
        "Are you all right? No, you are left.",
        "What lights up a soccer stadium? A soccer match.",
        "Apples, oranges, pears, guava.",
        "What's your favorite movie?",
        "Hello world!",
        "Merry Christmas, Ho, Ho, Ho!",
        "Time is valuable.",
        "What do elves learn in school? The elf-abet.",
        "Yes.",
        "Python Fundamentals",
        "The first guitar was created in ancient Egypt.",
        "The Amazing Spider-Man",
        "Indomitable spirit, ancient memory, leap.",
        "Battle Mage, Bellatrix, Astarte",
        "What's Forrest Gump's password? 1forrest1.",
        "TTSTTTS is the major scale pattern.",
        "Don't get caught!",
        "Drink water and always sit/stand up straight!",
        "Man it hurts to be this hip.",
        "Showing off is a fool's idea for glory.",
        "Change Difficulty (Easy/Normal/Hard)",
        "qwerty asdf 1234",
        "==== !@#$Q",
        "Time flies like an arrow. Fruit flies like a banana.",
        "Power Geyser, Rising Upper, Power Wave",
        "Slow and steady wins the race.",
        "What did 0 say to 8? Nice belt.",
        # Additional sentences for now
        "JavaScript and Python are popular languages for web development.",
        "To be or not to be, that is the question.",
        "A stitch in time saves nine.",
        "Every cloud has a silver lining.",
        "You miss 100% of the shots you don't take.",
        "When life gives you lemons, make lemonade.",
        "Fortune favors the bold.",
        "Practice makes perfect.",
        "Don't put all your eggs in one basket.",
        "A journey of a thousand miles begins with a single step.",
        "Keep your friends close and your enemies closer.",
        "All that glitters is not gold.",
        "Brevity is the soul of wit.",
        "The early bird catches the worm.",
        "Actions speak louder than words.",
        "Beauty is in the eye of the beholder.",
        "Curiosity killed the cat.",
        "Don't count your chickens before they hatch.",
        "Necessity is the mother of invention.",
        "Opportunity knocks but once.",
        "Silence is golden.",
        "Honesty is the best policy.",
        "Laughter is the best medicine.",
        "Knowledge is power.",
        "No pain, no gain.",
        "An apple a day keeps the doctor away.",
        "Better late than never.",
        "The pen is mightier than the sword.",
        "Two wrongs don't make a right.",
        "A picture is worth a thousand words.",
    ]
    
    # Add random function so the sentences can shuffle
    return random.choice(sentences)

# Main function to play the stealth typing game
def play_stealth_typing_game(difficulty):
    score = 0  # Default score
    max_attempts = 3  # Total attempts

    # Set time limits based on difficulty
    if difficulty == 'easy':
        time_limit = 25
    elif difficulty == 'normal':
        time_limit = 15
    elif difficulty == 'hard':
        time_limit = 10
    else:
        print("Invalid difficulty. Starting in normal mode.")
        time_limit = 15

    # Add while loop
    while True:
        display_menu()

        # Get user choice
        choice = get_user_choice()

        if choice == '1':
            play_game(score, max_attempts, time_limit, difficulty)
        elif choice == '2':
            display_instructions()
            # Use go back function giving a display prompt of false so the get_user_choice menu doesn't appear
            display_go_back_message()
            back_choice = get_user_choice(display_prompt=False)
            if back_choice != '1':
                display_menu_message("Returning to the main menu.")
                continue  # Continue the loop to display the menu again
        elif choice == '3':
            # Difficulty menu
            new_difficulty = input("Select difficulty (Easy/Normal/Hard): ").lower()
            if new_difficulty in ['easy', 'normal', 'hard']:
                difficulty = new_difficulty
                display_menu_message(f"Difficulty set to {difficulty.capitalize()}.")
            else:
                # Automatically adjust to normal mode if the user inputs the wrong instruction
                difficulty = 'normal'
                display_menu_message("Invalid difficulty. Setting to normal.")
        elif choice == '4':
            display_menu_message("\nThank you for playing!\n")
            break
        else:
            display_menu_message("Invalid choice. Please choose again.")

# Function to play the actual game
def play_game(score, max_attempts, time_limit, difficulty):
    display_intro(difficulty)
    time.sleep(3) # This is where the time module kicks in

    while True:
        sentence = generate_sentence()
        print("\nYour mission: \033[93m", sentence, "\033[0m")

        try:
            # Get user input within the time limit
            user_input = inputimeout(prompt="Type here: ", timeout=time_limit)
            if user_input.lower() == sentence.lower():
                print("Correct! You typed quietly.")
                score += 1
            else:
                print("Oops! You were detected.")
                max_attempts -= 1
                if max_attempts == 0:
                    break
        except TimeoutOccurred: # inputime module
            print("Time's up! You were detected.")
            max_attempts -= 1
            if max_attempts == 0:
                break

        print(f"Score: {score}\n")
        time.sleep(1)  # inputimeout module

    print("\nGame Over. Your final score:", score)

# Main entry point of the program
if __name__ == "__main__":
    # Get the difficulty level from the user
    difficulty = input("\nSelect difficulty (Easy/Normal/Hard): ").lower()

    # Start the game with the chosen difficulty
    play_stealth_typing_game(difficulty)