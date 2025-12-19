from hogwarts.utils.input_utils import load_file_content
from random import randint
from hogwarts.utils.input_utils import ask_choice, ask_text
from random import choice
from hogwarts.universe.character import modify_money, add_to_inventory

def potion_minigame(character):
    print("The brewing class is about to start!")
    print("Today, you'll be brewing 3 potions.")

    available_potions = load_file_content("hogwarts/data/potions.json")

    potions_to_brew = [available_potions[randint(1, 8)] for _ in range(3)]
    all_ingredients = set()
    for potion in available_potions.values():
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
            print("here are the ingredients in the potion:")
            ingredients = potion.get("ingredients", [])
            for i in range(1, len(ingredients)):
                print(f"Potion: {ingredients[i]}")
            print("- ... and one more ingredient.")
            user_ingredient = ask_choice(f"We are missing an ingredient! \n Enter the last ingredient of {expected_name}: ",[ingredients[0], all_ingredients[randint(1,len(all_ingredients))], all_ingredients[randint(1,len(all_ingredients))], all_ingredients[randint(1,len(all_ingredients))]])
            if user_ingredient== ingredients[0]:
                print(f"Well done! {user_ingredient} is indeed an ingredient of {expected_name}.")
                success_count += 1
            else:
                print(f"Wrong ingredient. The correct ingredient was: {ingredients[0]}.")
        else:
            print(f"Wrong name. The correct name was: {expected_name}.")
        print()

    for j in range(success_count):
        character["Attributes"]["intelligence"] += 1
        character["Attributes"]["ambition"] += 1
        character[["money"]] += 5
    print(f"You successfully brewed {success_count} out of 3 potions.")

def duel_attack(character):
    spells = [
        ("Stupefy", 6),
        ("Expelliarmus", 5),
        ("Confringo", 8),
        ("Sectumsempra", 12),  # puissant mais risqué
        ("Expulso", 9)
    ]
    intel = character["Attributes"].get("intelligence", 0)
    amb = character["Attributes"].get("ambition", 0)
    base = randint(1, 6)
    # meilleur choix de sort si intelligence élevée
    if intel >= 8 and randint(1, 10) > 3:
        spell = choice([s for s in spells if s[0] in ("Sectumsempra", "Confringo")])
    elif amb >= 7 and randint(1, 10) > 4:
        spell = choice([s for s in spells if s[0] in ("Expulso", "Confringo")])
    else:
        spell = choice(spells)
    attack_value = base + (intel // 2) + (amb // 3) + spell[1]
    return attack_value, spell[0]

def duel_defense(character):
    maneuvers = [
        ("Protego", 8),
        ("Duck and Counter", 6),
        ("Disarming Charm (Expelliarmus)", 7),
        ("Shielding incantation", 5)
    ]
    courage = character["Attributes"].get("courage", 0)
    loyalty = character["Attributes"].get("loyalty", 0)
    base = randint(1, 6)
    if courage >= 8:
        maneuver = maneuvers[0]
    elif loyalty >= 7:
        maneuver = maneuvers[2]
    else:
        maneuver = choice(maneuvers)
    defense_value = base + (courage // 2) + (loyalty // 3) + maneuver[1]
    return defense_value, maneuver[0]

def duel_deatheaters(character):
    print("Vous tombez sur un groupe de Mangemorts. Préparez-vous au duel !")
    rounds = 3
    player_wins = 0
    for r in range(1, rounds + 1):
        print(f"\n— Round {r} —")
        atk_val, atk_spell = duel_attack(character)
        # création simple d'un ennemi basé sur difficulté aléatoire
        enemy_def = randint(3, 12) + randint(0, 4)
        print(f"Vous lancez {atk_spell} (puissance {atk_val}). Les Mangemorts se défendent ({enemy_def}).")
        if atk_val > enemy_def:
            print("Vous touchez l'ennemi !")
            player_wins += 1
        else:
            # ennemi contre-attaque
            enemy_atk = randint(4, 12)
            def_val, maneuver = duel_defense(character)
            print(f"Un Mangemort contre-attaque (puissance {enemy_atk}). Vous tentez {maneuver} (défense {def_val}).")
            if def_val >= enemy_atk:
                print("Vous parvenez à parer l'attaque.")
                player_wins += 0.5
            else:
                print("Vous êtes touché·e. Vous perdez un peu de confiance.")
                # pénalité modérée
                if character["Attributes"].get("courage", 0) > 0:
                    character["Attributes"]["courage"] = max(0, character["Attributes"]["courage"] - 1)
                modify_money(character, -10)

    # Résultat final
    if player_wins >= 2:
        print("\nVictoire contre les Mangemorts ! Vous vous en sortez honorablement.")
        modify_money(character, 30)
        character["Attributes"]["intelligence"] += 1
        add_to_inventory(character, "inventory", "Trophy of the skirmish")
    else:
        print("\nVous avez dû battre en retraite. Les Mangemorts vous ont mis en déroute.")
        modify_money(character, -20)
        # petite perte d'ambition si fuite
        character["Attributes"]["ambition"] = max(0, character["Attributes"]["ambition"] - 1)
    print(f"Attributs actuels : {character['Attributes']}. Argent : {character['money']}")

def duel_astronomy_tower(character):
    print("La Tour d'Astronomie. Une confrontation importante vous attend.")
    choice = ask_choice("Comment abordez-vous la situation ?", [
        "Affronter directement (bravoure)",
        "Tenter de désarmer discrètement (ruse)",
        "Appeler des renforts (prudence)"
    ])
    # modificateurs selon choix
    if choice == "Affronter directement (bravoure)":
        modifier = character["Attributes"].get("courage", 0) + randint(0, 4)
    elif choice == "Tenter de désarmer discrètement (ruse)":
        modifier = character["Attributes"].get("intelligence", 0) + randint(0, 4)
    else:
        modifier = character["Attributes"].get("loyalty", 0) + randint(0, 3)

    # Draco (ou adversaire) qualité dépend de l'ambition globale
    opponent_power = 8 + randint(0, 4) + (character["Attributes"].get("ambition", 0) // 2)
    player_attack, spell = duel_attack(character)
    total_player = player_attack + modifier

    print(
        f"Vous utilisez {spell} avec une force totale de {total_player}. L'adversaire a {opponent_power} de puissance.")
    if total_player >= opponent_power:
        print("Succès : vous neutralisez l'adversaire et maîtrisez la situation.")
        character["Attributes"]["loyalty"] += 1
        character["Attributes"]["courage"] += 1
        modify_money(character, 20)
    else:
        print("Échec : l'adversaire prend l'avantage. Vous subissez des conséquences.")
        # petites pénalités roleplay
        character["Attributes"]["courage"] = max(0, character["Attributes"]["courage"] - 1)
        modify_money(character, -15)
    print(f"Attributs actuels : {character['Attributes']}. Argent : {character['money']}")


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
    print ("End of Chapter 5 — You've taken your first steps into the world of potion brewing!")



