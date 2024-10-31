"""Yourdle is a Wordle clone where you can alter aspects of the game."""
#Importing the random module for random selection of words.
import random

#Importing the lists of words/letters
from letter_list import letter_list
from letter_list_3 import word_list_3
from letter_list_4 import word_list_4
from letter_list_5 import word_list_5
from letter_list_6 import word_list_6
from letter_list_7 import word_list_7

#Importing Textual modules
from textual import events
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Button, Label, Static

#Dictionary containing all the word lists for easy access
word_lists = {
    3:word_list_3,
    4:word_list_4,
    5:word_list_5,
    6:word_list_6,
    7:word_list_7}

#Setting Variables

correct_guess = False
valid_guess = False
user_tries = 0
user_check = ""
answer_check = ""
fin_check = ""
wrong_chars = ""
wrong_chars_list: list[str] = []
correct_chars_list: list[str] = []
dif_chars_list: list[str] = []
correct_answer = ""
currentid: str = ""
word_length = 0
num_tries = 0

#Creating the background for asking the user's chosen settings at the beginning
class UserQueryBackground(Static):
    
    class Create(Message):
        """Message sent when inputs are ready to be created."""
    
    #Creating the widget containing the buttons
    def compose(self):
        yield UserQuery()
    
    #Making the buttons record information and hide themselves once pressed
    def on_button_pressed(self, event):
        button = event.button
        global num_tries
        global word_length
        if button.id[1] == "1":
            #Selecting number of tries the user will have
            if len(button.id) == 4:
                num_tries = int(button.id[2:4])
            else:
                num_tries = int(button.id[2])
            self.query(".b1").add_class("hide")
            self.query(".b2").add_class("show")
        if button.id[1] == "2":
            #Selecting the length of the word the user will guess
            word_length = int(button.id[2])
            self.add_class("hide")
            self.add_class("bottomlayer")
            global correct_answer
            global user_word_list
            #Selecting a random word from the word list to be the answer
            user_word_list = word_lists[word_length]
            word_index = random.randrange(0, len(user_word_list))
            correct_answer = user_word_list[word_index]
            correct_answer = correct_answer.upper()
            #Telling the program to make the game interface
            self.post_message(Create())

#Widget containing the buttons for choosing settings
class UserQuery(Static):
    def compose(self):
        yield Label("Enter the number of guesses you would like!", classes="b1 text")
        for i in range(3, 11):
            yield UserQueryInput(str(i), id ="b1"+str(i), classes = "b1")
        yield Label("Enter the length of the word you'll guess!", classes="b2 text")
        for i in range(3, 8):
            yield UserQueryInput(str(i),id ="b2"+str(i),classes = "b2")
class UserQueryInput(Button):
    pass
#Message sent after settings have been recieved to create the game
class Create(Message):
    pass
#Message sent for deleting an inputted letter
class Backspace(Message):
    pass
#The widget the contains single letters
class LetterGuess(Static, can_focus = True):
    def on_load(self):
        self.add_class("letterguess")
    #Creates a border to show which letter is selected
    def on_focus(self):
        self.add_class("focus")
        global currentfocus
        currentfocus = app.focused
    #Removes border when unselected
    def on_blur(self):
        self.remove_class("focus")
    #Event caused when the user inputs a key
    def on_key(self, event) -> None:
        letter = event.key.upper()
        global currentid
        #Making sure the space isn't full and the key entered is a letter
        if self.renderable == "" and letter in letter_list:
            self.update(letter)
            currentid = str(self.id)
            currentid = int(currentid[1])
            currentid = currentid + 1
        #Removing letters when backspace is pressed
        if letter == "BACKSPACE" and self.renderable == "":
            self.update("")
            currentid = str(self.id)
            currentid = int(currentid[1])
            currentid = currentid - 1
        if letter == "BACKSPACE" and self.renderable != "":
            self.update("")
            currentid = str(self.id)
            currentid = int(currentid[1])
    #Removes letters when the container for all the letters is selected
    def on_backspace(self):
        self.update("")
    def on_win(self, event):
        #Getting id of the parent
        currentwg = self.parent
        currentwg_id = currentwg.id[-1]
        currentwg_id = "#wgw" + currentwg_id
        #Searching for the widget with the corresponding id
        postwgw = app.query_one(currentwg_id)
        #Posting information to the "win screen version" of the parent
        currentkey = self.renderable
        print(currentkey)
        if "correct" in self.classes:
            postwgw.post_message(NewLetterGuess("correct", currentkey, self))
        elif "incorrect" in self.classes:
            postwgw.post_message(NewLetterGuess("incorrect", currentkey, self))
        elif "wrongspot" in self.classes:
            postwgw.post_message(NewLetterGuess("wrongspot", currentkey, self))
        #Preventing unnecessary event bubbling
        event.stop()
        
class WordGuess(Static):
    def compose(self) -> ComposeResult:
        #Creating spaces for letters
        for i in range(word_length):
            yield LetterGuess("", id = ("l" + str(i+1)))
    def on_key(self, event) -> None:
        letter = event.key.upper()
        global currentid
        #For using backspace when the container for the letters is selected
        if letter in letter_list or letter == "BACKSPACE":  # noqa: SIM102
            if int(currentid) != word_length + 1 and int(currentid) != 0:
                currentletter = self.query_one("#l" + str(currentid))
                currentletter.focus()
                if letter == "BACKSPACE":
                    currentletter.post_message(Backspace())
    def on_show(self):
        #Selects the first letter of the first word when the game is created
        if self.id == "c0":
            self.query_one("#l1").focus()
    def key_enter(self):
        global valid_guess
        global correct_guess
        valid_guess = True
        
        #Creating a variable with the users current guess
        user_guess = ""
        for i in range(word_length):
            current_letter = self.query_one("#l"+str(i+1)).renderable
            user_guess = user_guess + str(current_letter)
        
        #Making the guess invalid if the guess isn't in the word list
        if user_guess not in user_word_list:
            valid_guess = False
        
        if valid_guess:
            #Calulcating the color of each letter
            user_check = ""
            answer_check = ""
            fin_check = ""
            for i in range(word_length):
                if user_guess[i] == correct_answer[i]:
                    user_check = user_check + "-"
                    answer_check = answer_check + "_"
                else:
                    user_check = user_check + user_guess[i]
                    answer_check = answer_check + correct_answer[i]
            
            for i in range(word_length):
                if user_check[i] in answer_check:
                    fin_check = fin_check + user_check[i]
                else:
                    fin_check = fin_check + "-"
            
            correct_chars: dict[str, int] = {}
            for i in range(word_length):
                correct_chars.setdefault(answer_check[i], 0)
            for i in range(word_length):
                correct_chars[answer_check[i]]=correct_chars[answer_check[i]]+1
            
            guess_chars: dict[str, int] = {}
            for i in range(word_length):
                guess_chars.setdefault(fin_check[i], 0)
            correct_letters = 0
            for i in range(word_length):
                if user_guess[i] == correct_answer[i]:
                    self.query_one("#l"+str(i+1)).add_class("correct")
                    #Creating a list of correct letters for coloring buttons
                    correct_chars_list.append(user_guess[i])
                    correct_letters = correct_letters + 1
                    #Checking if the user's guess is the correct answer
                    if correct_letters == word_length:
                        correct_guess = True
                        #Telling the game to create the win screen
                        app.post_message(Win())
                elif user_guess[i] == fin_check[i]:
                    guess_chars[fin_check[i]] = guess_chars[fin_check[i]] + 1
                    if guess_chars[fin_check[i]] <= correct_chars[fin_check[i]]:
                        self.query_one("#l"+str(i+1)).add_class("wrongspot")
                        dif_chars_list.append(user_guess[i])
                    else:
                        self.query_one("#l"+str(i+1)).add_class("incorrect")
                else:
                    self.query_one("#l"+str(i+1)).add_class("incorrect")
                    if user_guess[i] not in correct_answer:
                        wrong_chars_list.append(user_guess[i])
                    if wrong_chars_list.count(user_guess[i]) >= 2:
                        wrong_chars_list.remove(user_guess[i])
    def on_win(self, event):
        #Sending the win message to all children
        for i in range(word_length):
            currentlg = self.query_one("#l" + str(i+1))
            currentlg.post_message(Win())
        #Preventing unnecessary event bubbling
        event.stop()


class Yourdle(App):
    CSS_PATH = "Yourdle.tcss"

    def compose(self) -> ComposeResult:
        #Creating the background for the user to enter game settings
        yield UserQueryBackground()
    
    def on_create(self):
        #Tells me the answer to the current game (Will be removed after)
        self.mount(CorrectAnswer())
        #Adding the guess and button containers
        self.mount(GuessContainer())
        self.mount(InputContainer())
    def on_win(self, event):
        #Hiding the answer given at the beginning (Will be removed after)
        self.query_one(CorrectAnswer).add_class("hide")
        #Hiding the game containers
        self.query_one(GuessContainer).add_class("hide")
        self.query_one(InputContainer).add_class("hide")
        #Creating the win screen
        self.mount(WinBackground())
        #Preventing unnecessary event bubbling
        event.stop()
    def on_win_loaded(self, event):
        #Telling the word containers to beam their info to the win screen
        for i in range(user_tries):
            currentwg = app.query_one("#c" + str(i))
            currentwg.post_message(Win())
        #Preventing unnecessary event bubbling
        event.stop()

class CorrectAnswer(Static):
    def compose(self) -> ComposeResult:
        global correct_answer
        #Creates a container that has the correct answer inside
        for i in range(word_length):
            yield Static(correct_answer[i], classes="lc correct")
class Win(Message):
    #Message sent when the game is won
    pass

class WinLoaded(Message):
    #Message sent when the win screen widgets have loaded
    pass

class NewLetterGuess(Message):
    #Message containing information from a letter container
    def __init__(self, color, letter, widget) -> None:
        self.color = color
        self.letter = letter
        self.widget = widget
        super().__init__()
class WinBackground(Static):
    #Loading the container inside the win screen
    def compose(self):
        yield WinContainer()

class WinContainer(Static):
    #Loading the container that contains the past guesses
    def compose(self):
        yield CorrectGuessesContainer()
class CorrectGuessesContainer(Static):
    #The container that has past guesses and correct answer if the user lost
    def compose(self):
        if correct_guess == True:
            yield Label("You win! Here's the guesses you made:",classes="text")
        else:
            yield Label("You lost. Here's the correct answer:",classes="text")
            yield CorrectAnswer()
        
        if correct_guess == False:
            yield Label("Here's the guesses you made:",classes="text")
        for i in range(user_tries):
            yield WordGuessWin(id=("wgw" + str(i)), disabled= True)
        


class WordGuessWin(Static):
    #The version of the container for letters on the win screen
    def compose(self):
        for i in range(word_length):
            #Creating squares for information to be put into
            currentlg_id = ("lgw" + str(i+1))
            print (currentlg_id)
            yield LetterGuess("", id = currentlg_id)
        #Telling the app to begin coloring and adding text to the squares
        if self.id == "wgw"+str(user_tries-1):
            app.post_message(WinLoaded())
    def on_load(self):
        #Telling the letter containers to send their information
        for i in range(word_length):
            currentlg_id = ("lgw" + str(i+1))
            self.query_one("#" + currentlg_id).post_message(Win())
    def on_new_letter_guess(self, event):
        #Recieving the info present in a square, and subsequently applying them
        currentlgw = event.widget
        currentlgw_id = currentlgw.id
        currentlgw_pos = currentlgw_id[-1]
        loadedlgw = self.query_one("#lgw" + str(currentlgw_pos))
        loadedlgw.add_class(event.color)
        loadedlgw.update(event.letter)
        #Preventing unnecessary event bubbling 
        event.stop()

class GuessContainer(Static):
    def compose(self) -> ComposeResult:
        #Creating word containers
        for i in range(num_tries):
            yield WordGuess(id=("c" + str(i)), disabled= True)
    def on_mount(self):
        #Allowing the first word container to be typed into
        self.query_one("#c0").disabled = False
    def on_key(self, event):
        #Preventing unnecessary event bubbling
        event.stop()
    def key_enter(self):
        if valid_guess:
            #Establishing global variables
            global user_tries
            global correct_guess
            #Disabling the current slot for words
            self.query_one("#c" + str(user_tries)).disabled = True
            #Increasing the counter of tries the user has
            user_tries = user_tries + 1
            #Causing the end screen sequence after the user runs out of guesses
            if user_tries == num_tries and not correct_guess:
                app.post_message(Win())
            #Enabling and focusing the next slot for words
            if user_tries != num_tries:
                self.query_one("#c" + str(user_tries)).disabled = False
                self.query_one("#c" + str(user_tries)).query_one("#l1").focus()
            #Coloring buttons when information about the word is gained
            for i in range(len(wrong_chars_list)):
                app.query_one("#b" + wrong_chars_list[i]).variant = "error"
            for i in range(len(dif_chars_list)):
                app.query_one("#b" + dif_chars_list[i]).variant = "warning"
            for i in range(len(correct_chars_list)):
                app.query_one("#b" + correct_chars_list[i]).variant ="success"
    

class InputContainer(Static):
    def compose(self) -> ComposeResult:
        #Creating buttons for every letter
        yield Button("Q", id = "bQ", classes="Ib")
        yield Button("W", id = "bW", classes="Ib")
        yield Button("E", id = "bE", classes="Ib")
        yield Button("R", id = "bR", classes="Ib")
        yield Button("T", id = "bT", classes="Ib")
        yield Button("Y", id = "bY", classes="Ib")
        yield Button("U", id = "bU", classes="Ib")
        yield Button("I", id = "bI", classes="Ib")
        yield Button("O", id = "bO", classes="Ib")
        yield Button("P", id = "bP", classes="Ib")
        yield Button("A", id = "bA", classes="Ib")
        yield Button("S", id = "bS", classes="Ib")
        yield Button("D", id = "bD", classes="Ib")
        yield Button("F", id = "bF", classes="Ib")
        yield Button("G", id = "bG", classes="Ib")
        yield Button("H", id = "bH", classes="Ib")
        yield Button("J", id = "bJ", classes="Ib")
        yield Button("K", id = "bK", classes="Ib")
        yield Button("L", id = "bL", classes="Ib")
        yield Button("Z", id = "bZ", classes="Ib")
        yield Button("X", id = "bX", classes="Ib")
        yield Button("C", id = "bC", classes="Ib")
        yield Button("V", id = "bV", classes="Ib")
        yield Button("B", id = "bB", classes="Ib")
        yield Button("N", id = "bN", classes="Ib")
        yield Button("M", id = "bM", classes="Ib")
    def on_button_pressed(self, event):
        #Sending a key event when a button is pressed
        letter = event.button.id[1]

        currentfocus.post_message(events.Key(key=letter,character=letter))


if __name__ == "__main__":
    #Running the app
    app = Yourdle()
    app.run()