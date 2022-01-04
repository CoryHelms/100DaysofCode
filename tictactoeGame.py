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
        numberBoad = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + '| '.join(row) + ' |')

    def availableMoves(self):
        pass