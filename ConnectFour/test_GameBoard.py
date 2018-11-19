import unittest
import GameBoard

class test_GameBoard(unittest.TestCase):
    
    def test_downward_diag_win(self):
        b = [
                ["R",None,None,None,None],
                ["Y","R",None,None,None],
                ["Y","Y","R",None,None],
                ["Y","Y","Y","R",None]
            ]
        gb = GameBoard.GameBoard()
        gb.board = b
        assert gb.downward_diag_win(0,0) is True
        assert gb.downward_diag_win(1,1) is True
        assert gb.downward_diag_win(2,2) is True
        assert gb.downward_diag_win(3,3) is True
    
    def test_upward_diag_win(self):
        b = [
                ["Y",None,None,"Y",None],
                ["Y","R","Y","R",None],
                ["Y","Y","R","R",None],
                ["Y","Y","Y","R",None]
            ]
        gb = GameBoard.GameBoard()
        gb.board = b
        gb.turn = "Y"
        assert gb.upward_diag_win(3,0) is True
        assert gb.upward_diag_win(2,1) is True
        assert gb.upward_diag_win(1,2) is True
        assert gb.upward_diag_win(0,3) is True

if __name__ == '__main__':
    unittest.main()
