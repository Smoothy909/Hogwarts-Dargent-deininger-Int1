from hogwarts.utils.input_utils import *
from hogwarts.universe.house import *
from hogwarts.universe.character import *

def launch_menu():
    while True:
        choice = ask_choice("Main Menu - Choose an option:", ["Start New Game", "Exit"])
        if choice == "Start New Game":
            return "new_game"
        elif choice == "Exit":
            return "exit"

def run_chapter(chapter_nuber, character, houses):
    if chapter_nuber == 1:
        from hogwarts.chapters.chapter_1 import chapter_1
        chapter_1(character)
    elif chapter_nuber == 2:
        from hogwarts.chapters.chapter_2 import chapter_2
        chapter_2(character)
    elif chapter_nuber == 3:
        from hogwarts.chapters.chapter_3 import chapter_3
        chapter_3(character, houses)
    elif chapter_nuber == 4:
        from hogwarts.chapters.chapter_4 import chapter_4
        chapter_4(character, houses)
    elif chapter_nuber == 5:
        from hogwarts.chapters.chapter_5 import chapter_5
        chapter_5(character, houses)
    elif chapter_nuber == 6:
        from hogwarts.chapters.chapter_6 import chapter_6
        chapter_6(character, houses)
    return