"""
This is a quiz program built using functions, classes, and arrays to allow for condensed coding.
__author__ = Brandon Roberts
Citations added where necessary
"""
import sys  # Allows the use of system-specific functions like sys.exit to create a proper way to end the quiz
"""
Allows the use of system-specific functions like sys.exit to create a proper way to end the quiz
"""


class Question:
    """
A class defining the aspects of the prompt and answer
    """

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# Credit for the basic form of the below function goes to Mike Dane on YouTube,
# Altered to check for user error by Dalton, Jeffrey, Victoria, Prof. Vaneslow
# and myself from COP 1500 Fall 2019


def run_quiz(questions):
    """
Function built to run as a multiple choice quiz without the need for
multiple lines of code.
    :param questions: parameter pulling the Question array through the function
    """
    start_quiz = True
    while start_quiz:
        print()
        print()
        print("Welcome to my simple space science quiz!")
        print("The following is a series of questions meant to stimulate your "
              "mind!")
        print("Make sure you enter a correctly corresponding letter to ensure "
              "credit.")
        print("Good luck, and let us begin!")
        print()
        print()
        total = 0
        for question in questions:
            bad_input = True
            while bad_input:
                answer = input(question.prompt)
                if answer == 'a' or answer == 'b' or answer == 'c' or \
                        answer == 'd':
                    if answer == question.answer:
                        total += 1
                    bad_input = False
                else:
                    bad_input = True
                    print("Please enter a correct response.")
                    print()
        print("Congratulations, you got " + str(total) + "/" + str(
            len(questions))
              + " correct!")
        quiz_restart = input("Would you like to play again? Enter 'y' to "
                             "restart. Enter anything else to exit program.")
        if quiz_restart != 'y':
            print("Thank you for playing!")
            print()
            sys.exit(0)  # terminates program
        else:
            run_quiz(questions)


def main():
    """
The main body of the program which holds the question and question prompt arrays, as well as a user input function
asking the user if they wish to begin.
    """
    question_prompts = [  # An array allowing easier calling of questions through the function
        "What is the branch of science that deals with the physical nature of "
        "stars and other celestial bodies?\n"
        "(a) Space Science\n(b) Cosmology\n(c) Astrophysics\n(d) Physics\n\n",
        "What type of star is our sun?\n"
        "(a) Yellow Dwarf\n(b) Red Giant\n(c) Blue Dwarf\n(d) Neutron Star\n\n",
        "When a star dies, what phenomena occurs?\n"
        "(a) Solar Eclipse\n(b) Super Novae\n(c) It just stops shining\n(d) "
        "Nothing\n\n",
        "How are black holes formed?\n"
        "(a) The death of massive stars\n(b) Two stars colliding\n(c) An "
        "asteroid"
        " flies too fast\n(d) We don't know\n\n",
        "Which galaxy is the closest to our Milky Way Galaxy?\n"
        "(a) Whirlpool Galaxy\n(b) Messier 81\n(c) Sombrero Galaxy\n(d) "
        "Andromeda"
        " Galaxy\n\n"
    ]

    questions = [  # The questions array passing each question and its' answer through the Question class, allowing /
        Question(question_prompts[0], "c"),  # quiz function to use the arrays
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "a"),
        Question(question_prompts[4], "d"),
    ]
    quiz_run = True  # Function asking for user input if they would like to begin the quiz
    while quiz_run:
        quiz_start = input(
            "Would you like to play a game? Enter 'y' to begin. "
            "Enter anything else to leave.")
        if quiz_start != 'y':
            quiz_run = False
            print("Thank you for your time!")
        else:
            run_quiz(questions)


main()
