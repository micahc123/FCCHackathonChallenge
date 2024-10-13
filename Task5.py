import time
import os
import random
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
    ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
    ██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
    ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
    ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
    ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
    """
    print(Fore.CYAN + Style.BRIGHT + title + Style.RESET_ALL)

def display_clock(hours, minutes, seconds, color=Fore.GREEN):
    clock = f"""
    {color}┌──────────────────────────┐
    │                          │
    │     {hours:02d} : {minutes:02d} : {seconds:02d}     │
    │                          │
    └──────────────────────────┘{Style.RESET_ALL}
    """
    print(clock)

def countdown_timer(event, total_seconds):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    color_index = 0

    while total_seconds > 0:
        clear_screen()
        display_title()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(Fore.YELLOW + f"\n{' '*10}Countdown to: {event}\n" + Style.RESET_ALL)
        display_clock(hours, minutes, seconds, color=colors[color_index])
        print(Fore.CYAN + f"\n{' '*10}Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}" + Style.RESET_ALL)
        
        time.sleep(1)
        total_seconds -= 1
        color_index = (color_index + 1) % len(colors)

    clear_screen()
    display_title()
    print(Fore.YELLOW + f"\n{' '*10}Countdown to: {event}\n" + Style.RESET_ALL)
    display_clock(0, 0, 0, color=Fore.RED)
    print(Fore.GREEN + "\n" + " "*10 + "Time's up!" + Style.RESET_ALL)
    
    fun_messages = [
        f"Woohoo! It's time for {event}!",
        f"The wait is over! {event} is here!",
        f"Let's get this party started! It's {event} time!",
        f"Break out the confetti! {event} has arrived!",
        f"The moment we've all been waiting for: {event} is now!"
    ]
    animate_text("\n" + " "*5 + random.choice(fun_messages), color=Fore.MAGENTA)

def get_user_input(prompt):
    while True:
        user_input = input(Fore.YELLOW + prompt + Style.RESET_ALL).strip()
        if user_input:
            return user_input
        print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

def get_time_input(prompt):
    while True:
        try:
            value = int(input(Fore.YELLOW + prompt + Style.RESET_ALL))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print(Fore.RED + "Please enter a valid positive number." + Style.RESET_ALL)

def main():
    clear_screen()
    display_title()
    animate_text("Welcome to the Countdown Timer!", color=Fore.GREEN)
    
    event = get_user_input("Enter the event name: ")
    hours = get_time_input("Enter hours: ")
    minutes = get_time_input("Enter minutes: ")
    seconds = get_time_input("Enter seconds: ")

    total_seconds = hours * 3600 + minutes * 60 + seconds

    print(Fore.MAGENTA + "\nStarting countdown...\n" + Style.RESET_ALL)
    time.sleep(1)  # Add a short pause for effect

    countdown_timer(event, total_seconds)

if __name__ == "__main__":
    main()