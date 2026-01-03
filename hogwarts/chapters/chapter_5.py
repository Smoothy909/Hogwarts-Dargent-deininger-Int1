from hogwarts.utils.input_utils import load_file_content
from random import randint
from hogwarts.utils.input_utils import ask_choice, ask_text
from hogwarts.universe.character import display_character
from hogwarts.universe.house import initialize_houses, modify_houses_points, display_winning_house


def potion_minigame(character, houses):
    print("⋆₊ ⊹★ 🧪⭑⋆｡˚")
    print("The brewing class is about to start!")
    print("Today, you'll be brewing 3 potions.")

    available_potions = load_file_content("hogwarts/data/potions.json")

    potions_to_brew = [available_potions[randint(1, 7)] for _ in range(3)]
    all_ingredients = set()
    for potion in available_potions:
        for ingredient in potion.get("ingredients", []):
            all_ingredients.add(ingredient)
    all_ingredients = list(all_ingredients)
    print()
    print("You will need to identify each potion by name and then provide one ingredient.")
    input("Press Enter to begin...")
    success_count = 0

    for potion in potions_to_brew:
        expected_name = potion.get("potion")
        hint = potion.get("effects")
        if hint:
            print(f"Hint: {hint}")

        user_name = ask_text("What is the name of this potion? ")
        if user_name.lower() == expected_name.lower():

            print("Correct name!")
            success_count+= 1
            print()
            print("here are the ingredients in the potion:")
            ingredients = potion.get("ingredients", [])
            for i in range(1, len(ingredients)):
                print(f"- {ingredients[i]}")
            print("- ... ")
            print()
            user_ingredient = ask_choice(f"We are missing an ingredient! \n Enter the last ingredient of {expected_name}: ",[ingredients[0], all_ingredients[randint(1,len(all_ingredients)-1)], all_ingredients[randint(1,len(all_ingredients)-1)], all_ingredients[randint(1,len(all_ingredients)-1)]])
            if user_ingredient== ingredients[0]:
                print(f"Well done! {user_ingredient} is indeed the last ingredient of {expected_name}.")
                if randint(1,2) == 1:
                    character["Attributes"]["courage"] += 1
                else:
                    character["Attributes"]["loyalty"] += 1
                houses=initialize_houses()
                modify_houses_points(houses,10, character['house'])
            else:
                print(f"Wrong ingredient. The correct ingredient was: {ingredients[0]}.")
        else:
            print(f"Wrong name. The correct name was: {expected_name}.")
        print()

    for j in range(success_count):
        character["Attributes"]["intelligence"] += 1
        character["Attributes"]["ambition"] += 1
        character["money"] += 5

        modify_houses_points(houses,31,character['house'])
    all_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    all_houses.pop(all_houses.index(character['house']))
    for i in range(len(all_houses)):
        modify_houses_points(houses, 20 * randint(0, 3), all_houses[i])

    print(f"your house {character['house']} has {houses[character['house']]} points!")
    print()
    print(f"You successfully brewed {success_count} out of 3 potions.")
    print()
    if ask_text("Press Enter to view your inventory...") == "":
        display_character(character)
        return character
    else :
        return character

def chapter_5(character, houses):
    print()
    print("-------Chapter 5: The Potion Brewing Minigame-------")
    print()
    print("Welcome to your first Potion Brewing class at Hogwarts!")
    print()
    potion_minigame(character, houses)
    display_winning_house(houses)
    print()
    print ("End of Chapter 5 — You've taken your first steps into the world of potion brewing!")
    return character, houses
