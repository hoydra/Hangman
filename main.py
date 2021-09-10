# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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



class Hangman:
    SECRETWORD = "bromeem"
    correct = list("_" * len(SECRETWORD))
    life = 6
    image = 0




    def interface(self):
        print(hangmanpics[Hangman.image])
        print("".join(Hangman.correct))



    def player(self):
        guess = input(" : ")
        if len(guess) != 1:
            print("Error")

        if guess not in Hangman.SECRETWORD:
            Hangman.life -= 1
            Hangman.image += 1
            print(Hangman.life)
           # print(hangmanpics[Hangman.image])


        for count,i in enumerate(list(Hangman.SECRETWORD)):
            if guess == i:
                Hangman.correct[count] = guess










    def game(self):
        end = False
        while end == False:
            self.interface()
            self.player()
            if "_" not in Hangman.correct:
                end = True

# Press the green button in the gutter to run the script.







if __name__ == '__main__':
    game = Hangman()
    game.game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
