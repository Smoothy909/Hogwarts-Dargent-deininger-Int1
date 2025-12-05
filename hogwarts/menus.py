from hogwarts.utils.input_utils import *
from hogwarts.universe.house import *
from hogwarts.universe.character import *


def display_menu():
    ask_choice("Welcome to Hogwarts! Please choose an option:", ["1. Start New Game", "2. Load Game", "3. Exit"])
    return
def launch_menu():
    houses = {
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

def run_chapter(chapter_nuber, character):
    if chapter_nuber == 1:
        from hogwarts.chapters.chapter_1 import start_chapter_1
        start_chapter_1(character)
    elif chapter_nuber == 2:
        from hogwarts.chapters.chapter_2 import chapter_2
        chapter_2(character)
    elif chapter_nuber == 3:
        from hogwarts.chapters.chapter_3 import chapter_3
        chapter_3(character)
    elif chapter_nuber == 4:
        from hogwarts.chapters.chapter_4 import chapter_4
        chapter_4(character)
    elif chapter_nuber == 5:
        from hogwarts.chapters.chapter_5_extension import chapter_5
        chapter_5(character)
    return