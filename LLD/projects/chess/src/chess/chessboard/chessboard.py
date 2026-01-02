class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        # ... (initialization logic)

    def setup_board(self):
        ...
        
    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece_at(start_pos)
        
        # Update the grid
        self.grid[start_pos[0]][start_pos[1]] = None
        self.grid[end_pos[0]][end_pos[1]] = piece
        
        # Update the piece's knowledge of its position
        if piece:
            piece.move(end_pos)