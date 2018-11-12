class GameBoard():
    """
    Connect Four
    """

    def __init__(self, cols=5,rows=4,win_length=4):
        if cols < 5 or rows < 4 or win_length<1:
            raise IndexError

        self.cols = cols
        self.rows = rows
        self.win_length = win_length

        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        self.turn = "R"

    def move(self, col):
        if col < 0 or col >= self.cols:
            raise IndexError("Invalid Column")

        if self.board[-1][col]:
            raise IndexError("Unable to place piece, this column is full")

        else:
            for row in range(self.rows):
                if self.board[row][col] is None:
                    self.board[row][col] = self.turn
                    self.change_turn()
                    return

    def change_turn(self):
        if self.turn == "R":
            self.turn = "Y"
        else:
            self.turn = "R"
    
    def print_board(self):
        for r in range(self.rows-1,-1,-1):
            line = ""
            for c in range(self.cols):
                if self.board[r][c]:
                    line += self.board[r][c]
                else:
                    line += " "

            print("|".join(line))

        print("")

    def check_win(self,row,col):
        #TODO
        return False









