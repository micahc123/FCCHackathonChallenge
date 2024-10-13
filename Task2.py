import random
import string
import time
import os
from colorama import init, Fore, Style
import re

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

#classes for story generation and elemenst
class StoryElement:
    def __init__(self, category, content):
        self.category = category
        self.content = content

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class StoryGenerator:
    def __init__(self):
        self.characters = []
        self.settings = []
        self.events = []
        self.plot_structures = []

    def add_element(self, category, content):
        element = StoryElement(category, content)
        if category == "setting":
            self.settings.append(element)
        elif category == "event":
            self.events.append(element)
        elif category == "plot_structure":
            self.plot_structures.append(element)

    def add_character(self, name, role):
        character = Character(name, role)
        self.characters.append(character)

    def generate_story(self):
        if not self.characters or not self.settings or not self.events or not self.plot_structures:
            return "Not enough elements to generate a story."

        plot = random.choice(self.plot_structures)
        setting = random.choice(self.settings)
        main_character = random.choice(self.characters)
        supporting_character = random.choice([c for c in self.characters if c != main_character])
        event1, event2 = random.sample(self.events, 2)

        story = f"{plot.content}\n\n"
        story += f"In a {setting.content}, {main_character.name} the {main_character.role} lived a quiet life. "
        story += f"One day, {event1.content} This unexpected turn of events brought {main_character.name} face to face with {supporting_character.name} the {supporting_character.role}. "
        story += f"Together, they headed to {event2.content} "
        story += f"In the end, {main_character.name} learned a valuable lesson about life and friendship."

        return story

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def animate_text(text, delay=0.03, color=Fore.WHITE):
    text = strip_ansi_codes(text)
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def display_title():
    title = """
    ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗    ███████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
    ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
    ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║    ███████╗   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
    ██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║    ╚════██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
    ██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║    ███████║   ██║   ╚██████╔╝██║  ██║   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
    """
    print(Fore.CYAN + Style.BRIGHT + title + Style.RESET_ALL)

def get_user_input(prompt):
    while True:
        user_input = input(Fore.YELLOW + prompt + Style.RESET_ALL).strip()
        if user_input and all(c.isalpha() or c.isspace() for c in user_input):
            return string.capwords(user_input)
        animate_text("Invalid input. Please use only letters and spaces.", color=Fore.RED)

def main():
    generator = StoryGenerator()

    # Add predefined elements
    generator.add_element("setting", "bustling city")
    generator.add_element("setting", "quiet village")
    generator.add_element("setting", "mysterious forest")
    generator.add_element("event", "a strange artifact appeared in the local museum.")
    generator.add_element("event", "an ancient prophecy began to unfold.")
    generator.add_element("event", "a long-lost relative and returned with a secret.")
    generator.add_element("event", "they saw an age-old mystery that had puzzled the town for generations.")
    generator.add_element("event", "embark on a perilous journey to save their home from an impending disaster.")
    generator.add_element("plot_structure", "It was a time of great change...")
    generator.add_element("plot_structure", "In a world where nothing was as it seemed...")
    generator.add_element("plot_structure", "Fate had a curious way of bringing people together...")

    clear_screen()
    display_title()
    animate_text("Welcome to the Random Story Generator!", color=Fore.GREEN)
    animate_text("Please enter names for the characters in your story.", color=Fore.CYAN)

    main_character_name = get_user_input("Enter the name of the main character: ")
    supporting_character_name = get_user_input("Enter the name of the supporting character: ")

    generator.add_character(main_character_name, "adventurer")
    generator.add_character(supporting_character_name, "local guide")

    animate_text("\nGenerating your unique story...\n", color=Fore.MAGENTA)
    time.sleep(1)  # Add a short pause for effect

    story = generator.generate_story()
    
    # Split the story into sentences and animate each one
    sentences = story.split('. ')
    for sentence in sentences:
        animate_text(sentence + '.', delay=0.05, color=Fore.WHITE)
        time.sleep(0.5)  # Add a short pause between sentences

    animate_text("\nThe End", color=Fore.GREEN)

if __name__ == "__main__":
    main()