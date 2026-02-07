#!/usr/bin/env python3


def display_results(house):
    colors = {
        "Gryffindor": "\033[91m",
        "Slytherin": "\033[92m",
        "Ravenclaw": "\033[94m",
        "Hufflepuff": "\033[93m"
    }

    if house == "Gryffindor":
        print(
    "\033[1mCongratulations you brave soul, the house has assigned you to the house of "
    "\033[91mGodric Gryffindor!\033[0m")
    elif house == "Slytherin":
        print(
    "\033[1mI'm sorry for you selfish soul, you have been assigned to the kinda sucky "
    "\033[92mSlytherin :C\033[0m")
    elif house == "Ravenclaw":
        print(
    "\033[1mThe sorting hat has seen the desire for knowledge in your soul, "
    "\033[94myou have been assigned to the house of Rowena Ravenclaw!\033[0m")
    elif house == "Hufflepuff":
        print(
    "\033[1mDoes this house even matter?, you've been assigned to "
    "\033[93mHufflepuff :|\033[0m")


def get_house(weights:dict):
    house = max(weights, key=weights.get)
    return house