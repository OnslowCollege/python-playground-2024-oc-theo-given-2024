"""Yourdle is a Wordle clone where you can alter aspects of the game."""
#Importing the random module for random selection of words.
import random

#Importing the lists of words
from letter_list_3 import word_list_3
from letter_list_4 import word_list_4
from letter_list_5 import word_list_5
from letter_list_6 import word_list_6
from letter_list_7 import word_list_7

#Importing Textual modules
from textual.app import App, ComposeResult
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widgets import Button, Static
from textual import events


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
letter_list = "qwertyuiopasdfghjklzxcvbnm"
valid_tries = False
valid_length = False
correct_guess = False
valid_guess = False
valid_letter = False
user_tries = 0
previous_guesses = ""
colored_guess = ""
user_check = ""
answer_check = ""
fin_check = ""
wrong_chars = ""
wrong_chars_list: list[str] = []

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

#TEXTUAL


class LetterGuess(Static):
    def on_load(self):
        self.add_class("letterguess")
    def on_enter(self):
        self.add_class("correct")
class WordGuess(Static):
    def compose(self) -> ComposeResult:
        for i in range(word_length):
            yield LetterGuess("E")


class Yourdle(App):
    CSS_PATH = "Yourdle.tcss"

    def compose(self) -> ComposeResult:
        yield GuessContainer()
        yield InputContainer()




class GuessContainer(Static):
    def compose(self) -> ComposeResult:
        for i in range(num_tries):
            yield WordGuess()

class InputContainer(Static):
    def compose(self) -> ComposeResult:
        yield Button("Q")
        yield Button("W")
        yield Button("E")
        yield Button("R")
        yield Button("T")
        yield Button("Y")
        yield Button("U")
        yield Button("I")
        yield Button("O")
        yield Button("P")
        yield Button("A")
        yield Button("S")
        yield Button("D")
        yield Button("F")
        yield Button("G")
        yield Button("H")
        yield Button("J")
        yield Button("K")
        yield Button("L")
        yield Button("Z")
        yield Button("X")
        yield Button("C")
        yield Button("V")
        yield Button("B")
        yield Button("N")
        yield Button("M")

if __name__ == "__main__":
    app = Yourdle()
    app.run()



#Selecting the word list of the users choice.
user_word_list = word_lists[word_length]

#Randomly selecting a word from the aforementioned list to be the answer.


#Choosing the answer (For testing purposes)
correct_answer = input("Enter the answer: ")
if correct_answer == (""):
    word_index = random.randrange(0, len(user_word_list))
    correct_answer = user_word_list[word_index]
    correct_answer = correct_answer.lower()

#Runs while the user still has guesses and they haven't yet guessed correctly
while user_tries != num_tries and not correct_guess:
    #Runs until the user inputs a guess that is valid
    while not valid_guess:
        try:
            if num_tries-user_tries == 1:
                user_guess = str(input("Enter your final guess: "))
            else:
                user_guess = str(input("Enter your guess: "))
            user_guess = user_guess.lower()
            if len(user_guess) == word_length:
                valid_guess = True
                #Makes sure all characters in the answer are letters
                for i in range(word_length):
                    valid_letter = False
                    for j in range(len(letter_list)):
                        if user_guess[i] == letter_list[j]:
                            valid_letter = True
                    if not valid_letter:
                        valid_guess = False
                    valid_letter = False
                if not valid_guess:
                    print("Invalid Input.")
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
                answer_check = answer_check + "_"
            else:
                user_check = user_check + user_guess[i]
                answer_check = answer_check + correct_answer[i]
        
        #Looks for each character of the trimmed user input
        for i in range(word_length):
            if user_check[i] in answer_check:
                fin_check = fin_check + user_check[i]
            else:
                fin_check = fin_check + "-"
        
        #Puts each character of the answer check into a dictionary
        correct_chars: dict[str, int] = {}
        for i in range(word_length):
            correct_chars.setdefault(answer_check[i], 0)
        for i in range(word_length):
            correct_chars[answer_check[i]] = correct_chars[answer_check[i]] + 1
        #Creates a dictionary with each character in fin_check
        guess_chars: dict[str, int] = {}
        for i in range(word_length):
            guess_chars.setdefault(fin_check[i], 0)
        #Colors their guess and adds it to a string with all previous guesses
        #Also, adds all characters absent from the answer into a list.
        for i in range(word_length):
            if user_guess[i] == correct_answer[i]:
                colored_guess = colored_guess + makegreen(user_guess[i])
            elif user_guess[i] == fin_check[i]:
                guess_chars[fin_check[i]] = guess_chars[fin_check[i]] + 1
                if guess_chars[fin_check[i]] <= correct_chars[fin_check[i]]:
                    colored_guess = colored_guess + makeyellow(user_guess[i])
                else:
                    colored_guess = colored_guess + makered(user_guess[i])
            else:
                colored_guess = colored_guess + makered(user_guess[i])
                if user_guess[i] not in correct_answer:
                    wrong_chars_list.append(makered(user_guess[i]))
                if wrong_chars_list.count(makered(user_guess[i])) >= 2:
                    wrong_chars_list.remove(makered(user_guess[i]))
        previous_guesses = previous_guesses + colored_guess + "\n"
        #Shows the user's last guess and all other guesses
        print (previous_guesses)
        #Shows all incorrect characters the user has found so far
        print("")
        wrong_chars_list.sort()
        for i in range(len(wrong_chars_list)):
            if i < len(wrong_chars_list)-1:
                wrong_chars = wrong_chars + wrong_chars_list[i] + makered(" ")
            else:
                wrong_chars = wrong_chars + wrong_chars_list[i]
        print (wrong_chars)
        #Resetting variables for the next guess
        colored_guess = ""
        user_check = ""
        answer_check = ""
        fin_check = ""
        wrong_chars = ""
        #Tells the user how many tries they have left
        if num_tries-user_tries != 0:
            if num_tries-user_tries == 1:
                print ("You have 1 guess left.")
            else:
                print (f"You have {num_tries-user_tries} guesses left.")
#Runs if the user runs out of guesses
if user_tries == num_tries:
    print(f"No more guesses left! The answer was: {makegreen(correct_answer)}")
