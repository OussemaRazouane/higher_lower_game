from replit import clear
import art
from game_data import*
import random

per_data = data

def affichage(a:dict):
    """Print the message in this form name..."""
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")

def game(sc:int):
    if per_data:
        clear()
        print(art.logo)
        if sc!=0:
            print(f"You're right! Current score: {sc}.")
        a=random.choice(per_data)
        per_data.remove(a)
        b=random.choice(per_data)
        per_data.remove(b)
        affichage(a)
        print(art.vs)
        affichage(b)
        anser=input("Who has more followers? Type 'A' or 'B'")
        if anser=="A" and a["follower_count"]>b["follower_count"]:
            game(sc+1)
        elif anser=="B" and b["follower_count"]>a["follower_count"]:
            game(sc+1)
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {sc}.")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {sc}.")
game(0)
