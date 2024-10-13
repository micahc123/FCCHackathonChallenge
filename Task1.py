import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def display_title():
    title = """
    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗     ██╗    ██╗██╗███████╗ █████╗ ██████╗ ██████╗ 
    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██║    ██║██║╚══███╔╝██╔══██╗██╔══██╗██╔══██╗
    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║ █╗ ██║██║  ███╔╝ ███████║██████╔╝██║  ██║
    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║███╗██║██║ ███╔╝  ██╔══██║██╔══██╗██║  ██║
    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚███╔███╔╝██║███████╗██║  ██║██║  ██║██████╔╝
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
    """
    print(Fore.CYAN + Style.BRIGHT + title + Style.RESET_ALL)

def get_difficulty():
    while True:
        animate_text("Choose your difficulty level:", color=Fore.YELLOW)
        animate_text("1. Easy (1-50, 10 guesses)", color=Fore.GREEN)
        animate_text("2. Medium (1-100, 7 guesses)", color=Fore.YELLOW)
        animate_text("3. Hard (1-200, 5 guesses)", color=Fore.RED)
        choice = input(Fore.MAGENTA + "Enter your choice (1/2/3): " + Style.RESET_ALL)
        if choice in ['1', '2', '3']:
            return int(choice)
        animate_text("Invalid choice. Please try again.", color=Fore.RED)

def play_game(difficulty):
    if difficulty == 1:
        max_number = 50
        max_guesses = 10
    elif difficulty == 2:
        max_number = 100
        max_guesses = 7
    else:
        max_number = 200
        max_guesses = 5

    secret_number = random.randint(1, max_number)
    guesses_left = max_guesses

    animate_text(f"\nI'm thinking of a number between 1 and {max_number}.", color=Fore.CYAN)
    animate_text(f"You have {max_guesses} guesses to find it.", color=Fore.CYAN)

    while guesses_left > 0:
        animate_text(f"\nGuesses left: {guesses_left}", color=Fore.YELLOW)
        guess = input(Fore.GREEN + "Enter your guess: " + Style.RESET_ALL)
        
        try:
            guess = int(guess)
        except ValueError:
            animate_text("Please enter a valid number.", color=Fore.RED)
            continue

        if guess < 1 or guess > max_number:
            animate_text(f"Please enter a number between 1 and {max_number}.", color=Fore.RED)
            continue

        guesses_left -= 1

        if guess == secret_number:
            animate_text("\nCongratulations! You guessed the number!", color=Fore.GREEN)
            animate_text(f"You had {guesses_left} guesses left.", color=Fore.YELLOW)
            return True
        elif guess < secret_number:
            animate_text("Too low! Try a higher number.", color=Fore.BLUE)
        else:
            animate_text("Too high! Try a lower number.", color=Fore.MAGENTA)

    animate_text(f"\nGame over! The number was {secret_number}.", color=Fore.RED)
    return False

def main():
    clear_screen()
    display_title()
    animate_text("Welcome to the Number Wizard Game!", color=Fore.GREEN)
    
    while True:
        difficulty = get_difficulty()
        clear_screen()
        display_title()
        result = play_game(difficulty)
        
        if result:
            animate_text("\nYou're a true Number Wizard!", color=Fore.GREEN)
        else:
            animate_text("\nBetter luck next time, apprentice!", color=Fore.YELLOW)
        
        play_again = input(Fore.CYAN + "\nDo you want to play again? (y/n): " + Style.RESET_ALL).lower()
        if play_again != 'y':
            break
    
    animate_text("\nThank you for playing Number Wizard! Goodbye!", color=Fore.GREEN)

if __name__ == "__main__":
    main()