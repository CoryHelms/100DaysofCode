class TicTacToe:
    def __init__(self):
        self.board=['' for _ in range(9)]
        self.currentWinner = None
        self
    
    def PrintBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def PrintBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + '| '.join(row) + ' |')

    def availableMoves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves
    
    def emptySquares(self):
        return ' ' in self.board
    
    def numEmptySquares(self):
        return self.board.count(' ')

    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return letter
        return False

    def winner(self, square, letter):
        pass

def play(game, xPlayer, oPlayer, printGame = True):
    if printGame:
        game.printBoardNums()
    
    letter = 'X'

    while game.emptySquares():
        if letter == 'O':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)
        
        if game.makeMove(square, letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.printBoard()
                print('')
        
            if game.currentWinner:
                if printGame:
                    print(letter + ' Wins!')
                return letter

            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
        
        if printGame:
            print('It\'s a tie!')

        
        