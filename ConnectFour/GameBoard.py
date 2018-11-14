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
                    if self.check_win(row,col):
                        return True
                    else:
                        self.change_turn()
                        return False

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
        #Check for win along row
        for offset in range(-self.win_length,self.win_length+1):
            count = 0
            if col+offset < 0 or col+offset+self.win_length > self.cols:
                continue
            else:
                for c in range(col+offset,col+offset+self.win_length):
                    if self.board[row][c] == self.turn:
                        count +=1
                    if count == self.win_length:
                        return True

        #Check for win along column
        for offset in range(-self.win_length,self.win_length+1):
            count = 0
            if row+offset < 0 or row+offset+self.win_length > self.rows:
                continue
            else:
                for r in range(row+offset,row+offset+self.win_length):
                    if self.board[r][col] == self.turn:
                        count +=1
                    if count == self.win_length:
                        return True
    
        
        #Check for win along upper diagonal
        """ 
        This isn't working yet
        r-o, c+o
        for offset in range(-self.win_length,self.win_length+1):
            count = 0
            if (row+offset < 0 or row+offset+self.win_length > self.rows or
                col+offset < 0 or col+offset+self.win_length > self.cols):
                continue
            else:
                for o in range(row+offset,row+offset+self.win_length):
                    if self.board[row+o][col+o] == self.turn:
                        count +=1
                    if count == self.win_length:
                        return True
        """

        #Check for win along lower diagonal
        #TODO








