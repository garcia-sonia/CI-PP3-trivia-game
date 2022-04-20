# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
questions_asked = [
    "What is the most commonly broken human bone?\n(a) femur\n(b)clavicle",
    "What vitamin is sometimes refered to as the sunshine vitamin?\n(a) vitamin A\n(b)vitamin D",

keys == [
    Key(questions[0], "a"),
    Key(questions[1], "b")
]

def play_quiz(keys):
    '''function
    '''
    score = 0
    for key in keys:
        answer = input(question.ask)
        if answer == question.answer:
            score += 1
    print("you got", score, "out of", len(questions))

play_quiz(keys)