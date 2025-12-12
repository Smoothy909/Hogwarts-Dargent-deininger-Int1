from hogwarts.universe.character import *
from random import randint, choice

def create_team(house, team_data, is_player=False, player=None):
    team = {
        "house": house,
        "score": 0,
        "has_scored": 0,
        "has_blocked": 0,
        "caught_snitch": False,
        "members": []
    }

    if is_player and player:
        team["members"].append(player["first_name"] + " " + player["last_name"] + ' (Seeker)')
    if house in team_data:
        team['members'].extend(team_data[house]["players"])

    return team

def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal = randint(1, 10)
    if chance_goal >= 6:
        points_scored = 10
        attacking_team["score"] += points_scored
        attacking_team["has_scored"] += 1
        if player_is_seeker:
            goal_player = attacking_team['members'][0]
        else:
            if len(attacking_team['members']) > 1:
                goal_player = attacking_team['members'][randint(1, len(attacking_team['members']) - 1)]
            else:
                goal_player = attacking_team['members'][0]
        print(f"Goal scored by {goal_player}! {attacking_team['house']} earns {points_scored} points.")
    else:
        defending_team["has_blocked"] += 1
        print(f"{defending_team['house']} blocked the goal attempt!")

def golden_snitch_appears():
    chance_snitch = randint(1, 6)
    if chance_snitch == 6:
        return True
    return False

def catch_snitch(e1):
    catch = randint(1, 6)
    if catch == 1:
        e1["caught_snitch"] = True
        e1["score"] += 150
        print(f"{e1['house']} caught the Golden Snitch and earns 150 points!")
        return e1
    else:
        return e1

def display_score(e1, e2):
    print()
    print("-------Score-------")
    print(f"{e1['house']} -> {e1['score']} points | Goals Scored: {e1['has_scored']} | Snitch Caught: {'Yes' if e1['caught_snitch'] else 'No'}")
    print(f"{e2['house']} -> {e2['score']} points | Goals Scored: {e2['has_scored']} | Snitch Caught: {'Yes' if e2['caught_snitch'] else 'No'}")
    print("------------------------------")

def display_team(house,team):
    print()
    print(f"-------{house} Quidditch Team-------")
    print("Team Members:")
    for member in team['members']:
        print(f" - {member}")
    print("------------------------------")

def quidditch_match(character, houses):
    player_team = create_team(character['house'], houses, is_player=True, player=character)
    available_houses = {k: v for k, v in houses.items() if k != character['house']}
    opponent_house = choice(list(available_houses.keys()))
    opponent_team = create_team(opponent_house, available_houses, is_player=False)
    input("Press Enter to see the teams...")
    display_team(character['house'], player_team)
    display_team(opponent_team['house'], opponent_team)
    print()
    print("You will be playing as the Seeker for your team!")
    print()
    input("Press Enter to start the match...")
    print('--------Quidditch Match Start!--------')
    n = 1
    while n <= 20 and not (player_team["caught_snitch"] or opponent_team["caught_snitch"]):
        print()
        print('---Round', n, '---')
        attempt_goal(player_team, opponent_team, player_is_seeker=True)
        attempt_goal(opponent_team, player_team, player_is_seeker=False)
        if golden_snitch_appears():
            print("The Golden Snitch has appeared!")
            print()
            if n % 2 == 1:
                print("You have a chance to catch the Snitch!")
                input()
                catch_snitch(player_team)
            else:
                print(f"{opponent_team['house']} has a chance to catch the Snitch!")
                catch_snitch(opponent_team)
            break
        display_score(opponent_team, player_team) if (n % 3 == 1) or (n == 1) else None
        n += 1
        input()
    print('--------Quidditch Match End!--------')
    display_score(opponent_team, player_team)
    winning_team = player_team if player_team["score"] > opponent_team["score"] else opponent_team
    #display_winning_house(winning_team) #to update later with match winner
    print()
    print(f"The winner of the Quidditch match is {winning_team['house']}!")
    print()
    return

def chapter_4(character):
    print()
    print("-------Chapter 4: The Quidditch Match-------")
    print()
    print("It's time for your first Quidditch match! As the Seeker for your house team, you have a crucial role to play.")
    print("The match will consist of several rounds where both teams will attempt to score goals and catch the Golden Snitch.")
    print("Your performance as the Seeker can greatly influence the outcome of the match.")
    print("Get ready to take to the skies and lead your team to victory!")
    input()
    houses_data = load_file_content("hogwarts/data/teams_quidditch.json")
    quidditch_match(character, houses_data)
    print("End of Chapter 4 — What an incredible performance on the field!")



