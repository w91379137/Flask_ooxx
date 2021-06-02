
space = "　"
x = "Ｘ"
o = "Ｏ"

win_line_list = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]
class OOXXGame():

    turn = 0
    next = x
    board = []
    winner = None

    def __init__(self):
        self.createBoard()
    
    def createBoard(self):
        new_board = []
        for i in range(9):
            new_board.append(space)
        self.board = new_board
        # print(self.board)

    def clickBoard(self, index):

        if self.winner is not None:
            return
        
        if self.board[index] != space:
            return

        self.board[index] = self.next
        self.turn += 1
        if self.turn % 2 == 0:
            self.next = x
        else:
            self.next = o
        self.checkOver()

    def checkOver(self):
        for win_line in win_line_list:
            if self.board[win_line[0]] != space and self.board[win_line[0]] == self.board[win_line[1]] and self.board[win_line[1]] == self.board[win_line[2]]:
                self.winner = self.board[win_line[0]]
