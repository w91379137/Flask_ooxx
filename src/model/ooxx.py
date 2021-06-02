
space = "　"
x = "Ｘ"
o = "Ｏ"

class OOXXGame():

    turn = 0
    next = x
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
        
        if self.board[index] == space:
            self.board[index] = self.next
            self.turn += 1
            if self.turn % 2 == 0:
                self.next = x
            else:
                self.next = o
