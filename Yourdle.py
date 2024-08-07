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

#Puts each character of the correct answer into a dictionary
correct_chars: dict[str, int] = {}
for i in range(word_length):
    correct_chars.setdefault(correct_answer[i], 0)
for i in range(word_length):
    correct_chars[correct_answer[i]] = correct_chars[correct_answer[i]] + 1
print (correct_chars)







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
                print("")
                print("Invalid Input.")
        except ValueError:
            print("")
            print("Invalid Input.")
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
        
        #Removes correct letters from the answer and user guess for later comparison
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                check_1 = check_1 + "-"
                check_2 = check_2 + "_"
            else:
                check_1 = check_1 + user_guess[i]
                check_2 = check_2 + correct_answer[i]
        
        #Creates a dictionary
        chars: dict[str, int] = {}
        for i in range(word_length):
            chars.setdefault(check_1[i], 0)
        for i in range(word_length):
            chars[check_1[i]] = chars[check_1[i]] + 1
        print (chars)
        
        #looks for each character of the trimmed user input
        for i in range(word_length):
            if check_1[i] in check_2:
                check_3 = check_3 + check_1[i]
            else:
                check_3 = check_3 + "-"
        
        #Creates a dictionary with each character in check_3
        guess_chars: dict[str, int] = {}
        for i in range(word_length):
            guess_chars.setdefault(check_3[i], 0)
        #Colors and prints their guess along with all previous guesses
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                colored_guess = colored_guess + makegreen(user_guess[i])
            elif user_guess[i] == check_3[i]:
                guess_chars[check_3[i]] = guess_chars[check_3[i]] + 1
                if guess_chars[check_3[i]] <= correct_chars[check_3[i]]:
                    colored_guess = colored_guess + makeyellow(user_guess[i])
                else:
                    colored_guess = colored_guess + makered(user_guess[i])
            else:
                colored_guess = colored_guess + makered(user_guess[i])
        previous_guesses = previous_guesses + colored_guess + "\n"
        #Resetting variables for the next guess
        colored_guess = ""
        check_1 = ""
        check_2 = ""
        check_3 = ""
        #Shows the user's last guess and all other guesses
        print (previous_guesses)
        #Tells the user how many tries they have left
        if num_tries-user_tries != 0:
            print (f"Incorrect. You have {num_tries-user_tries} guesses left.")
#Runs if the user runs out of guesses
if user_tries == num_tries:
    print(f"You ran out of guesses! The answer was: {correct_answer}")







