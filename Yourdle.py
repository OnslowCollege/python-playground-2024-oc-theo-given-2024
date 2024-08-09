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
def makegreen(skk) -> str:
    """
    Make the string entered have a green background.

    Arguments:
    ---------
        skk: The text that is getting a green background.

    Returns: The resulting text with a green background.

    """
    return (f"\033[0;37;42m{skk}\033[0;30m")

def makeyellow(skk)-> str:
    """
    Make the string entered have a yellow background.

    Arguments:
    ---------
        skk: The text that is getting a yellow background.

    Returns: The resulting text with a yellow background.

    """
    return(f"\033[0;43m{skk}\033[0;30m")

def makered(skk)-> str:
    """
    Make the string entered have a red background.

    Arguments:
    ---------
        skk: The text that is getting a red background.

    Returns: The resulting text with a red background.

    """
    return(f"\033[0;41m{skk}\033[0;30m")

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
user_check = ""
correct_check = ""
fin_check = ""
wrong_chars_list: list[str] = []
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
        word_length = int(input("Enter length of word you'll guess (3-7): "))
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

#Puts each character of the correct answer into a dictionary
correct_chars: dict[str, int] = {}
for i in range(word_length):
    correct_chars.setdefault(correct_answer[i], 0)
for i in range(word_length):
    correct_chars[correct_answer[i]] = correct_chars[correct_answer[i]] + 1

#Runs while the user still has guesses and they haven't yet guessed correctly
while user_tries != num_tries and not correct_guess:
    #Runs until the user inputs a guess that is valid
    while not valid_guess:
        try:
            user_guess = str(input("Enter your guess: "))
            if len(user_guess) == word_length:
                valid_guess = True
                print("")
            else:
                print("Invalid Input.")
                print("")
        except ValueError:
            print("Invalid Input.")
            print("")
    #Runs if the user guesses the correct word.
    if user_guess == correct_answer:
        correct_guess = True
        #Printing the user's last guess
        for i in range(word_length):
            colored_guess = colored_guess + makegreen(user_guess[i])
        previous_guesses = previous_guesses + colored_guess + "\n"
        print (previous_guesses)
        print ("You guessed correctly!")
    #Runs if the user guesses an incorrect word
    else:
        #Resets the valid guess boolean for the next guess
        valid_guess = False
        #Increases the number of attempts the user has had by 1
        user_tries = user_tries + 1
        
        #Removes correct letters from the answer and user guess for comparison
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                user_check = user_check + "-"
                correct_check = correct_check + "_"
            else:
                user_check = user_check + user_guess[i]
                correct_check = correct_check + correct_answer[i]
        
        #Looks for each character of the trimmed user input
        for i in range(word_length):
            if user_check[i] in correct_check:
                fin_check = fin_check + user_check[i]
            else:
                fin_check = fin_check + "-"
        
        #Creates a dictionary with each character in fin_check
        guess_chars: dict[str, int] = {}
        for i in range(word_length):
            guess_chars.setdefault(fin_check[i], 0)
        #Colors their guess and adds it to a string with all previous guesses
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                colored_guess = colored_guess + makegreen(user_guess[i])
            elif user_guess[i] == fin_check[i]:
                guess_chars[fin_check[i]] = guess_chars[fin_check[i]] + 1
                if guess_chars[fin_check[i]] <= correct_chars[fin_check[i]]:
                    colored_guess = colored_guess + makeyellow(user_guess[i])
                else:
                    colored_guess = colored_guess + makered(user_guess[i])
                    wrong_chars_list.append(makered(user_guess[i]))
            else:
                colored_guess = colored_guess + makered(user_guess[i])
                wrong_chars_list.append(makered(user_guess[i]))
                if wrong_chars_list.count(makered(user_guess[i])) >= 2:
                    wrong_chars_list.remove(makered(user_guess[i]))
        previous_guesses = previous_guesses + colored_guess + "\n"
        #Resetting variables for the next guess
        colored_guess = ""
        user_check = ""
        correct_check = ""
        fin_check = ""
        #Shows the user's last guess and all other guesses
        print (previous_guesses)
        #Shows all incorrect characters the user has found so far
        print("")
        print(wrong_chars_list)
        #Tells the user how many tries they have left
        if num_tries-user_tries != 0:
            print (f"You have {num_tries-user_tries} guesses left.")
#Runs if the user runs out of guesses
if user_tries == num_tries:
    print(f"You ran out of guesses! The answer was: {correct_answer}")
