# Author MrS & TW 1/15/21

import random

def hangman_display(x):
    if x == 0:
        print("""+------+
|      
|
|
|
|
---""")
    if x == 1:
        print("""+------+
|      O
|
|
|
|
---""")
    if x == 2:
        print("""+------+
|      O
|      |
|
|
|
---""")
    if x == 3:
        print("""+------+
|      O
|     \|
|
|
|
---""")
    if x == 4:
        print("""+------+
|      O
|     \|/
|
|
|
---""")
    if x == 5:
        print("""+------+
|      O
|     \|/
|     /
|
|
---""")
    if x == 6:
        print("""+------+
|      O
|     \|/
|     / \
|
---""")

wordlist = ["area", "book", "business", "case", "child", "comany", "country", "day", "eye", "fact", "family", "government", "ground", "hand", "home", "job", "life", "lot", "man", "money", "month", "mother", "night", "number", "part", "people", "place", "point", "problem", "program", "question", "right", "room", "school", "state", "story", "student", "study", "system", "thing", "time", "water", "way", "week", "woman", "word", "work", "world", "year"]

words = random.choice(wordlist)

print(len(words))

correct = ['_'] * len(words) 
wrong = []  


def word_length():
    for i in correct:
        print(i, end = ' ')
    print()

word_length()
hangman_display(len(wrong))


while True:
    
    print('-------------')

    guess = input("Guess a letter: ")

    if guess in words:
        index = 0
        for i in words:
            if i == guess:
                correct[index] = guess
            index += 1
        word_length()
    else:
        if guess not in wrong:
            wrong.append(guess)
            hangman_display(len(wrong))
        else:
            print('Already guessed that')
        print(wrong)
    if len(wrong) > 5:
        print('You Lose!')
        print('The Word Was', words)
        break
    if '_' not in correct:
        print('You Win!')
        break