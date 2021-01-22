# Author MrS & TW 1/15/21

import random

wordlist = ["area", "book", "business", "case", "child", "comany", "country", "day", "eye", "fact", "family", "government", "ground", "hand", "home", "job", "life", "lot", "man", "money", "month", "mother", "night", "number", "part", "people", "place", "point", "problem", "program", "question", "right", "room", "school", "state", "story", "student", "study", "system", "thing", "time", "water", "way", "week", "woman", "word", "work", "world", "year"]

words = random.choice(wordlist)

print(len(words))

correct = ['_'] * len(words) # ***** needs to be in function and defined
wrong = []  # Defined in if else statement


def word_length():
    correct = ['_'] * len(words) # ***** needs to be defined
    for i in correct:
        print(i, end = ' ')
    print()


word_length()

# Problem when running program. When giving guesses, they are identified as wrong
# problem may be in if else statement or the variable correct (line 11)

while True:

    print('-------------')

    guess = input("Guess a letter: ")

    if guess in wordlist:
        index = 0
        for i in words:
            if i == guess:
                correct[index] = guess
            index += 1
        word_length()
    else:
        if guess not in wrong:
            wrong.append(guess)
        else:
            print('Already guessed')
        print(wrong)
    if len(wrong) > 5:
        print('You Lose!')
        print('The Word Was', words)
        break
    if '_' not in correct:
        print('You Win!')
        break

    # Make top and bottom row of hangman picture as list
    # Make the separate body parts and have the program call them to the function
