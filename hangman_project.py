# Author MrS & TW 1/15/21

import random 

wordlist = ["area", "book", "business", "case", "child", "comany", "country", "day", "eye", "fact", "family", "government", "grou", "hand", "home", "job", "life", "lot", "man", "money", "month", "mother", "night", "number", "part", "people", "place", "point", "problem", "program", "question", "right", "room", "school", "state", "story", "student", "study", "system", "thing", "time", "water", "way", "week", "woman", "word", "work", "world", "year"]

words = random.choice(wordlist)

print(len(words))

correct = ['_'] * len(words)
wrong = []

def length():
    for i in correct:
        print(i, end = ' ')
    print()

length()

while True:

    print('-------------')

    guess = input("Guess a letter: ")

    if guess in wordlist:
        index = 0
        for i in words:
            if i == guess:
                right[index] = guess
            index += 1
        length()
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


