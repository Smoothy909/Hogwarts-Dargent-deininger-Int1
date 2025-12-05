from hogwarts.universe.house import display_winning_house
from hogwarts.universe.character import *
from random import randint

def create_team(house, team_data, is_player=False, player=None):
    team = {
        "house": house,
        "score": 0,
        "has_scored": 0,
        "has_stopped": 0,
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
            goal_player = attacking_team['members'][randint(1,len(attacking_team['members'])-1)]
        print(f"Goal scored by {goal_player}! {attacking_team['house']} earns {points_scored} points.")
    else :
        defending_team["has_blocked"] += 1
        print(f"{defending_team['house']} blocked the goal attempt!")

def golden_snitch_appears():
    chance_snitch = randint(1, 9)
    if chance_snitch == 6:
        return True
    return False

def catch_snitch(e1, e2):
    catch = randint(1, 2)
    if catch == 1:
        e1["caught_snitch"] = True
        e1["score"] += 150
        print(f"{e1['house']} caught the Golden Snitch and earns 150 points!")
        return e1
    else:
        e2["caught_snitch"] = True
        e2["score"] += 150
        print(f"{e2['house']} caught the Golden Snitch and earns 150 points!")
        return e2

def display_score(e1, e2):
    print()
    print("-------Quidditch Score-------")
    print()
    print(f"{e1['house']}: {e1['score']} points | Goals Scored: {e1['has_scored']} | Snitch Caught: {'Yes' if e1['caught_snitch'] else 'No'}")
    print(f"{e2['house']}: {e2['score']} points | Goals Scored: {e2['has_scored']} | Snitch Caught: {'Yes' if e2['caught_snitch'] else 'No'}")
    print()
    print("------------------------------")

def display_team(house,team):
    print()
    print(f"-------{house} Quidditch Team-------")
    print()
    print("Team Members:")
    for member in team['members']:
        print(f" - {member}")
    print()
    print("------------------------------")

def quidditch_match(character, houses):
    print()
    player_team = create_team(character['house'], houses, is_player=True, player=character)
    houses.pop(character['house'])
    opponent_team = create_team(houses[randint(0,2)], houses, is_player=False, player=character)
    display_team(character['house'],player_team)
    display_team(opponent_team['house'],opponent_team)
    print()
    print("You will be playing as the Seeker for your team!")
    print()
    n=1
    print('--------Quidditch Match Start!--------')
    while n<=20 and not (player_team["caught_snitch"] or opponent_team["caught_snitch"]):
        print('---Round',n,'---')
        attempt_goal(player_team, opponent_team, player_is_seeker=True)
        print()
        attempt_goal(opponent_team, player_team, player_is_seeker=False)
        print()
        display_score(opponent_team, player_team)
        if golden_snitch_appears():
            print("The Golden Snitch has appeared!")
            print()
            if n%2==1:
                print("You have a chance to catch the Snitch!")
                catch_snitch(player_team, opponent_team)
            else:
                print(f"{opponent_team['house']} has a chance to catch the Snitch!")
                catch_snitch(opponent_team, player_team)
            break
        n+=1
        print()
        input("Press Enter to continue to the next round...")
    return

def chapter_4(character):
    print()
    print("-------Chapter 4: The Quidditch Match-------")
    print()
    print("It's time for your first Quidditch match! As the Seeker for your house team, you have a crucial role to play.")
    print("The match will consist of several rounds where both teams will attempt to score goals and catch the Golden Snitch.")
    print("Your performance as the Seeker can greatly influence the outcome of the match.")
    print("Get ready to take to the skies and lead your team to victory!")
    print()
    houses_data = load_file_content("//hogwarts/data/quidditch_teams.json")
    quidditch_match(character, houses_data)
    print()
    print("End of Chapter 4 — What an incredible performance on the field!")
    display_winning_house(houses_data)
