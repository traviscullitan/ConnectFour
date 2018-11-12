import GameBoard


def main():
    gb = GameBoard.GameBoard()
    gb.print_board()
    for i in range(5):
        try:
            gb.move(0)
            gb.print_board()
        except IndexError:
            print("Invalid Move")

if __name__ == "__main__":
   main()