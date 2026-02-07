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


def ask_question(questions:list):
    question = random.choice(questions)
    answer = input(f"{question} (y/n): ")

    while answer != ("y" or "n"):  
        print("The answer must be 'y' or 'n'")
        answer = input() 
    return answer

ask_question(load_sorting_hat_questions("actual_question.json"))