from ..hogwarts.utils.input_utils import *
from ..hogwarts.universe.house import *
from ..hogwarts.universe.character import *


def display_menu():
    ask_choice("Welcome to Hogwarts! Please choose an option:", ["1. Start New Game", "2. Load Game", "3. Exit"])
    return
def launch_menu():
    houses_points = {
        "Gryffindor": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0,
        "Slytherin": 0
    }
    while True:
        choice = ask_choice("Main Menu - Choose an option:", ["Start New Game", "Load Game", "Exit"])
        if choice == "Start New Game":
            return "new_game"
        elif choice == "Load Game":
            return "load_game"
        elif choice == "Exit":
            return "exit"

