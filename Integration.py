# Brandon Roberts
# Space trivia
# Lines 6-9, 12-23, 25-31, 44-53, "Building a Multiple Choice Quiz - Mike Dane" on YouTube.
#      -turning the whole quiz into a looping function and pulling from an array made this a whole lot easier.
#      -altered code where not code-breaking in order to clean up
# restart function still not complete
# added check for user input error within questions to check for invalid input


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questionPrompts = [
    "What is the branch of science that deals with the physical nature of stars and other celestial bodies?\n"
    "(a) Space Science\n(b) Cosmology\n(c) Astrophysics\n(d) Physics\n\n",
    "What type of star is our sun?\n"
    "(a) Yellow Dwarf\n(b) Red Giant\n(c) Blue Dwarf\n(d) Neutron Star\n\n",
    "When a star dies, what phenomena occurs?\n"
    "(a) Solar Eclipse\n(b) Super Novae\n(c) It just stops shining\n(d) Nothing\n\n",
    "How are black holes formed?\n"
    "(a) The death of massive stars\n(b) Two stars colliding\n(c) An asteroid flies too fast\n(d) We don't know\n\n",
    "Which galaxy is the closest to our Milky Way Galaxy?\n"
    "(a) Whirlpool Galaxy\n(b) Messier 81\n(c) Sombrero Galaxy\n(d) Andromeda Galaxy\n\n"
]

questions = [
    Question(questionPrompts[0], "c"),
    Question(questionPrompts[1], "a"),
    Question(questionPrompts[2], "b"),
    Question(questionPrompts[3], "a"),
    Question(questionPrompts[4], "d"),
]


# added restart = true, restart = false, couldn't test in class
# def restart():
#     restart = true
#     while restart:
#         restart = input("Would you like to go again? Enter '1' for Yes or '2' for No: ")
#         if restart == 1:
#             run_quiz(questions)
#         else:
#             print("Thanks for playing!")
#             restart = false


def run_quiz(questions):
    print("Welcome to my simple space science quiz!")
    print("The following is a series of questions meant to stimulate your mind!")
    print("Make sure you enter the letter at the beginning of each question to ensure credit.")
    print("Good luck, and let us begin!")
    total = 0
    for question in questions:
        bad_input = True
        while bad_input:
            answer = input(question.prompt)
            if answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd':
                if answer == question.answer:
                    total += 1
                bad_input = False
            else:
                bad_input = True
    print("Congratulations, you got " + str(total) + "/" + str(len(questions)) + " correct!")
    restart = input("Would you like to play again? Enter '1' for Yes, '2' for No: ")
    if restart != 1:
        input("Thank you for playing! Enter any character to exit.")
    else:
        run_quiz(questions)


run_quiz(questions)
