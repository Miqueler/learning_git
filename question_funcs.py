questions = {
    "When faced with a difficult challenge, what is your first instinct?": {
        "Gryffindor": 3,
        "Slytherin": 2,
        "Ravenclaw": 1,
        "Hufflepuff": 1
    },

    "What do you value most in yourself?": {
        "Gryffindor": 2,   # bravery
        "Slytherin": 3,    # ambition
        "Ravenclaw": 3,    # intelligence
        "Hufflepuff": 2    # loyalty
    },

    "Which of these would bother you the most?": {
        "Gryffindor": 2,   # injustice
        "Slytherin": 3,    # failure
        "Ravenclaw": 2,    # ignorance
        "Hufflepuff": 3    # betrayal
    },

    "How do you prefer to solve problems?": {
        "Gryffindor": 2,   # action
        "Slytherin": 3,    # strategy
        "Ravenclaw": 3,    # logic
        "Hufflepuff": 1    # cooperation
    },

    "What would others most likely praise you for?": {
        "Gryffindor": 3,   # courage
        "Slytherin": 2,    # leadership
        "Ravenclaw": 3,    # cleverness
        "Hufflepuff": 2    # kindness
    },

    "If you could be remembered for one thing, what would it be?": {
        "Gryffindor": 3,
        "Slytherin": 3,
        "Ravenclaw": 2,
        "Hufflepuff": 2
    },

    "In a group project, what role do you naturally take?": {
        "Gryffindor": 2,   # motivator
        "Slytherin": 3,    # organizer
        "Ravenclaw": 3,    # thinker
        "Hufflepuff": 2    # supporter
    },

    "Which trait do you find most admirable in others?": {
        "Gryffindor": 3,   # bravery
        "Slytherin": 2,    # determination
        "Ravenclaw": 3,    # wisdom
        "Hufflepuff": 3    # loyalty
    },

    "How do you react to rules?": {
        "Gryffindor": 2,   # bend them
        "Slytherin": 3,    # use them
        "Ravenclaw": 2,    # understand them
        "Hufflepuff": 3    # respect them
    },

    "What motivates you the most?": {
        "Gryffindor": 3,   # honor
        "Slytherin": 3,    # success
        "Ravenclaw": 2,    # knowledge
        "Hufflepuff": 2    # belonging
    }
}


def ask_question(question):
    answer = input(f"{question} (y/n): ")

    while answer != ("y" or "n"):  
        print("The answer must be 'y' or 'n'")
        answer = input() 
    return answer

