from hogwarts.menus import launch_menu, run_chapter
from hogwarts.universe.house import initialize_houses
from hogwarts.utils.input_utils import ask_choice
from hogwarts.universe.character import create_character


def main():
    start = launch_menu()

    # ---- DEBUG ----
    debug_mode = ask_choice("normal play or test mode?", ["normal play", "test mode"])

    if start == "new_game":
        print("Starting a new game...")
        print()
        current_chapter = 0
        houses = initialize_houses()
        character = create_character()
        while current_chapter <= 5:
            print()
            if debug_mode == "normal play":
                if current_chapter == 0:
                    current_chapter = 1
                    run_chapter(current_chapter, character, houses)
                else:
                    continue_game = ask_choice("Do you want to continue to the next chapter?", ["Yes", "No"])
                    if continue_game == "Yes":
                        current_chapter += 1
                        print()
                        input("Press Enter to continue to the next chapter...")
                        run_chapter(current_chapter, character, houses)
                    else:
                        print("Exiting the game. See you next time!")
                        return -1
            else:
                chapter_to_test = ask_choice("Select chapter to test:", ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6"])
                current_chapter = int(chapter_to_test.split()[-1])
                if chapter_to_test == "Chapter 4" or chapter_to_test == "Chapter 3" or chapter_to_test == "Chapter 5":
                    character['house'] = 'Gryffindor'  # Ensure character has a house for chapter
                    print('assigned to gryffindor by default')
                    run_chapter(current_chapter, character, houses)
                    return 'test complete'
                else:
                    run_chapter(current_chapter, character, houses)
                    return 'test complete'

    else:
        print("Exiting...")
        return -1

if __name__ == "__main__":
    main()
