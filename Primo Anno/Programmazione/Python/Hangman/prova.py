from tkinter import *
import platform
from PIL import Image, ImageTk
from random_word import RandomWords
from colorama import Fore
from colorama import Style

class HangmanGame:
    def __init__(self):
        self.window_width = 600
        self.window_height = 600
        self.title = "Hangman Game"
        self.root = Tk()
        self.used_chr = set()
        self.buttons = set()
        self.hangman = Hangman()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (self.window_width // 2)
        y = (screen_height // 2) - (self.window_height // 2)

        resolution = f"{self.window_width}x{self.window_height}+{x}+{y}"

        self.root.geometry(resolution)
        self.root.title(self.title)
        self.root.resizable(False, False)

        os_name = platform.system()

        if os_name == 'Windows':
            icon_path = 'img/hangman-game.ico'
        if os_name == 'Linux':
            icon_path = 'img/hangman-game.xbm'

        self.root.iconbitmap(icon_path)

        self.menu = Frame(self.root, borderwidth=2,
                          relief="solid", width=100, height=150)
        self.menu.grid(column=0, row=0)

        self.title_frame = Frame(
            self.root, borderwidth=2, relief="solid", width=400, height=150)
        self.title_frame.grid(column=1, row=0)

        self.times = Frame(self.root, borderwidth=2,
                           relief="solid", width=100, height=150)
        self.times.grid(column=2, row=0)

        self.word = Frame(self.root, borderwidth=2,
                          relief="solid", width=600, height=150)
        self.word.grid(column=0, row=1, columnspan=3)
        self.word_to_guess_label = Label(self.word, text='__________________')
        #self.word_to_guess_label.pack()
        

        self.input_frame = Frame(self.root, width=400, height=100)
        self.input_frame.grid(column=0, row=2, columnspan=3)

        self.input_buttons = Frame(
            self.root, borderwidth=2, relief="solid", width=600, height=200)
        self.input_buttons.grid(column=0, row=3, columnspan=3, pady=20)

        self.input_guess = Entry(
            self.input_frame, width=48, font=('courier', 8, 'bold'))
        Label(self.input_frame, text='Used Characters', pady=15,
              fg='black', font=('Arial', 8)).grid(column=0, row=0, padx=5)
        self.input_guess.grid(column=1, row=0, columnspan=2)
        Label(self.input_frame, text='Make a Guess..', pady=15, fg='red',
              font=('Arial', 12, 'bold')).grid(column=0, row=1, columnspan=3)

        self.buttons_per_row = 10
        for i, char in enumerate(range(ord('a'), ord('z') + 1)):
            button = self.create_button(chr(char))
            self.buttons.add(button)
            button.grid(row=i // self.buttons_per_row, column=i %
                        self.buttons_per_row, padx=5, pady=5)

        self.restart_button = Button(self.input_buttons, text='Restart',
                                     command=self.restart,
                                     cursor='hand2',
                                     borderwidth=1,
                                     fg='black',
                                     background='white',
                                     width=10,
                                     height=2)
        self.restart_button.grid(
            row=i // self.buttons_per_row, column=(i % self.buttons_per_row) + 1, columnspan=5)

        self.title_window = Label(self.title_frame, text=self.title, font=(
            'Arial', 15, 'bold'), fg='red', pady=50, padx=50)
        self.title_window.grid(row=0, column=1)

        image = Image.open("img/hangman-game.png")
        image = image.resize((80, 80))
        self.photo = ImageTk.PhotoImage(image)
        self.label_img = Label(self.title_frame, image=self.photo)
        self.label_img.grid(row=0, column=0)

    def set_state(self, st: str, widget):
        widget.config(state=st)

    def set_chr(self, char: str, text: Entry, btn: Button):
        self.set_state(NORMAL, text)
        text.insert(END, char)
        self.set_state(DISABLED, text)
        self.used_chr.add(char)
        self.set_state(DISABLED, btn)

        # Update the hangman game state
        self.hangman.setChar(char)
        self.hangman.makeGuess()
        self.hangman.printWord()

    def restart(self):
        for btn in self.buttons:
            self.set_state(NORMAL, btn)
        self.input_guess.config(state=NORMAL)
        self.input_guess.delete(0, END)
        self.hangman = Hangman()  # Reset hangman game state

    def create_button(self, char: str):
        btn = Button(self.input_buttons,
                     text=char,
                     cursor='hand2',
                     borderwidth=1,
                     fg='black',
                     background='white',
                     width=3,
                     height=2,
                     command=lambda ch=char: self.set_chr(ch, self.input_guess, btn))
        return btn

    def run(self):
        self.root.mainloop()

class Hangman:
    def __init__(self):
        self.word = ""
        self.char = ""
        self.__wordIndex = ""
        self.__charUsed = []
        self.__displayChars = []
        self.__BOLD = "\033[1m"
        self.__END = "\033[0m"
        self.__MESSAGES = {
            "WIN": f"{Fore.GREEN}{self.__BOLD}You Won!{self.__END}{Style.RESET_ALL}",
            "LOSE": f"{Fore.RED}{self.__BOLD}You Lost!{self.__END}{Style.RESET_ALL}",
            "USED": f"{Fore.RED} already used...{Style.RESET_ALL}",
            "INPUT_ERROR": f"{Fore.RED}Enter only one character!{Style.RESET_ALL}",
            "WORD": f"{Fore.RED}The word to guess was:{Style.RESET_ALL}",
        }

        self.random_words = RandomWords()
        self.word = self.random_words.get_random_word().lower()
        self.__wordIndex = "_" * len(self.word)
        self.__displayChars = ["_"] * len(self.word)

    def checkInput(self, char):
        if len(char) != 1 or char == "":
            return False
        else:
            return True

    def getIndexes(self):
        indexes, index = [], 0
        for i in range(len(self.word)):
            if self.__wordIndex[i] == self.char:
                index = self.__wordIndex.index(self.char)
                self.__wordIndex = self.__wordIndex.replace(self.char, "_", 1)
                indexes.append(index)
        return indexes

    def insertChar(self):
        if not self.char in self.__charUsed and len(self.char) == 1:
            self.__charUsed.append(self.char)

    def makeGuess(self):
        if self.char in self.word and self.char != "":
            return True
        else:
            return False

    def setChar(self, char):
        if self.checkInput(char):
            self.char = char
        else:
            self.char = ""
            print(self.__MESSAGES["INPUT_ERROR"])

    def printWord(self):
        for char in self.__displayChars:
            print(f"{Fore.YELLOW}{char}{Style.RESET_ALL}", end=" ")
        print()

    def playGame(self):
        i = 0
        while "".join(self.__displayChars) != self.word and i < len(self.word) + (
            len(self.word) // 2
        ):
            self.setChar(input(f"{Fore.BLUE}Try to guess...{Style.RESET_ALL}\n>>"))
            if not (self.char in self.__charUsed):
                self.insertChar()
                res = self.makeGuess()
                if res:
                    indexes = self.getIndexes()
                    for j in indexes:
                        self.__displayChars[j] = self.char
                self.printWord()
            else:
                print(f"{Fore.CYAN}'{self.char}'" + self.__MESSAGES["USED"])
            i += 1
        if "".join(self.__displayChars) == self.word:
            print(self.__MESSAGES["WIN"])
        else:
            print(self.__MESSAGES["LOSE"])
            print(
                self.__MESSAGES["WORD"]
                + f" {Fore.MAGENTA}{self.__BOLD}{self.word}{self.__END}{Style.RESET_ALL}"
            )

game = HangmanGame()
game.run()
