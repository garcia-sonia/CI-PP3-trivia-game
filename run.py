# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    print("you got", score, "out of", len(questions))


play_quiz(keys)