from piece import ChessPiece
from color.color import Color

class Pawn(ChessPiece):
    def __init__(self, color: str, position: tuple, is_first_move: bool = True):
        super().__init__(color, "PAWN", position)
        self.is_first_move = is_first_move

    def is_valid_move(self, destination: tuple, board) -> bool:
        # white moves from 1 to 8
        # black moves from 8 to 1
        # if pawn in moving first time, it can move 2 rows
        # can move diagonally -> TO DO
        prev_x, prev_y = self.position[0], self.position[1]
        new_x, new_y = destination[0], destination[1]
        direction = -1 if self.color == Color.BLACK else 1

        if new_y == prev_y:
            if new_x == prev_x + direction:
                return board.get_piece_at(destination) is None

            if self.is_first_move and new_x == prev_x + (2 * direction):
                square_in_front = (prev_x + direction, prev_y)
                return board.get_piece_at(square_in_front) is None and board.get_piece_at(destination) is None
        elif abs(prev_y - new_y) == 1 and (new_x - prev_y) == direction:
            target_piece = board.get_piece_at(destination)

            return target_piece is not None and target_piece.color != self.color

        return False


