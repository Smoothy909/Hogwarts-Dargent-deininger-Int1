from hogwarts.utils.input_utils import load_file_content
from random import randint
from hogwarts.utils.input_utils import ask_choice, ask_text
from hogwarts.universe.character import modify_money, add_to_inventory, display_character


def potion_minigame(character):
    print("The brewing class is about to start!")
    print("Today, you'll be brewing 3 potions.")

    available_potions = load_file_content("hogwarts/data/potions.json")

    potions_to_brew = [available_potions[randint(1, 7)] for _ in range(3)]
    all_ingredients = set()
    for potion in available_potions:
        for ingredient in potion.get("ingredients", []):
            all_ingredients.add(ingredient)
    all_ingredients = list(all_ingredients)
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
            user_ingredient = ask_choice(f"We are missing an ingredient! \n Enter the last ingredient of {expected_name}: ",[ingredients[0], all_ingredients[randint(1,len(all_ingredients))], all_ingredients[randint(1,len(all_ingredients))], all_ingredients[randint(1,len(all_ingredients))]])
            if user_ingredient== ingredients[0]:
                print(f"Well done! {user_ingredient} is indeed an ingredient of {expected_name}.")
                if randint(1,2) == 1:
                    character["Attributes"]["courage"] += 1
                else:
                    character["Attributes"]["loyalty"] += 1
            else:
                print(f"Wrong ingredient. The correct ingredient was: {ingredients[0]}.")
        else:
            print(f"Wrong name. The correct name was: {expected_name}.")
        print()

    for j in range(success_count):
        character["Attributes"]["intelligence"] += 1
        character["Attributes"]["ambition"] += 1
        character["money"] += 5
    print(f"You successfully brewed {success_count} out of 3 potions.")
    print()
    if ask_text("Appuyez sur Entrée pour voire votre inventaire...") == "":
        display_character(character)
        return character
    else :
        return character


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
    total_attr = character["Attributes"]["intelligence"] + character["Attributes"]["ambition"] + character["Attributes"]["loyalty"] + character["Attributes"]["courage"]

    attack = ask_choice("Choose a spell to cast for your attack:", [spell[0] for spell in spells_with_damage])
    for i in range(len(spells_with_damage)):
        if spells_with_damage[i][0] == str(attack):
            spell_to_use = spells_with_damage[i]
            break

    if (spell_to_use[1] >= total_attr and spell_to_use[0] in character["spells_learned"]) or (spell_to_use[1] < total_attr and spell_to_use[0] not in character["spells_learned"]):
        spell_to_use[1] = spell_to_use[1]
        print("you cast this spell !")
    elif spell_to_use[1] >= total_attr:
        print("You didn't manage to cast the spell")
        spell_to_use[1] = 0
    elif spell_to_use[1] < total_attr and spell_to_use[0] in character["spells_learned"]:
        spell_to_use[1] = spell_to_use[1]*1.5
        print("you perfectly cast this spell !")
    else:
        spell_to_use[1] = 0
        return spell_to_use
    return spell_to_use[1], spell_to_use[0]

def duel_defense(character):
    maneuvers = [
        ["Protego", 22],
        ["Duck and Counter", 32],
        ["Expelliarmus", 36],
        ["Finite Incantatem", 40],
        ["Rennervate", 25]
    ]
    total_attr = character["Attributes"]["intelligence"] + character["Attributes"]["ambition"] + character["Attributes"]["loyalty"] + character["Attributes"]["courage"]

    defense = ask_choice("Choose a way to defend yourself :", [spell[0] for spell in maneuvers])
    for i in range(len(maneuvers)):
        if maneuvers[i][0] == str(defense):
            def_to_use = maneuvers[i]
            break

    if def_to_use[1] >= total_attr:
        taken_coeff = 1
    else:
        taken_coeff = 0

    return taken_coeff



def duel_deatheaters(character):
    print()
    input("You fall upon an aggressive deatheater group. Prepare for the duel !")
    print()
    enemies = 5
    enemy_hp = 40
    player_hp = 100
    while enemies > 0 and player_hp > 0:
        # --- Player Turn ---
        atk_val, atk_spell = duel_attack(character)
        enemy_def = (randint(6, 18) + randint(0, 7)) if randint(1,3) != 2 else 0
        print(f"You cast {atk_spell} (power : {int(atk_val)}). The Deatheaters defend themselves ({enemy_def}).")
        if atk_val > enemy_def:
            print("Vous touchez l'ennemi !")
            enemy_hp -= atk_val - enemy_def

            if enemy_hp <= 0:
                print("You have succesfully killed a Deatheater !")
                enemies -= 1
                enemy_hp = 40
        else:
            print("Votre attaque a échoué.")

        # --- Enemy Turn ---
        damage_coeff = duel_defense(character)
        if damage_coeff == 0:
            print("Vous avez réussi à vous défendre contre l'attaque du Mangemort.")
        else:
            enemy_attack = randint(10, 25) + randint(0, 5)
            print(f"Un Mangemort attaque avec une puissance de {enemy_attack}.")
            player_hp -= enemy_attack
            print(f"Vous subissez {enemy_attack} points de dégâts. Points de vie restants : {player_hp}.")
        if enemies <= 0:
            victory = True
            break
        if player_hp <= 0:
            victory = False
            break

    # Résultat final
    if victory:
        print("\nVictoire contre les Mangemorts ! Vous vous en sortez honorablement.")
        modify_money(character, 50)
        character["Attributes"]["intelligence"] += 2
        add_to_inventory(character, "inventory", "Trophy of the skirmish")
    else:
        print("\nVous avez dû battre en retraite. Les Mangemorts vous ont mis en déroute.")
        modify_money(character, -25)
        character["Attributes"]["ambition"] -= 1

    if ask_text("Appuyez sur Entrée pour voire votre inventaire...") == "":
        display_character(character)
        return character
    else :
        return character


def duel_astronomy_tower(character):
    print()
    input("Vous montez dans la Tour d'Astronomie. Préparez-vous à un duel important !")
    print()
    ennemy_hp = 60
    player_hp = 100
    while ennemy_hp > 0 and player_hp > 0:
        # --- Player Turn ---
        atk_val, atk_spell = duel_attack(character)
        enemy_def = randint(5, 15) + randint(0, 4) if randint(1,5) != 2 else 0
        print(f"Vous lancez {atk_spell} (puissance {atk_val}). L'adversaire se défend ({enemy_def}).")
        if atk_val > enemy_def:
            print("Vous touchez l'ennemi !")
            ennemy_hp -= max(0, atk_val - enemy_def)
            if ennemy_hp <= 0:
                print("L'adversaire est vaincu !")
                victory = True
                break
        else:
            print("Votre attaque a échoué.")

        # --- Enemy Turn ---
        damage_coeff = duel_defense(character)
        if damage_coeff == 0:
            print("Vous avez réussi à vous défendre contre l'attaque de l'adversaire.")
        else:
            enemy_attack = randint(10, 30) + randint(0, 5)
            print(f"Your opponent attacks with a power of {enemy_attack}.")
            player_hp -= enemy_attack
            print(f"You are dealt {enemy_attack} points of damage. HP left : {player_hp}.")
        if player_hp <= 0:
            victory = False
            break

    # Résultat du combat
    if victory:
        print("\nVictory in the Astronomy Tower !")
        modify_money(character, 100)
        character["Attributes"]["loyalty"] += 1
        character["Attributes"]["courage"] += 1
        add_to_inventory(character, "inventory", "Astronomy Tower Token")
    else:
        print("\nDefeated in the Astronomy Tower. You'll face consequences.")
        modify_money(character, -50)
        character["Attributes"]["courage"] -= 1

    if ask_text("Press Enter to see your inventory...") == "":
        display_character(character)
        return character
    else:
        return character

def Half_blood_prince(character):
    potion_minigame(character)
    duel_deatheaters(character)
    duel_astronomy_tower(character)

def chapter_5(character):
    print()
    print("-------Chapter 5: The Potion Brewing Minigame-------")
    print()
    print("Welcome to your first Potion Brewing class at Hogwarts!")
    print()
    Half_blood_prince(character)
    print()
    print ("End of Chapter 5 — You've taken your first steps into the world of potion brewing!")



