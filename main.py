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
    SECRETWORD = random.choice(rand_word())
    print(SECRETWORD)
    correct = list("_" * len(SECRETWORD))
    wrong = []
    life = 6
    image = 0


    @staticmethod
    def interface():
        print(hangmanpics[Hangman.image])
        print("".join(Hangman.correct))

    @staticmethod
    def player():

        if "".join(Hangman.correct) == Hangman.SECRETWORD:
            return True

        guess = input(" : ")
        if len(guess) != 1:
            print("one letter only ! -1 life")

        if guess.isnumeric():
            print("no numbers ! -1 life")

        if guess not in Hangman.SECRETWORD or guess in Hangman.wrong:
            print(f"{guess} is not in the word !")
            Hangman.wrong.append(guess)
            Hangman.life -= 1
            Hangman.image += 1

        # make a function to not accept duplicates, so if we write m and then m again one life -= 1



        for count,i in enumerate(list(Hangman.SECRETWORD)):

            if guess == i:
                Hangman.correct[count] = guess

    def game(self):
        end = False
        won = False
        while end == False:
            self.interface()
            if self.player():
                won = True
            if won:
                for i in range(5):
                    print(victory_figure[0])
                    time.sleep(1)
                    print(victory_figure[1])
                    time.sleep(1)

                    end = True


if __name__ == '__main__':
    game = Hangman()
    game.game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
