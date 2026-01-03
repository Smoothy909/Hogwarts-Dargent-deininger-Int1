from random import choice, randrange, randint
from hogwarts.universe.character import display_character
from hogwarts.universe.house import modify_houses_points, display_winning_house
from hogwarts.utils.input_utils import load_file_content


def learn_spells(character):
    print("You begin your magic lessons at Hogwarts...")
    print()

    if "Spells" not in character:
        character["Spells"] = []

    data = load_file_content("hogwarts/data/spells.json")

    utility = []
    for spell in data:
        if spell["type"] == "Utility":
            utility.append(spell)

    offensive = []
    for spell in data:
        if spell["type"] == "Offensive":
            offensive.append(spell)

    defensive = []
    for spell in data:
        if spell["type"] == "Defensive":
            defensive.append(spell)


    learned = []

    def pick_one(pool):
        picked_spell = choice(pool)
        if picked_spell not in learned:
            character["spells_learned"].append(picked_spell["name"])
            learned.append(picked_spell)
        else:
            pick_one(pool)
        return picked_spell

    pick_one(offensive)
    print("˚ ༘ 🦕𖦹⋆｡˚")
    print(f"""The Potions classroom was unusually silent.
Snape was already waiting, arms crossed, his dark eyes fixed on you as if he were evaluating your worth before you even spoke.

“We shall see whether you can handle offensive magic without embarrassing yourself…”

With a sharp flick of his wand, a shadowy training figure materialized in front of you.

{spell['name']} is not a spell to be used lightly. But you must understand its mechanics.

You inhale slowly.
You raise your wand.
{spell['sensation']}

You have learned the spell: {spell['name']} ({spell['type']})

Snape gives the slightest nod—almost approval, or perhaps you imagined it.""")
    input()
    print()
    pick_one(defensive)


    print("ִֶָ. ..𓂃 ࣪ ִֶָ🪽་༘࿐")
    print(f"""The contrast is immediate: the Charms classroom is bright, lively, and full of floating objects.
Professor Flitwick bounces onto his stack of books, smiling warmly.

“Ah! A motivated student, excellent! Today we’ll practice a spell essential for your safety: {spell['name']}”

Around you, enchanted objects misbehave—flapping books, spinning chairs, feathers darting like birds.
Flitwick gestures encouragingly, inviting you to focus as the chaotic magic swirls around the room, waiting for your first attempt.""")

    input()
    print()

    used = []
    count = 0
    while count < 3:
        spell = choice(utility)

        if spell not in used:
            used.append(spell)
            character["spells_learned"].append(str(spell["name"]))
            learned.append(spell)
            count += 1
    print("⭒˚.⋆⭒🖤⃝🪐⭒˚.⋆⭒")
    print(f"""The Transfiguration classroom radiates discipline and precision.
Professor McGonagall stands tall, her sharp gaze cutting through the air as if she could read your thoughts.

“Utility spells form the foundation of proper magical practice. Let us begin.”

With a precise motion of her wand, she summons a variety of objects around you—feathers, books, fragments of pottery, and other items that shift subtly under the ambient magic.
Each one seems to react differently, as if waiting for the right spell to shape its behavior.

McGonagall guides you through the first exercise, her tone firm but encouraging.
You focus, channeling your intent as the spell begins to take form, accompanied by a distinct sensation: 
"A delicate, unveiling tingle spreads across your fingertips, as though secrets were surfacing to meet you."


You have learned the spell: {used[0]['name']} ({used[0]['type']})""")
    print(f"""
Without giving you time to rest, she transitions smoothly to the next lesson.
The objects around you shift again, responding to the new magical pattern you’re attempting to master.
You steady your wand, letting the energy settle before releasing it, feeling:
"A pulling current tugs at your palm, eager and insistent, as if the world itself were leaning toward you."

You have learned the spell: {used[1]['name']} ({used[1]['type']})""")
    print(f"""

For the final exercise, McGonagall raises her chin slightly, observing your posture with a critical eye.
The room grows quieter, as if the magic itself were holding its breath.
You concentrate, letting the spell unfold naturally, guided by the sensation blooming at your fingertips: 
"A soft, drifting sensation flows through your hand, gentle yet unsettling, like a thought slipping away."

You have learned the spell: {used[2]['name']} ({used[2]['type']})


McGonagall nods approvingly.

“You are progressing well. Continue like this, and you may become a competent wizard yet.”
""")
    input()


    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for s in learned:
        print(f"- {s['name']} ({s['type']}): {s['description']}")

    return learned


def magic_quiz(character, houses):
    print()
    print("⋆.ೃ࿔* :･🌱⋆.ೃ࿔* :･")
    print()
    print("You will now take the magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")
    print()

    data = load_file_content("hogwarts/data/magic_quiz.json")

    questions = []
    pool = []

    for truc in data:
        pool.append(truc)

    count = 0
    while count < 4 and len(pool) > 0:
        index = randrange(len(pool))
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
    print()
    all_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    all_houses.pop(all_houses.index(character['house']))
    for i in range(len(all_houses)):
        modify_houses_points(houses, 5*randint(0, 10),all_houses[i])
    modify_houses_points(houses, score, character['house'])
    print(f"your house {character['house']} has {houses[character['house']]} points!")
    display_winning_house(houses)
    return houses


def chapter_3(character, houses):
    print()
    print("-------Chapter 3: Classes and Discovering Hogwarts-------")
    print()
    learn_spells(character)
    magic_quiz(character, houses)
    display_character(character)
    print()
    print("End of Chapter 3 — Your magical journey continues!")
    return character, houses