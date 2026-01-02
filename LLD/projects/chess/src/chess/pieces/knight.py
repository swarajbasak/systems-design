from piece import ChessPiece

class Knight(ChessPiece):
    def __init__(self, color, position: tuple):
        super().__init__(color, "KNIGHT", position)

    def is_valid_move(self, new_position, board) -> bool:
        new_x, new_y = new_position[0], new_position[1]
        prev_x, prev_y = self.position[0], self.position[1]
        destination_piece = board.get_piece_at(new_position)
        return (destination_piece is None or destination_piece.color != self.color) and (abs(new_x - prev_x) == 2 and abs(new_y - prev_y) == 1) or (abs(new_x - prev_x) == 1 and abs(new_y - prev_y) == 2)
    

"""
5, 5 (x, y)
 
3, 4 (x - 2, y - 1)

3, 6 (x - 2, y + 1)

7, 4 (x + 2, y - 1)
 
7, 6 (x + 2, y + 1)
"""