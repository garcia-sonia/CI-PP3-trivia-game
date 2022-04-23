# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



user_instructions = """In this quiz you'll need to guess the band,
the song or the lyrics. There are 20 questions and you will
get your final 'Top of the Pops' score after answering all the questions.
"""

def introduce_quiz():
    """
    Initial message to introduce the quiz.
    Input will appear for user to type in their name.
    While loop will ensure that user does not leave
    the name input empty.
    Print also the instructions for the quiz
    """
    print('*' * 60)
    print('')
    print("Welcome to the 'Top of the Pops' quiz")
    print('')
    print('*' * 60)
    print('')
    global user_name
    while True:
        user_name = input("Please enter your name:\n")
        print('')
        if user_name == '':
            print("Please enter a name!")
            print('')
        else:
            break
    print(f"Welcome {user_name}!")
    print(user_instructions)
    print('')
    

introduce_quiz()



def enter_favorite_song():
    favorite_song = input("Before we start the quiz, please enter your favourite band for our records\n")
    print('')
    if favorite_song == '':
        print("Please enter your favorite band!")
        print('')
    else:
        print(f"Thank you {user_name} let's start the quiz!\n")
        print('')


enter_favorite_song()

'''
def favorite_decade():
    user_decade = input("Choose your favorite decade: 70s / 80s / 90s / 2000s\n")
    if user_decade == "80s":
        play_quiz_80(keys)
    else:
        quit()


favorite_decade()
'''

class Key:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



questions_asked = [
    "What is the most commonly broken human bone?\n(a) femur\n(b)clavicle\n",
    "What vitamin is sometimes refered to as the sunshine vitamin?\n(a) vitamin A\n(b)vitamin Db",
]

keys = [
    Key(questions_asked[0], "a"),
    Key(questions_asked[1], "b")
]


def play_quiz(keys):
    '''
    function
    '''
    score = 0
    for key in keys:
        answer = input(key.prompt)
        if answer == key.answer:
            score += 1
    print("you got", score, "out of", len(questions_asked))


play_quiz(keys)