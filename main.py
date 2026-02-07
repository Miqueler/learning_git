#!/usr/bin/env python3

"""Hogwarts house sorter"""

from cli_utils import get_house, display_results
from question_funcs import load_sorting_hat_questions, ask_question, update_house_weightings


questions_list = load_sorting_hat_questions("actual_question.json")
weightings = {
    "Gryffindor": 0, 
    "Slytherin": 0, 
    "Ravenclaw": 0, 
    "Hufflepuff": 0
}

def main():
    for question in questions_list:
        answer_weightings = ask_question(question)
        weightings = update_house_weightings(weightings, answer_weightings)
    house = get_house(weightings)
    display_results(house)
    print("The sorting hat thanks you for your patience. Don't get up to no good at Hogwarts!")


if __name__ == "__main__":
    print("Welcome to our Hogwarts house quiz!")
    print("Which house shall you be sorted in? Answer the questions to find out...")
    while True:
        try:
            main()
        except:
            print("You took off the sorting hat and decided Hogwarts isn't for you.")
            print("Try again next year!")