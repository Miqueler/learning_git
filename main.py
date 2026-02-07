#!/usr/bin/env python3

"""Hogwarts house sorter"""

from cli_utils import display_question, parse_answers, get_house, display_results
from question_funcs import load_sorting_hat_questions

print("Welcome to our Hogwarts house quiz!")
print("Which house shall you be sorted in? Answer the questions to find out...")

questions_list = load_sorting_hat_questions("actual_question.json")

def main():
    for question in questions_list:
        display_question(question)
        answer = input()
        parse_answers(question, answer)
    house = get_house()
    display_results(house)
    print("The sorting hat thanks you for your patience. Don't get up to no good at Hogwarts!")
    
while True:
    try:
        main()
    except:
        print("You took off the sorting hat and decided Hogwarts isn't for you.")
        print("Try again next year!")