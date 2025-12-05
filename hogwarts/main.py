from hogwarts.chapters.chapter_1 import start_chapter_1
from hogwarts.chapters.chapter_4 import chapter_4
from hogwarts.menus import launch_menu
from hogwarts.utils.input_utils import ask_choice
from hogwarts.universe.character import create_character


def main():
    start = launch_menu()
    current_chapter = 0
    if start == "new_game":
        print("Starting a new game...")
        character = create_character()
        print()

        start_chapter_1()
        continue_game = ask_choice("Do you want to continue to the next chapter?", ["Yes (save progress)", "stop and save progress", "quit without saving"])
        if continue_game == "Yes (save progress)":
            current_chapter = 1
            input("Press Enter to continue to the next chapter...")
            chapter_4(character)
        else:
            print("Exiting the game. See you next time!")
            return -1


    elif launch_menu() == "load_game":
        print("Loading a saved game...")
        # Load game state here
        return -1
    else:
        print("Exiting...")
        return -1

if __name__ == "__main__":
    main()
