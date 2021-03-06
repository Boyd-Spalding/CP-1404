# """
# CP1404/CP5632 - Practical
# Random word generator - based on format of words
#
# Another way to get just consonants would be to use string.ascii_lowercase
# (all letters) and remove the vowels.
# """
# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#
# word_format = "ccvcvvc"
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     else:
#         word += random.choice(VOWELS)
#
# print(word)


"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS_WILDCARD = "#"
CONSONANTS_WILDCARD = "%"
CHOICES = "#%cv"

word_format = ""
input_length = random.randint(1, 10 + 1)
for i in range(input_length):
    word_format += random.choice(CHOICES)

print("Word format: {}".format(word_format))


word = ""
for kind in word_format:
    if kind == VOWELS_WILDCARD:
        char_size = random.randint(1, 5 + 1)
        for i in range(char_size):
            word += random.choice(VOWELS)
    elif kind == CONSONANTS_WILDCARD:
        char_size = random.randint(1, 5 + 1)
        for i in range(char_size):
            word += random.choice(CONSONANTS)
    elif kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)


print("Password is: {}".format(word))

