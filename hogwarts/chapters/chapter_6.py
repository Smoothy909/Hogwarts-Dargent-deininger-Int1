from random import randint
from hogwarts.universe.house import modify_houses_points, display_winning_house
from hogwarts.utils.input_utils import ask_choice, ask_text
from hogwarts.universe.character import modify_money, add_to_inventory, display_character
import time

def duel_attack(character):
    spells_with_damage = [
        ["Wingardium Leviosa", 5],
        ["Expelliarmus", 15],
        ["Petrificus Totalus", 22],
        ["Stupefy", 27],
        ["Rictusempra", 30],
        ["Incendio", 35],
        ["Crucio", 38],
        ["Imperio", 42],
        ["Avada Kedavra", 50],
        ["Diffindo", 17],
        ["Confringo", 30],
        ["Incarcerous", 26],
    ]
    total_attr = character["Attributes"]["intelligence"] + character["Attributes"]["ambition"] + \
                 character["Attributes"]["loyalty"] + character["Attributes"]["courage"]

    attack = ask_choice("Choose a spell to cast for your attack:", [spell[0] for spell in spells_with_damage])
    for i in range(len(spells_with_damage)):
        if spells_with_damage[i][0] == str(attack):
            spell_to_use = spells_with_damage[i]
            break
    atk_val = 0
    if (spell_to_use[1] >= total_attr and spell_to_use[0] in character["spells_learned"]) or (
            spell_to_use[1] < total_attr and spell_to_use[0] not in character["spells_learned"]):
        atk_val = spell_to_use[1]
        print()
        print("you cast this spell !")
    elif spell_to_use[1] >= total_attr:
        print()
        print("You didn't manage to cast the spell")
        atk_val = 0
    elif spell_to_use[1] < total_attr and spell_to_use[0] in character["spells_learned"]:
        atk_val = spell_to_use[1] * 1.5
        print()
        print("you perfectly cast this spell !")
    return atk_val, spell_to_use[0]


def duel_defense():
    maneuvers = [
        ["Protego", 22],
        ["Duck and Counter", 32],
        ["Expelliarmus", 36],
        ["Finite Incantatem", 40],
        ["Rennervate", 25]
    ]
    defense = ask_choice("Choose a way to defend yourself :", [spell[0] for spell in maneuvers])
    for i in range(len(maneuvers)):
        if maneuvers[i][0] == str(defense):
            def_to_use = maneuvers[i]
    def_val = def_to_use[1]
    return def_val


def duel_deatheaters(character):
    print("After brewing class, you head towards the Hagrid's hut.")
    print("In the way, you encounter a group of Death Eaters attacking Hogwarts students.")
    print()
    print("Do you want to confront them?")
    time.sleep(4)
    print(
        "You don't even have the time to ask you the question that Hagrid appears behind you and pushes you into a duel against the Death Eaters!")

    input("Prepare for the duel !")
    print()
    print("--- Duel against the Death Eaters ---")
    enemies = 5
    enemy_hp = 40
    player_hp = 100
    n = 1
    victory = False
    while enemies > 0 and player_hp > 0:
        # --- Player Turn ---
        print(f"--- Round {n} ---")
        n += 1
        atk_val, atk_spell = duel_attack(character)
        enemy_def = (randint(6, 18) + randint(0, 7)) if randint(1, 3) != 2 else 0
        print(f"You cast {atk_spell} (power : {int(atk_val)}). The Deatheaters defend themselves ({enemy_def}).")
        if atk_val > enemy_def:
            print("You hit the enemy !")
            print()
            enemy_hp -= atk_val - enemy_def
            print(f"Remaining HP of the Deatheater : {enemy_hp - (atk_val - enemy_def)}")
        else:
            print("Your attack has failed.")
            print()
        if enemy_hp <= 0:
            print("You have succesfully killed a Deatheater !")
            print()
            enemies -= 1
            if enemies <= 0:
                victory = True
                break
            enemy_hp = 40

        # --- Enemy Turn ---
        def_val = duel_defense()
        enemy_attack = randint(0, 10) * 4
        print()
        print(f"a Death Eater attacks you (power : {enemy_attack}). You try to defend yourself ({def_val}).")
        if def_val > enemy_attack:
            print("You managed to defend yourself against the Death Eater’s attack.")
        else:
            hp_loss = enemy_attack - def_val
            player_hp -= hp_loss
            print(f"You take {hp_loss} points of damage. Remaining health : {player_hp}.")
            if player_hp <= 0:
                victory = False
                break
            else:
                print(f"Player Remaining health : {player_hp}.")
                print(f"Boss Remaining health : {enemy_hp}.")

    # final result of the duel
    if victory:
        print("\nVictory against the Death Eaters! You come out of it with honor.")
        modify_money(character, 50)
        character["Attributes"]["intelligence"] += 2
        add_to_inventory(character, "inventory", "Trophy of the skirmish")
    else:
        print("\nYou were forced to retreat. The Death Eaters routed you.")
        modify_money(character, -25)
        character["Attributes"]["ambition"] -= 1

    if ask_text("Press Enter to view your inventory...") == "":
        display_character(character)
        return character
    else:
        return character


def duel_astronomy_tower(character, houses):
    print()
    print("Later that evening, you receive an urgent message from Dumbledore.")
    print("He informs you that the leader of the Death Eaters has infiltrated the Astronomy Tower.")
    print("You must confront him to protect the school.")
    print()
    input("You climb the Astronomy Tower. There is a powerful mage at the top !"
          "Prepare yourself for an important duel !")
    print()
    print("--- Boss Duel in the Astronomy Tower ---")
    enemy_hp = 80
    player_hp = 100
    n = 1
    victory = False
    while enemy_hp > 0 and player_hp > 0:
        # --- Player Turn ---
        print(f"--- Round {n} ---")
        n += 1
        atk_val, atk_spell = duel_attack(character)
        enemy_def = randint(15, 35) + randint(0, 5)
        print(f"You cast {atk_spell} (power :{atk_val}). The opponent defends (value: {enemy_def}).")
        if atk_val > enemy_def:
            print(f"You hit the enemy! Remaining HP of the opponent: {enemy_hp - (atk_val - enemy_def)}")
            enemy_hp -= max(0, atk_val - enemy_def)
            if enemy_hp <= 0:
                print("The opponent is defeated!")
                victory = True
                break
        else:
            print("Your attack has failed.")

        # --- Enemy Turn ---
        def_val = duel_defense()
        enemy_attack = 4 * randint(0, 10)
        print()
        print(f"The great Wizard attacks you (power : {enemy_attack}). You try to defend yourself ({def_val}).")
        if def_val > enemy_attack:
            print()
            print("You managed to defend yourself against the Death Eater’s attack.")
        else:
            hp_loss = enemy_attack - def_val
            player_hp -= hp_loss
            print(f"You are dealt {hp_loss} points of damage. ")
            if player_hp <= 0:
                victory = False
                break
            else:
                print(f"Player Remaining health : {player_hp}.")
                print(f"Boss Remaining health : {enemy_hp}.")

    # Résultat du combat
    if victory:
        print("Victory in the Astronomy Tower !")
        input()
        print("Dumbledore will offer you 100 Galleons for your bravery and 100 points to your house.")
        modify_money(character, 100)
        modify_houses_points(houses, 100, character['house'])
        character["Attributes"]["loyalty"] += 1
        character["Attributes"]["courage"] += 1
        add_to_inventory(character, "inventory", "Astronomy Tower Token")
    else:
        print("Defeated in the Astronomy Tower. You'll face consequences.")
        print()
        print("Dumbledore deducts 50 Galleons from your funds and 50 points from your house.")
        modify_houses_points(houses, -50, character['house'])
        modify_money(character, -50)
        character["Attributes"]["courage"] -= 1

    if ask_text("Press Enter to see your inventory...") == "":
        display_character(character)
        return character, houses
    else:
        return character, houses


def half_blood_prince(character, houses):
    duel_deatheaters(character)
    duel_astronomy_tower(character, houses)

def chapter_6(character, houses):
    print()
    print("-------Chapter 6: The Duel Against the Death Eaters-------")
    print()
    print("After mastering potion brewing, you face new challenges at Hogwarts.")
    print("Dark forces threaten the school, and it's up to you to defend it.")
    print()
    half_blood_prince(character, houses)
    print()
    print(f"your house {character['house']} has {houses[character['house']]} points!")
    display_winning_house(houses)
    print()
    print("End of Chapter 6 — You've defended Hogwarts against the Death Eaters!")
    print()
    print("Thank you for playing Hogwart's Adventure! Your magical journey ends here for now.")
    input("Here is your final character status:")
    display_character(character)
    return character, houses