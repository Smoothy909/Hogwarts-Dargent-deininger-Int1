
from hogwarts.utils.input_utils import *
def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] += points
    else:
        houses[house_name] = points
    return houses

def display_winning_house(houses):
    if not houses:
        print("No houses available.")
        return
    winning_house = max(houses, key=houses.get)
    print(f"The winning house is {winning_house} with {houses[winning_house]} points!")

questions = [
    (
        "After you have died, what would you most like people to do when they hear your name?",
        [
            "Miss you, but smile.",
            "Ask for more stories about your adventures.",
            "Think with admiration of your achievements.",
            "Think 'I don't care what they say, I admired them.'"
        ],
        ["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"]
    ),
    (
        "Given the choice, would you rather invent a potion that would guarantee you:",
        [
            "Glory?",
            "Wisdom?",
            "Love?",
            "Power?"
        ],
        ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    ),
    (
        "You enter an enchanted garden. What do you look at first?",
        [
            "The silver leaf tree bearing golden apples.",
            "The fat red toadstools that appear to be talking to each other.",
            "The luminous pool with something mysterious in its depths.",
            "The statue of an old wizard with a strangely twinkling eye."
        ],
        ["Ravenclaw", "Hufflepuff", "Slytherin", "Gryffindor"]
    ),
    (
        "Four boxes are placed before you. Which would you try to open?",
        [
            "The small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking.",
            "The gleaming jet black box with a silver lock and key, marked with a mysterious rune.",
            "The plain pewter box, which says 'I open only for the worthy.'",
            "The small golden casket, standing on clawed feet, with an inscription warning that secret knowledge comes at a price."
        ],
        ["Hufflepuff", "Slytherin", "Gryffindor", "Ravenclaw"]
    ),
    (
        "A Muggle confronts you and says they know you are a wizard. What do you do?",
        [
            "Ask them what makes them think so?",
            "Agree, and ask whether they’d like a free sample of a jinx?",
            "Agree, and walk away, leaving them to wonder if you are bluffing.",
            "Tell them you are worried about their mental health and offer to call a doctor."
        ],
        ["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"]
    ),
    (
        "Which of the following do you find most difficult to deal with?",
        [
            "Hunger",
            "Cold",
            "Loneliness",
            "Boredom"
        ],
        ["Hufflepuff", "Slytherin", "Gryffindor", "Ravenclaw"]
    ),
    (
        "You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. What do you do?",
        [
            "Attempt to confuse the troll into letting all three of you pass without fighting.",
            "Suggest drawing lots to decide which of you will fight.",
            "Volunteer to fight immediately.",
            "Offer the troll a trade (a shiny object or galleons) to let you pass."
        ],
        ["Ravenclaw", "Hufflepuff", "Gryffindor", "Slytherin"]
    ),
]

def assign_house(character):
    list_house_answers = [["Gryffindor"],["Hufflepuff"],["Ravenclaw"],["Slytherin"]]
    for i in range(len(questions)):
        question, options, houses = questions[i]
        answer = ask_choice(question, options)
        selected_house = houses[options.index(answer)]
        if selected_house == "Gryffindor":
            list_house_answers[0].append(answer)
        elif selected_house == "Hufflepuff":
            list_house_answers[1].append(answer)
        elif selected_house == "Ravenclaw":
            list_house_answers[2].append(answer)
        elif selected_house == "Slytherin":
            list_house_answers[3].append(answer)
    while True:
        if len(list_house_answers[0]) > len(list_house_answers[1]):
            if len(list_house_answers[0]) > len(list_house_answers[2]):
                if len(list_house_answers[0]) > len(list_house_answers[3]):
                    assigned_house = "Gryffindor"
                    break
                elif len(list_house_answers[0]) < len(list_house_answers[3]):
                    assigned_house = "Slytherin"
                    break
                else:
                    assigned_house = ask_choice("It's a tie between Gryffindor and Slytherin! Which house do you prefer?", ["Gryffindor", "Slytherin"])
                    break
            elif len(list_house_answers[0]) < len(list_house_answers[2]):
                assigned_house = "Ravenclaw"
                break
            else:
                if len(list_house_answers[2]) > len(list_house_answers[3]):
                    assigned_house = ask_choice("It's a tie between Gryffindor and Ravenclaw! Which house do you prefer?", ["Gryffindor", "Ravenclaw"])
                    break
                elif len(list_house_answers[2]) < len(list_house_answers[3]):
                    assigned_house = "Slytherin"
                    break
                else:
                    assigned_house = ask_choice("It's a three-way tie between Gryffindor, Ravenclaw, and Slytherin! Which house do you prefer?", ["Gryffindor", "Ravenclaw", "Slytherin"])
                    break
        elif len(list_house_answers[0]) < len(list_house_answers[1]):
            if len(list_house_answers[1]) > len(list_house_answers[2]):
                if len(list_house_answers[1]) > len(list_house_answers[3]):
                    assigned_house = "Hufflepuff"
                    break
                elif len(list_house_answers[1]) < len(list_house_answers[3]):
                    assigned_house = "Slytherin"
                    break
                else:
                    assigned_house = ask_choice("It's a tie between Hufflepuff and Slytherin! Which house do you prefer?", ["Hufflepuff", "Slytherin"])
                    break
            elif len(list_house_answers[1]) < len(list_house_answers[2]):
                assigned_house = "Ravenclaw"
                break
            else:
                if len(list_house_answers[2]) > len(list_house_answers[3]):
                    assigned_house = ask_choice("It's a tie between Hufflepuff and Ravenclaw! Which house do you prefer?", ["Hufflepuff", "Ravenclaw"])
                    break
                elif len(list_house_answers[2]) < len(list_house_answers[3]):
                    assigned_house = "Slytherin"
                    break
                else:
                    assigned_house = ask_choice("It's a three-way tie between Hufflepuff, Ravenclaw, and Slytherin! Which house do you prefer?", ["Hufflepuff", "Ravenclaw", "Slytherin"])
                    break
        else:
            if len(list_house_answers[2]) > len(list_house_answers[3]):
                assigned_house = ask_choice("It's a tie between Gryffindor and Hufflepuff! Which house do you prefer?", ["Gryffindor", "Hufflepuff"])
                break
            elif len(list_house_answers[2]) < len(list_house_answers[3]):
                assigned_house = "Slytherin"
                break
            else:
                assigned_house = ask_choice("It's a four-way tie! Which house do you prefer?", ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"])
                break

    character['house'] = assigned_house
    print(f"You have been assigned to {assigned_house}!")
    return assigned_house
