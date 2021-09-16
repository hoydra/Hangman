# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
import requests
from bs4 import BeautifulSoup

hangmanpics = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

victory_figure = ['''
  +---+
  |   |
      |
      |
      |
      |
\ O / |
  |   |
 / \  |      
=========''', '''
  +---+
  |   |
      |
      |
      |
\ O / |
  |   |
 / \  |
      |
=========''']

nouns = []

def rand_word():
    res = requests.get("https://www.wordexample.com/list/most-common-nouns-english")
    soup = BeautifulSoup(res.text, "html.parser")
    words = soup.find_all("span", class_="word-popover")

    for word in words:
        ver = str(word).split("\n\t\t")
        ver1 = ver[1].split("\t</span>")
        nouns.append(ver1[0])

    return nouns


class Hangman:

    secretword = random.choice(rand_word())
    correct = list("_" * len(secretword))
    wrong = []
    guessed = []
    life = 6
    status = ""
    image = 0


    @staticmethod
    def interface():

        try:
            print(hangmanpics[Hangman.image])
            print("".join(Hangman.correct))
            print(f"wrong: {Hangman.wrong}")
            print(Hangman.status)
        except Exception:
            print(f"You lost, the word was {Hangman.secretword}")
            return True

    @staticmethod
    def player():
        Hangman.status = ""

        if Hangman.life > 0 or Hangman.image > 4:
            Hangman.status = "lost"

        if "".join(Hangman.correct) == Hangman.secretword:
            return True

        guess = input(" : ")

        if guess not in Hangman.secretword or guess in Hangman.wrong:
            Hangman.status = f"{guess} is not in the word !"
            Hangman.wrong.append(guess)
            Hangman.life -= 1
            Hangman.image += 1

        if len(guess) != 1:
            Hangman.status = "one letter only ! -1 life"

        if guess.isnumeric():
            Hangman.status = "no numbers ! -1 life"

        if guess in Hangman.guessed:
            Hangman.status = f"{guess} already guessed"

        for count, i in enumerate(list(Hangman.secretword)):

            if guess == i:
                Hangman.guessed.append(guess)
                Hangman.correct[count] = guess

    def game(self):
        end = False
        won = False

        while end == False:
            self.interface()
            if self.player():
                won = True
                end = True
            if self.interface():
                end = True
            if won:

                for i in range(2):
                    print(victory_figure[0])
                    print("You")
                    time.sleep(1)
                    print(victory_figure[1])
                    print("Won!")
                    time.sleep(1)
                    end = True



if __name__ == '__main__':
    game = Hangman()
    game.game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
