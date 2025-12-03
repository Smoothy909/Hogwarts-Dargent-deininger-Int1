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

