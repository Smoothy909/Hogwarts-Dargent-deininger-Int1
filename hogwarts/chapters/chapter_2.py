import json
from hogwarts.universe import character
from hogwarts.utils.input_utils import ask_choice, load_file_content
from hogwarts.universe.house import assign_house, display_winning_house
from hogwarts.universe.character import display_character


def introduction2():
    print("You board the Hogwarts Express. The train begins its slow journey northward...")
    print("You settle into a quiet compartment, the hum of the train filling the air.")
    # or print("You find an empty compartment and take a seat as the train picks up speed")
    input("Press Enter to continue...")

def meet_friends(character):
    print("A red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you? ")
    choice1=ask_choice("How do you respond ?", ["Yes", "No"])
    if choice1=="Yes":
        character["Attributes"]["loyalty"] += 1
        print("")
        print("Sure, have a seat!")
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        input("")
        print("He leans closer, lowering his voice conspiratorially.")
        print("— Do you think we'll meet Harry Potter? I heard he's starting this year too!")
        print()
        print("(Harry Potter? So the rumors are true… This year might be more interesting than I thought.)")
        print()
        print("Before you can reply, the door opens again.")
    else:
        print("")
        character["Attributes"]["ambition"] += 1
        print("Sorry, I prefer to travel alone.")
        print("(I need some space to think. This year will define everything—I want to start on my own terms.)")
        input("")
        print("— Oh… okay then. No worries.")
        print("He leaves quietly, and you hear him chatting with someone in the next compartment.")
    input("")

    print("A girl enters, her arms full of books. She looks determined and curious.")
    print()
    print("— Hello, I'm Hermione Granger. Have you ever read A History of Magic?")
    choice2 = ask_choice("How do you respond?", ["Yes", "No"])
    if choice2 == "Yes":
        print("")
        character["Attributes"]["intelligence"] += 1
        print("Yes, I love learning new things!")
        print()
        print("Hermione beams, clearly impressed.")
        print("— Really? That’s great! Most people think magic is all about waving a wand, but understanding the theory behind it makes you a much better wizard.")
        input()
        print("She sits down and starts arranging her books.")
        print("— I’ve memorized all the spells in our textbooks already. It’s going to be brilliant!")
        print()
        print("(Wow… she’s intense. But maybe that’s a good thing.)")
    else:
        print("")
        character["Attributes"]["courage"] += 1
        print("Uh… no, I prefer adventures over books.")
        print("(Books are fine, but life is out there, not on a page. I want excitement, not homework.)")
        print("")
        print("Also")
        print("")
        print("I don't know how to read")
        input()
        print("— Well, adventures are fine, but knowledge is power, you know.")
        print("")
        print("She sits down anyway, flipping through a book.")
    input()
    print("A little later, the door opens once more.")
    print("A blonde boy steps in, his posture straight and confident, carrying himself with an air of elegance.")
    print("")
    print("— I'm Draco Malfoy. It's wise to choose your friends carefully from the start, don’t you think?")
    print("(He seems composed… but there’s something calculating in his tone. Is he offering advice or testing me?)")
    print()
    choice3 = ask_choice("How do you react?", ["Shake his hand politely", "Ignore him completely.","Respond with arrogance."])
    if choice3 == "Shake his hand politely":
        character["Attributes"]["intelligence"] += 1
        print("")
        print("Draco smirks.")
        print("— Smart choice. You'll go far at Hogwarts.")
        input()
        print("(Maybe he’s right… or maybe he’s just full of himself.)")
    elif choice3 == "Ignore him completely.":
        character["Attributes"]["loyalty"] += 1
        print("")
        print("Draco scowls, his voice dripping with disdain.")
        print("You'll regret that!")
        input()
        print("He storms out, muttering under his breath.")
        print("")
        print("(Good riddance. I don’t need his approval.)")

    else:
        print("")
        print("You match his tone.")
        print("— Maybe you should choose your words more carefully.")
        character["Attributes"]["ambition"] += 1
        input()
        print("Draco looks stunned, then laughs coldly.")
        print("— Interesting… I’ll remember you.")
        print("")
        print("(That could be trouble… or an opportunity.)")
    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print()
    print("Your choices already say a lot about your personality!")
    print()
    print(f"Your updated attributes : {character['Attributes']}")

def welcome_message():
    print("Professor Dumbledore appears before you, his eyes twinkling behind half-moon spectacles.")
    print("")
    print("He smiles gently before speaking.")
    print("")
    print("Welcome to Hogwarts")
    print("")
    print("A place where magic and knowledge intertwine, and where every choice you make will shape the wizard you are destined to become")
    print("")
    print("He pauses for a moment, his voice calm yet full of meaning.")
    print("")
    print("Remember: courage, wisdom, loyalty, and ambition all have their place here.")
    print("Your journey begins now... and I trust it will be a remarkable one.")

def sorting_ceremony(character):
    print()
    print("It's time for the Sorting Ceremony!")
    print("The Sorting Hat is placed on your head, and you feel it probing your mind.")
    assigned_house = assign_house(character)
    character["house"] = assigned_house
    print()
    print(f"The Sorting Hat has decided: You are in {assigned_house}!")
    display_character(character)
    return

def enter_common_room(character):
    house_info = load_file_content('hogwarts/data/houses.json')
    house=character["house"]
    if house == "Gryffindor":
        print("Percy Weasley, the Gryffindor prefect, gathers the new students with a proud smile.")

    print(f"{house_info[character['house']]['way']}")
    print(f"{house_info[character['house']]['description']}")
    print(f"{house_info[character['house']]['greetings']}")
    print(f"{house_info[character['house']]['installation_message']} {house_info[character['house']]['emoji']}")
    print(f"{house_info[character['house']]['traits']}")
    print("You feel a sense of belonging as you take in your new surroundings.")
    print()
    input("Press Enter to continue...")

def chapter_2(character):
    print()
    print("-------Chapter 2: The Journey to Hogwarts-------")
    print()
    introduction2()
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)
    print()
    print("End of Chapter 2 — Your adventure at Hogwarts is just beginning!")
    return character

