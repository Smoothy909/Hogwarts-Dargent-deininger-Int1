from hogwarts.utils.input_utils import *
from random import randint
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
        "money": randint(15, 40)*10  # Starting money
    }

    character = init_character(last_name, first_name, attributes)
    display_character(character)
    return character

def init_character(last_name, first_name, attributes):
    character = {
        "last_name": last_name,
        "first_name": first_name,
        "money": int(attributes["money"]),
        "inventory": [],
        "spells_learned": [],
        "Attributes": {
            "intelligence": int(attributes["intelligence"]),
            "courage": int(attributes["courage"]),
            "loyalty": int(attributes["loyalty"]),
            "ambition": int(attributes["ambition"]),
        }
    }
    return character

def display_character(character):
    print()
    print("-------Character Info-------")
    print()
    print(f"Character: {character['first_name']} {character['last_name']}")
    print(f"Money: {character['money']} Galleons")
    print("Inventory:", ", ".join(character['inventory']) if character['inventory'] else "Empty")
    print("Spells Learned:", ", ".join(character['spells_learned']) if character['spells_learned'] else "None")
    print("Attributes:")
    for attr, value in character['Attributes'].items():
        print(f"  {attr.capitalize()}: {value}")
    print()
    print("------------------------------")
    print()

def modify_money(character, amount):
    character['money'] += amount
    if character['money'] < 0:
        character['money'] = 0
    return character['money']

def add_to_inventory(character, key, item):
    if key == "inventory":
        character['inventory'].append(item)
    elif key == "spells_learned":
        character['spells_learned'].append(item)
    else:
        print(f"Invalid key: {key}. Use 'inventory' or 'spells_learned'.")
    return character

