"""Yourdle is a Wordle clone where you can alter aspects of the game."""
from letter_list_7 import word_list_7
from letter_list_6 import word_list_6
from letter_list_5 import word_list_5
from letter_list_4 import word_list_4
from letter_list_3 import word_list_3


#Setting Variables for while loops
valid_tries = False
valid_length = False



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
        word_length = int(input("Enter the length of the word to guess (3-7): "))
        if 3 <= word_length <= 7:
            valid_length = True
            print("")
        else:
            print("")
            print("Invalid Input.")
    except ValueError:
        print("")
        print("Invalid Input.")








