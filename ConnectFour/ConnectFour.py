import GameBoard


def main():
    gb = GameBoard.GameBoard()
    running = True
    gb.print_board()
    while running:
        
        turn = gb.turn
        try:
            col = int(input("Player {} - Which column do you want to place a piece?\n".format(turn)))
            if not gb.valid_col(col):
                raise IndexError
            if gb.move(col):
                print("Congats, player {} wins!\n".format(turn))
                running = False
        except:
            print("Invalid Move\n")
        finally:
            gb.print_board()

if __name__ == "__main__":
    main()