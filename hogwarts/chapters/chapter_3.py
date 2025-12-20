import json
import random
from hogwarts.universe.character import display_character
from hogwarts.universe.house import update_house_points, display_winning_house
from hogwarts.utils.input_utils import load_file_content


def learn_spells(character):
    print("You begin your magic lessons at Hogwarts...")
    print()

    # jsp si c'est necessaire mais je prefere verif
    if "Spells" not in character:
        character["Spells"] = []

    data = load_file_content("hogwarts/data/spells.json")

    offensive = []
    for spell in data:
        if spell["type"] == "Offensive":
            offensive.append(spell)

    defensive = []
    for spell in data:
        if spell["type"] == "Defensive":
            defensive.append(spell)

    utility = []
    for spell in data:
        if spell["type"] == "Utility":
            utility.append(spell)

    learned = []

    def pick_one(pool):
        spell = random.choice(pool)
        character["Spells"].append(spell)
        learned.append(spell)
        print(f"You have just learned the spell: {spell['name']} ({spell['type']})")
        input("Press Enter to continue...")
        return spell

    pick_one(offensive)

    pick_one(defensive)

    used = []
    count = 0
    while count < 3:  # vu qu'on a beosin de 3 spell utility
        spell = random.choice(utility)

        if spell not in used:  # soit je fais ca soit je fais du .pop
            used.append(spell)
            character["Spells"].append(spell)
            learned.append(spell)
            print(f"You have just learned the spell: {spell['name']} ({spell['type']})")
            input("Press Enter to continue...")
            count += 1

    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for s in learned:
        print(f"- {s['name']} ({s['type']}): {s['description']}")

    return learned


def magic_quiz(character):
    print("Welcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")
    print()

    data = load_file_content("hogwarts/data/magic_quiz.json")

    questions = []
    pool = []

    for truc in data:
        pool.append(truc)

    count = 0
    while count < 4 and len(pool) > 0:
        index = random.randrange(len(pool))
        chosen = pool[index]
        pool.pop(index)
        questions.append(chosen)
        count = count + 1

    score = 0

    question_number = 1
    for q in questions:
        print(str(question_number) + ". " + q["question"])
        answer = input("> ")

        if answer.strip().lower() == q["answer"].lower():
            print("Correct answer! +25 points for your house.")
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {q['answer']}")

    print(f"Score obtained: {score} points")

    # Add to character score
    if "score" not in character:
        character["score"] = 0
    character["score"] += score

    return score


def chapter_3(character):
    print()
    print("-------Chapter 3: Classes and Discovering Hogwarts-------")
    print()

    learn_spells(character)
    points = magic_quiz(character)
    # faut aussi faire un truc avec lespt de maison
    display_character(character)

    print()
    print("End of Chapter 3 — Your magical journey continues!")
    return character
