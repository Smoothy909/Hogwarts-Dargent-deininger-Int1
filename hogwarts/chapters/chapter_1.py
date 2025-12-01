from hogwarts.utils.input_utils import ask_text, ask_number, ask_choice
from hogwarts.universe.character import init_character, display_character, add_to_inventory, modify_money

def introduction():
    print("Welcome to Hogwarts School of Witchcraft and Wizardry!")
    ### A modifier ici pour l'introduction ###
    input("Press Enter to continue...")

def create_character():


    print("Let's create your character!")
    first_name = ask_text("Enter your first name: ")
    last_name = ask_text("Enter your last name: ")

    print("Distribute 30 points among the following attributes:")
    intelligence = ask_number("Intelligence (0-10): ")
    courage = ask_number("Courage (0-10): ")
    loyalty = ask_number("Loyalty (0-10): ")
    ambition = ask_number("Ambition (0-10): ")

    total_points = intelligence + courage + loyalty + ambition

    while total_points > 30:
        print("You have allocated more than the maximum amount of points. Please redistribute your points.")
        intelligence = ask_number("Intelligence (0-10): ")
        courage = ask_number("Courage (0-10): ")
        loyalty = ask_number("Loyalty (0-10): ")
        ambition = ask_number("Ambition (0-10): ")
        total_points = intelligence + courage + loyalty + ambition

    attributes = {
        "intelligence": intelligence,
        "courage": courage,
        "loyalty": loyalty,
        "ambition": ambition,
        "money": 100  # Starting money
    }

    character = init_character(last_name, first_name, attributes)
    display_character(character)
    return character

def receive_welcome_letter(character):
    print(f"Dear {character['first_name']} {character['last_name']},")
    print("We are pleased to inform you that you have been accepted to Hogwarts School of Witchcraft and Wizardry.")
    print("Please find enclosed a list of all necessary books and equipment.")
    print("Term begins on September 1st. We await your owl by no later than July 31st.")
    print("Yours sincerely,")
    print("Minerva McGonagall")
    print("Deputy Headmistress")
    ans = ask_choice("Do you accept to go to Hogwarts", ["Yes", "No"])
    if ans == "Yes":
        print("Great! Let's get started on your magical journey!")
    else:
        print("We're sorry to hear that. Maybe next time!")
    return ans

def meet_hagrid(character):
    print(f"Hello {character['first_name']}! I'm Rubeus Hagrid, Keeper of Keys and Grounds at Hogwarts.")
    print("I'll be helping you get to Hogwarts. Let's go to Diagon Alley to get your supplies!")
    accept = ask_choice("Are you ready to go to Diagon Alley?", ["Yes", "No"])
    if accept == "Yes" :
        print("Fantastic! Let's get your wand and other supplies.")
    else :
        print("Hagrid takes you by the hand and leads you to Diagon Alley anyway.")
    return

def buy_supplies(character):
    print("Welcome to Diagon Alley! Here you can buy all your magical supplies.")
    print(f"You have {character['money']} Galleons to spend.")
    print("You have to buy a wand, a robe, and some books.")
    input("Press enter to continue...")
    print("Here are a list of what you can buy:")
    print("REQUIRED ITEMS:")
    print("- Wands:")
    print("  1. Oak Wand - 10 Galleons")
    print("  2. Yew Wand - 15 Galleons")
    print("  3. Elder Wand - 50 Galleons")
    print("- Robes:")
    print("  1. Standard Robe - 20 Galleons")
    print("  2. Enchanted Robe - 40 Galleons")
    print("- Books:")
    print("  1. Basic Spellbook - 15 Galleons")
    print("  2. Advanced Spellbook - 30 Galleons")
    print("ADDITIONAL ITEMS (optional):")
    print("- tin Cauldron - 10 Galleons")
    print("- set of Glass or Crystal Phials - 5 Galleons")
    print("- telescope - 20 Galleons")
    print("- set of Brass Scales - 15 Galleons")
    print("- Trunk - 25 Galleons")
    print("- Broomstick - 60 Galleons")
    print("- potions ingredients - 5 Galleons each")
    print("A PET (optional):")
    print("- Owl - 100 Galleons")
    print("- Cat - 50 Galleons")
    print("- Toad - 25 Galleons")
    print()
    start = ask_choice("Do you want to start shopping?", ["Yes", "No"])
    if start == "No":
        print("You do not have a choice. You buy the required items anyway.")
        modify_money(character, -45)
        add_to_inventory(character, "inventory", "Oak Wand")
        add_to_inventory(character, "inventory", "Standard Robe")
        add_to_inventory(character, "inventory", "Basic Spellbook")
        input("Press enter to see your inventory")
        display_character(character)
        return
    else:
        while character['money'] >= 0:
            print(f"You have {character['money']} Galleons left.")
            wand_options = ["Oak Wand - 10 Galleons", "Yew Wand - 15 Galleons", "Elder Wand - 50 Galleons"]
            chosen_wand = ask_choice("Choose your wand:", wand_options)
            if chosen_wand == "Oak Wand - 10 Galleons":
                modify_money(character, -10)
                chosen_wand = "Oak Wand"
            elif chosen_wand == "Yew Wand - 15 Galleons":
                modify_money(character, -15)
                chosen_wand = "Yew Wand"
            else:
                modify_money(character, -50)
                chosen_wand = "Elder Wand"
            add_to_inventory(character, "inventory", chosen_wand)


            print(f"You have {character['money']} Galleons left.")
            robe_options = ["Standard Robe - 20 Galleons", "Enchanted Robe - 40 Galleons"]
            chosen_robe = ask_choice("Choose your robe:", robe_options)
            if chosen_robe == "Standard Robe - 20 Galleons":
                modify_money(character, -20)
                chosen_robe = "Standard Robe"
            else:
                modify_money(character, -40)
                chosen_robe = "Enchanted Robe"
            add_to_inventory(character, "inventory", chosen_robe)


            print(f"You have {character['money']} Galleons left.")
            books_options = ["Basic Spellbook - 15 Galleons", "Advanced Spellbook - 30 Galleons"]
            chosen_books = ask_choice("Choose your books:", books_options)
            if chosen_books == "Basic Spellbook - 15 Galleons":
                modify_money(character, -15)
                chosen_books = "Basic Spellbook"
            else:
                modify_money(character, -30)
                chosen_books = "Advanced Spellbook"
            add_to_inventory(character, "inventory", chosen_books)


            print()
            print()
            print(f"You have {character['money']} Galleons left.")
            continue_shopping = ask_choice("Do you want to continue shopping?", ["Yes", "No"])
            if continue_shopping == "Yes":
                print("You can continue shopping for additional items.")

                if character['money'] < 5:
                    print()
                    print("You do not have enough money to buy any additional items.")
                    print()
                    break

                nb_other_items= ask_number("Out of the other items (cauldron, phials, telescope, brass scales, trunk, broomstick, PET(only 1), how many additional items do you want to buy? ")
                for i in range(nb_other_items):
                    item = ask_choice("Which item do you want to buy?", ["tin Cauldron - 10 Galleons", "set of Glass or Crystal Phials - 5 Galleons", "telescope - 20 Galleons", "set of Brass Scales - 15 Galleons", "Trunk - 25 Galleons", "Broomstick - 60 Galleons", "Owl - 100 Galleons", "Cat - 50 Galleons", "Toad - 25 Galleons", "potions ingredients - 5 Galleons each"])
                    if item == "tin Cauldron - 10 Galleons":
                        price = 10
                        item = "tin Cauldron"
                    elif item == "set of Glass or Crystal Phials - 5 Galleons":
                        price = 5
                        item = "set of Glass or Crystal Phials"
                    elif item == "telescope - 20 Galleons":
                        price = 20
                        item = "telescope"
                    elif item == "set of Brass Scales - 15 Galleons":
                        price = 15
                        item = "set of Brass Scales"
                    elif item == "Trunk - 25 Galleons":
                        price = 25
                        item = "Trunk"
                    elif item == "Broomstick - 60 Galleons":
                        price = 60
                        item = "Broomstick"
                    elif item == "Owl - 100 Galleons":
                        price = 100
                        item = "Owl"
                    elif item == "Cat - 50 Galleons":
                        price = 50
                        item = "Cat"
                    elif item == "Toad - 25 Galleons":
                        price = 25
                        item = "Toad"
                    else:
                        price = 5
                        item = "potions ingredients"

                    if character['money'] >= price:
                        modify_money(character, -price)
                        add_to_inventory(character, "inventory", item)
                        print(f"You have bought {item}.")
                        print(f"You have {character['money']} Galleons left.")
                    else:
                        print("Thy have been too greedy! To pay for your crime, thy shall end your compulsive habit.")
                        print("We will now delete sys32... Just kidding! You do not have enough money to buy this item.")
                        break
            else:
                print("You have chosen to stop shopping.")
                break
    print(f"You have finished your shopping with {character['money']} Galleons.")
    input("Press enter to see your inventory and continue...")
    display_character(character)

    # Chapter 1 Flow
def start_chapter_1():
        introduction()
        character = create_character()
        accepted = receive_welcome_letter(character)
        if accepted == "Yes":
            meet_hagrid(character)
            buy_supplies(character)
            print("Congratulations! You have completed Chapter 1 and are ready to start your journey at Hogwarts!")
        else:
            print("You have chosen not to attend Hogwarts. The game will now end.")

        return character

start_chapter_1()