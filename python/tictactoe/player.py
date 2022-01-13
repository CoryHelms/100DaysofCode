import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.availableMoves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                valideSquare = True
            except ValueError:
                print('Invalid square. Try again.')