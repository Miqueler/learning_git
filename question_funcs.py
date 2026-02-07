import json
import random

def load_sorting_hat_questions(filepath:str):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        questions = data.get("questions", [])

        if not questions:
            raise ValueError("No questions found in the JSON file.")

        return questions

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")


def ask_question(question_info:dict):
    #Expects the info from the question and returns a dictionary with the weights attached to each house for the given answer.
    question = question_info["text"]
    possible_answers = question_info["answers"]
    answer = input(f'''{question}
    1: {possible_answers[0]["text"]}
    2: {possible_answers[1]["text"]}
    3: {possible_answers[2]["text"]}
    4: {possible_answers[3]["text"]}
    Enter your answer (1-4): ''')
    

    while answer not in ["1", "2", "3", "4"]:  
        print("The answer must be a number 1-4")
        answer = input() 
    return possible_answers[int(answer)]["weights"]

def update_house_weightings(current_weightings, answer_weightings):
    for house in current_weightings.keys():
        current_weightings[house] += answer_weightings[house]
    return current_weightings