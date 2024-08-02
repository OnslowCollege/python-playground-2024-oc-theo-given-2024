"""Yourdle is a Wordle clone where you can alter aspects of the game."""
import random

from letter_list_3 import word_list_3
from letter_list_4 import word_list_4
from letter_list_5 import word_list_5
from letter_list_6 import word_list_6
from letter_list_7 import word_list_7


def makegreen(skk) -> str: return("\033[92m {}\033[00m" .format(skk))
def makeyellow(skk)-> str: return("\033[93m {}\033[00m" .format(skk))
def makered(skk)-> str: return("\033[91m {}\033[00m" .format(skk))

word_lists = {
    3:word_list_3,
    4:word_list_4,
    5:word_list_5,
    6:word_list_6,
    7:word_list_7}

#Setting Variables for while loops
valid_tries = False
valid_length = False
correct_guess = False
valid_guess = False
user_tries = 0
previous_guesses = ""
colored_guess = ""
#Lists of words of varying lengths

#While loop that forces the user to select a number of guesses within a range.
while not valid_tries:
    try:
        num_tries = int(input("Enter the number of guesses you want (3-10): "))
        if 3 <= num_tries <= 10:
            valid_tries = True
            print("")
        else:
            print("")
            print("Invalid Input.")
    except ValueError:
        print("")
        print("Invalid Input.")

#While loop that forces the user to select a word length within a range.
while not valid_length:
    try:
        word_length = int(input("Enter the length of the word you'll guess (3-7): "))
        if 3 <= word_length <= 7:
            valid_length = True
            print("")
        else:
            print("")
            print("Invalid Input.")
    except ValueError:
        print("")
        print("Invalid Input.")

user_word_list = word_lists[word_length]

word_index = random.randrange(0, len(user_word_list))
correct_answer = user_word_list[word_index]

print(correct_answer)
while user_tries != num_tries and not correct_guess:
    while not valid_guess:
        try:
            user_guess = str(input("Enter your guess: "))
            if len(user_guess) == word_length:
                valid_guess = True
                print("")
            else:
                print("")
                print("Invalid Input.")
        except ValueError:
            print("")
            print("Invalid Input.")
    if user_guess == correct_answer:
        print ("You guessed correctly!")
        correct_guess = True
    else:
        valid_guess = False
        user_tries = user_tries + 1
        for i in range(word_length):
            if user_guess[i] == correct_answer [i]:
                colored_guess = colored_guess + makegreen(user_guess[i])
        previous_guesses = previous_guesses + colored_guess + "\n"
        print (previous_guesses)
        if num_tries-user_tries != 0:
            print (f"Incorrect. You have {num_tries-user_tries} guesses left.")
if user_tries == num_tries:
    print(f"You ran out of guesses! The answer was: {correct_answer}")







