import random


def select_integer(min, max):
    """
    Random integer is returned

    :param min: number 1
    :param max: number 2
    :return: returns  random integer between number 1 and number2
    """

    return random.randint(int(min), int(max))

def maths_operations():
    """
    Operator is returned

    :return: arithemetic operation is returned
    """
    return random.choice(['+', '-', '*'])
def maths_result(num_1, num_2, operation):
    '''
    maths  result is calculated
    :param num_1: number 1
    :param num_2: number 2
    :param operation: arithemetic operation
    :return: return the result of arithemetic equation
    '''
    problem = f"{num_1} {operation} {num_2}"
    if operation == '+': result = num_1 + num_2 # sum opration
    elif operation == '-': result = num_1 - num_2 # differenc operation
    else: result = num_1 * num_2 # multiplication operation
    return problem, result

def math_quiz():
    '''
    3  maths quiz  is presented , answer is checked with th user's answer and final score is displayed'
    :return: final score of quiz out of 3 questions
    '''
    score = 0
    pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(pi)):
        # 2 random integers and operator  are selected
        first_integer = select_integer(1, 10); second_integer = select_integer(1, 5.5); operation = maths_operations()

        PROBLEM, ANSWER = maths_result(first_integer, second_integer, operation) # problem and result is returned
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input!! Please enter a valid integer as your answer.")
        except Exception as e:
            print(f"An unexpected error found: {e}")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{int(pi)}") # final score is displayed

if __name__ == "__main__":
    math_quiz()
