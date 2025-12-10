from hogwarts.utils.input_utils import ask_choice
from hogwarts.universe.character import display_character, add_to_inventory, modify_money


def introduction():
    print("Welcome to Hogwarts School of Witchcraft and Wizardry!")
    input()

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
    input()
    print("REQUIRED ITEMS:")
    print("- Wands:")
    print("  1. Oak Wand - 15 Galleons")
    print("  2. Yew Wand - 25 Galleons")
    print("  3. Elder Wand - 50 Galleons")
    print("- Robes:")
    print("  1. Standard Robe - 20 Galleons")
    print("  2. Enchanted Robe - 40 Galleons")
    print("- Books:")
    print("  1. Basic Spellbook - 15 Galleons")
    print("  2. Advanced Spellbook - 30 Galleons")
    print()
    print("A PET (required):")
    print("- Owl - 80 Galleons")
    print("- Cat - 50 Galleons")
    print("- Toad - 25 Galleons")
    print()
    print("ADDITIONAL ITEMS (optional):")
    print("- Magic Quill - 5 Galleons")
    print("- tin Cauldron - 10 Galleons")
    print("- set of Copper Scales - 10 Galleons")
    print("- set of Glass or Crystal Phials - 12 Galleons")
    print("- Trunk - 22 Galleons")
    print("- Broomstick - 60 Galleons")
    print("- Invisibility Cloak - 100 Galleons")
    print()
    start = ask_choice("Do you want to start shopping?", ["Yes", "No"])
    if start == "No":
        print("You do not have a choice. You will buy the required items anyway and a cat.")
        print()
        modify_money(character, -95)
        add_to_inventory(character, "inventory", "Oak Wand")
        add_to_inventory(character, "inventory", "Standard Robe")
        add_to_inventory(character, "inventory", "Basic Spellbook")
        add_to_inventory(character, "inventory", "cat")
        input("Press enter to see your inventory and continue the story...")
        display_character(character)
        return
    else:
        while character['money'] >= 0:
            print()
            print(f"You have {character['money']} Galleons left.")
            #  ---- Wand Selection ----
            chosen_wand = ask_choice("Choose your wand:", ["Oak Wand - 10 Galleons", "Yew Wand - 15 Galleons", "Elder Wand - 50 Galleons"])
            if chosen_wand == "Oak Wand - 10 Galleons":
                modify_money(character, -10)
                chosen_wand = "Oak Wand"
            elif chosen_wand == "Yew Wand - 15 Galleons":
                modify_money(character, -15)
                chosen_wand = "Yew Wand"
            else:
                modify_money(character, -50)
                chosen_wand = "Elder Wand"
            print(f"{chosen_wand} has been added to your inventory.")
            add_to_inventory(character, "inventory", chosen_wand)

            #  ---- Robe Selection ----
            print()
            print(f"You have {character['money']} Galleons left.")
            chosen_robe = ask_choice("Choose your robe:", ["Standard Robe - 20 Galleons", "Enchanted Robe - 40 Galleons"])
            if chosen_robe == "Standard Robe - 20 Galleons":
                modify_money(character, -20)
                chosen_robe = "Standard Robe"
            else:
                modify_money(character, -40)
                chosen_robe = "Enchanted Robe"
            print(f"{chosen_robe} has been added to your inventory.")
            add_to_inventory(character, "inventory", chosen_robe)

            #  ---- Book Selection ----
            print()
            print(f"You have {character['money']} Galleons left.")
            chosen_books = ask_choice("Choose your books:", ["Basic Spellbook - 15 Galleons", "Advanced Spellbook - 30 Galleons"])
            if chosen_books == "Basic Spellbook - 15 Galleons":
                modify_money(character, -15)
                chosen_books = "Basic Spellbook"
            else:
                modify_money(character, -30)
                chosen_books = "Advanced Spellbook"
            print(f"{chosen_books} has been added to your inventory.")
            add_to_inventory(character, "inventory", chosen_books)

            #  ---- Pet Selection ----
            print()
            print(f"You have {character['money']} Galleons left.")
            chosen_pet = ask_choice("Choose your pet :",["Owl - 80 Galleons", "Cat - 50 Galleons", "Toad - 30 Galleons"])
            if chosen_pet == "Owl - 80 Galleons":
                modify_money(character, -80)
                chosen_pet = "Basic Spellbook"
            elif chosen_pet == "Cat - 50 Galleons":
                modify_money(character, -50)
                chosen_pet = "Cat"
            else:
                modify_money(character, -30)
                chosen_pet = "Toad"
            print(f"{chosen_pet} has been added to your inventory.")
            add_to_inventory(character, "inventory", chosen_books)

            # ---- Additional Items ----
            print()
            print(f"You have bought all required items! You still have {character['money']} Galleons left.")
            print()
            continue_eventuality = True
            while continue_eventuality:
                continue_shopping = ask_choice("Do you want to continue shopping?", ["Yes", "No"])
                if continue_shopping == "Yes":

                    if character['money'] < 5:
                        print()
                        print("You do not have enough money to buy any additional items.")
                        print()
                        continue_eventuality = False

                    print()
                    print(f"You have {character['money']} Galleons left.")
                    print()
                    available_items = ["Magic Quill - 5 Galleons", "tin Cauldron - 10 Galleons", "set of Copper Scales - 10 Galleons", "set of Glass or Crystal Phials - 12 Galleons", "Trunk - 22 Galleons", "Broomstick - 60 Galleons", "Invisibility Cloak - 100 Galleons"]
                    item = ask_choice("Which item do you want to buy?", available_items)
                    if item == "Magic Quill - 5 Galleons":
                        price = 5
                        item = "Magic Quill"
                    elif item == "tin Cauldron - 10 Galleons":
                        price = 10
                        item = "tin Cauldron"
                    elif item == "set of Copper Scales - 10 Galleons":
                        price = 10
                        item = "set of Copper Scales"
                    elif item == "set of Glass or Crystal Phials - 12 Galleons":
                        price = 12
                        item = "set of Glass or Crystal Phials"
                    elif item == "Trunk - 22 Galleons":
                        price = 22
                        item = "Trunk"
                    elif item == "Broomstick - 60 Galleons":
                        price = 60
                        item = "Broomstick"
                    elif item == "Invisibility Cloak - 100 Galleons":
                        price = 100
                        item = "Invisibility Cloak"
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
                    return character

    print(f"You have finished your shopping with {character['money']} Galleons.")
    return character

def add_items_attributes(character):
    for item in character['inventory']:
        if item == "Oak Wand":
            character["Attributes"]["ambition"] += 1
        elif item == "Yew Wand":
            character["Attributes"]["ambition"] += 2
        elif item == "Elder Wand":
            character["Attributes"]["ambition"] += 5

        elif item == "Standard Robe":
            character["Attributes"]["loyalty"] += 1
        elif item == "Enchanted Robe":
            character["Attributes"]["loyalty"] += 2

        elif item == "Basic Spellbook":
            character["Attributes"]["intelligence"] += 2
        elif item == "Advanced Spellbook":
            character["Attributes"]["intelligence"] += 3


        elif item == "Magic Quill":
            character["Attributes"]["intelligence"] += 1
        elif item == "tin Cauldron":
            character["Attributes"]["intelligence"] += 1
        elif item == "set of Copper Scales":
            character["Attributes"]["intelligence"] += 1
        elif item == "set of Glass or Crystal Phials":
            character["Attributes"]["intelligence"] += 1
        elif item == "Trunk":
            character["Attributes"]["loyalty"] += 1
        elif item == "Broomstick":
            character["Attributes"]["courage"] += 2
        elif item == "Invisibility Cloak":
            character["Attributes"]["courage"] += 3

        elif item == "Owl":
            character["Attributes"]["intelligence"] += 2
        elif item == "Cat":
            character["Attributes"]["loyalty"] += 2
        elif item == "Toad":
            character["Attributes"]["courage"] += 1
    return character

# Chapter 1 Flow
def start_chapter_1(character):
        introduction()
        accepted = receive_welcome_letter(character)
        if accepted == "Yes":
            meet_hagrid(character)
            buy_supplies(character)
            print("Congratulations! You have completed Chapter 1 and are ready to start your journey at Hogwarts!")
            character = add_items_attributes(character)
            display_character(character)
        else:
            print("You have chosen not to attend Hogwarts. The game will now end.")

        return character
