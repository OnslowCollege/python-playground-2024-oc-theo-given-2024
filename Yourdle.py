"""Yourdle is a Wordle clone where you can alter aspects of the game."""
#Importing the random module for random selection of words.
import random

#Importing the lists of words
from letter_list_3 import word_list_3
from letter_list_4 import word_list_4
from letter_list_5 import word_list_5
from letter_list_6 import word_list_6
from letter_list_7 import word_list_7


#Functions for easily changing color of text.
def makegreen(skk) -> str: return (f"\033[0;37;42m{skk}\033[0;30m")
def makeyellow(skk)-> str: return(f"\033[0;43m{skk}\033[0;30m")
def makered(skk)-> str: return(f"\033[0;41m{skk}\033[0;30m")

#Dictionary containing all the word lists for easy access
word_lists = {
    3:word_list_3,
    4:word_list_4,
    5:word_list_5,
    6:word_list_6,
    7:word_list_7}

#Setting Variables
valid_tries = False
valid_length = False
correct_guess = False
valid_guess = False
user_tries = 0
previous_guesses = ""
colored_guess = ""
check_1 = ""
check_2 = ""
check_3 = ""
num_repeats = 0

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

#Selecting the word list of the users choice.
user_word_list = word_lists[word_length]

#Randomly selecting a word from the aforementioned list to be the answer.
word_index = random.randrange(0, len(user_word_list))
correct_answer = user_word_list[word_index]


#Getting the game to tell me the answer (For testing purposes)
print(correct_answer)

#The actual game part
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
        correct_guess = True
        for i in range(word_length):
            colored_guess = colored_guess + makegreen(user_guess[i])
        previous_guesses = previous_guesses + colored_guess + "\n"
        print (previous_guesses)
        print ("You guessed correctly!")
    else:
        valid_guess = False
        user_tries = user_tries + 1
        #Colors and prints their guess along with all previous guesses
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                check_1 = check_1 + "-"
            else:
                check_1 = check_1 + user_guess[i]
        print(check_1)
        print("")
        for i in range(word_length):
            for j in range(word_length):
                if i == j:
                    check_2 = check_2 + "_"
                else:
                    check_2 = check_2 + check_1[j]
            print (check_2)
            if check_1[i] in check_2:
                check_3 = check_3 + check_1[i]
            else:
                check_3 = check_3 + "_"
            check_2 = ""
        
        
        
        
        
        
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                colored_guess = colored_guess + makegreen(user_guess[i])
            elif user_guess[i] in correct_answer:
                colored_guess = colored_guess + makeyellow(user_guess[i])
            else:
                colored_guess = colored_guess + makered(user_guess[i])
            
        previous_guesses = previous_guesses + colored_guess + "\n"
        colored_guess = ""
        print (check_3)
        check_1 = ""
        check_2 = ""
        check_3 = ""
        print (previous_guesses)
        # Tells the user how many tries they have left
        if num_tries-user_tries != 0:
            print (f"Incorrect. You have {num_tries-user_tries} guesses left.")
if user_tries == num_tries:
    print(f"You ran out of guesses! The answer was: {correct_answer}")







