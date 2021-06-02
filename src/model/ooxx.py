
space = "　"
x = "Ｘ"
o = "Ｏ"

class OOXXGame():

    board = []

    def __init__(self):
        self.createBoard()
    
    def createBoard(self):
        new_board = []
        for i in range(9):
            new_board.append(space)
        self.board = new_board
        # print(self.board)

    def clickBoard(self, index):
        self.board[index] = x
