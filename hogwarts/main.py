from hogwarts.chapters.chapter_1 import start_chapter_1
from ..hogwarts.menus import *
def main():
    start = launch_menu()
    current_chapter = 0
    if start == "new_game":
        print("Starting a new game...")
        print()

        start_chapter_1()
        continue_game = ask_choice("Do you want to continue to the next chapter?", ["Yes (save progress)", "stop and save progress", "quit without saving"])
        if continue_game == "Yes":
            print("Continuing to the next chapter...")
            # start_chapter_2()  # Placeholder for the next chapter function
            # save_data(character, "savegame.json")  # Placeholder for save function
        else:
            print("Exiting the game. See you next time!")
            return -1


    elif launch_menu() == "load_game":
        print("Loading a saved game...")
        # Load game state here
    else:
        print("Exiting...")
        return -1

if __name__ == "__main__":
    main()
