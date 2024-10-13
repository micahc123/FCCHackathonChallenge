import random
import time
import os
from colorama import init, Fore, Style
import re

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_answer):
        self.questions.append(Question(question, options, correct_answer))

    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.ask_question(question)
        return self.score

    def ask_question(self, question):
        animate_text(question.question, color=Fore.CYAN)
        for i, option in enumerate(question.options):
            animate_text(f"{chr(65 + i)}. {option}", color=Fore.YELLOW)
        
        user_answer = self.get_user_answer(len(question.options))
        if user_answer == question.correct_answer:
            self.score += 1
            animate_text("Correct!", color=Fore.GREEN)
        else:
            animate_text(f"Sorry, that's incorrect. The correct answer was {question.correct_answer}.", color=Fore.RED)
        time.sleep(1)

    def get_user_answer(self, num_options):
        while True:
            user_input = input(Fore.MAGENTA + "Your answer (A, B, C, ...): " + Style.RESET_ALL).strip().upper()
            if len(user_input) == 1 and ord(user_input) - ord('A') in range(num_options):
                return user_input
            animate_text("Invalid input. Please enter a valid option.", color=Fore.RED)

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
    ██████╗ ██╗   ██╗██╗███████╗    ████████╗██╗███╗   ███╗███████╗██╗
    ██╔══██╗██║   ██║██║╚══███╔╝    ╚══██╔══╝██║████╗ ████║██╔════╝██║
    ██████╔╝██║   ██║██║  ███╔╝        ██║   ██║██╔████╔██║█████╗  ██║
    ██╔═══╝ ██║   ██║██║ ███╔╝         ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
    ██║     ╚██████╔╝██║███████╗       ██║   ██║██║ ╚═╝ ██║███████╗██╗
    ╚═╝      ╚═════╝ ╚═╝╚══════╝       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝
    """
    print(Fore.CYAN + Style.BRIGHT + title + Style.RESET_ALL)

def get_feedback(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage == 100:
        return "Perfect score! You're a quiz master!", Fore.GREEN
    elif percentage >= 66:
        return "Great job! You did well!", Fore.YELLOW
    elif percentage >= 33:
        return "Not bad, but there's room for improvement.", Fore.MAGENTA
    else:
        return "Looks like you need to study more. Keep trying!", Fore.RED

def main():
    quiz = Quiz()

    # Add questions
    quiz.add_question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "C")
    quiz.add_question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "A")
    quiz.add_question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "B")

    clear_screen()
    display_title()
    animate_text("Welcome to the Quiz Time!", color=Fore.GREEN)
    animate_text("You will be asked 3 multiple-choice questions.", color=Fore.CYAN)
    animate_text("Let's begin!\n", color=Fore.YELLOW)
    time.sleep(1)

    score = quiz.run_quiz()
    total_questions = len(quiz.questions)

    clear_screen()
    display_title()
    animate_text(f"\nYour final score: {score}/{total_questions}", color=Fore.CYAN)
    
    feedback, feedback_color = get_feedback(score, total_questions)
    animate_text(feedback, color=feedback_color)

    animate_text("\nThanks for playing Quiz Time!", color=Fore.GREEN)

if __name__ == "__main__":
    main()