from abc import ABC, abstractmethod
from color.color import Color

class ChessPiece(ABC):
    def __init__(self, color: Color, name: str, position: tuple):
        self.color = color
        self.name = name
        self.position = position
        self.is_active = True

    @abstractmethod
    def is_valid_move(self, new_position: tuple, board) -> bool:
        pass

    def move(self, new_position: tuple) -> bool:
        if self.is_valid_move(new_position):
            self.position = new_position
            return True
        return False