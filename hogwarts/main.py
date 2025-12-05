from hogwarts.menus import launch_menu, run_chapter
from hogwarts.utils.input_utils import ask_choice
from hogwarts.universe.character import create_character


def main():
    start = launch_menu()

    # ---- DBUG ----
    skip_for_test = ask_choice("normal play or test mode?", ["normal play", "test mode"])

    if start == "new_game":
        print("Starting a new game...")
        print()
        current_chapter = 0
        character = create_character()
        while current_chapter < 5:
            print()
            if skip_for_test == "normal play":
                continue_game = ask_choice("Do you want to continue to the next chapter?", ["Yes (save progress)", "stop and save progress", "quit without saving"])
                if continue_game == "Yes (save progress)":
                    current_chapter += 1
                    print()
                    input("Press Enter to continue to the next chapter...")
                    run_chapter(current_chapter, character)
                else:
                    print("Exiting the game. See you next time!")
                    return -1
            else:
                chapter_to_test = ask_choice("Select chapter to test:", ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5"])
                current_chapter = int(chapter_to_test.split()[-1])
                if chapter_to_test == "Chapter 4":
                    character['house'] = 'Gryffindor'  # Ensure character has a house for chapter 4
                    print('assigned to gryffindor by default')
                run_chapter(current_chapter, character)
                return 'test complete'


    elif start == "load_game":
        print("Loading a saved game...")
        # Load game state here
        return -1
    else:
        print("Exiting...")
        return -1

if __name__ == "__main__":
    main()
