# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import getpass

user_instructions = """Pick your decade, guess the band or the song,
find out your score"""

def introduce_quiz():
    """
    Initial message to introduce the quiz.
    Input will appear for user to type in their name.
    While loop will ensure that user does not leave
    the name input empty.
    Print also the instructions for the quiz
    """
    print('*' * 80)
    print('')
    print("Welcome to 'Guess the Band - Guess the Song'")
    print('')
    print('*' * 80)
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
    print(f"Welcome {user_name}! Let's find out how much you know!")
    print(user_instructions)
    print('')
    
introduce_quiz()




password = input("Please enter your password to access your coding tests")
print("That is not your assigned password")
quit()

print("It looks like you can\'t remberber your password. Would you like a hint?")






class Key:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



questions_asked = [
    "What is the most commonly broken human bone?\n(a) femur\n(b)clavicle",
    "What vitamin is sometimes refered to as the sunshine vitamin?\n(a) vitamin A\n(b)vitamin D",
]

keys = [
    Key(questions_asked[0], "a"),
    Key(questions_asked[1], "b")
]

def play_quiz(keys):
    '''function
    '''
    score = 0
    for key in keys:
        answer = input(key.prompt)
        if answer == key.answer:
            score += 1
    print("you got", score, "out of", len(questions_asked))


play_quiz(keys)