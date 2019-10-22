# Brandon Roberts
# Space trivia


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


def restart():
    while True:
        restart = input("Would you like to go again? Enter '1' for Yes or '2' for No: ")
        if restart == 1:
            run_quiz(questions)
        else:
            print("Thanks for playing!")
            break


def run_quiz(questions):
    print("Welcome to my simple space science quiz!")
    print("The following is a series of questions meant to stimulate your mind!")
    print("Good luck, and let us begin!")
    total = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            total += 1
    print("Congratulations, you got " + str(total) + "/" + str(len(questions)) + " correct!")
    restart()


run_quiz(questions)
