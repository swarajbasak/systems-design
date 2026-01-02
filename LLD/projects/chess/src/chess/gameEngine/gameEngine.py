from color.color import Color

class GameEngine:
    def __init__(self, board):
        self.board = board
        self.current_turn = Color.WHITE
    
    def switch_turn(self):
        if self.current_turn == Color.WHITE:
            self.current_turn = Color.BLACK
        else:
            self.current_turn = Color.WHITE