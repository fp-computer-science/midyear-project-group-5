# Author MrS & TW 1/15/21

wordlist = import random.choice("area", "book", "business", "case", "child", "comany", "country", "day", "eye", "fact", "family", "government", "grou", "hand", "home", "job", "life", "lot", "man", "money", "month", "mother", "night", "number", "part", "people", "place", "point", "problem", "program", "question", "right", "room", "school", "state", "story", "student", "study", "system", "thing", "time", "water", "way", "week", "woman", "word", "work", "world", "year")

def rand_word():
    word = random.choice(wordlist)
    return word.upper()

def game(word):
    word_length = "_" * len(word)
    guess = False
    guessed_letters = []
    guessed_words = []
    tries =6