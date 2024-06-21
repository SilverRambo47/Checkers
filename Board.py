import numpy as np

class Board:
    def __init__(self, dimension_sizes=(8, 8)):
        self.grid = np.zeros(dimension_sizes, dtype=int)  # Assurez-vous que grid est bien initialisé
        self.initialize_pieces()

    def initialize_pieces(self):
        for row in range(3):  # White pieces
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row, col] = 1  # 1 represents a white piece
        for row in range(5, 8):  # Black pieces
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row, col] = 2  # 2 represents a black piece

    def reset(self):
        self.grid.fill(0)
        self.initialize_pieces()

    def is_valid_move(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return False
        if self.grid[start_row, start_col] == 0 or self.grid[end_row, end_col] != 0:
            return False

        piece = self.grid[start_row, start_col]
        direction = 1 if piece == 1 else -1

        if (end_row - start_row == direction) and abs(end_col - start_col) == 1:
            return True
        if (end_row - start_row == 2 * direction) and abs(end_col - start_col) == 2:
            middle_row, middle_col = (start_row + end_row) // 2, (start_col + end_col) // 2
            if self.grid[middle_row, middle_col] == 3 - piece:
                return True

        return False

    def make_move(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            start_row, start_col = start_pos
            end_row, end_col = end_pos

            piece = self.grid[start_row, start_col]
            self.grid[end_row, end_col] = piece
            self.grid[start_row, start_col] = 0

            if abs(end_row - start_row) == 2:
                middle_row, middle_col = (start_row + end_row) // 2, (start_col + end_col) // 2
                self.grid[middle_row, middle_col] = 0

            if piece == 1 and end_row == 7:
                self.grid[end_row, end_col] = 3
            if piece == 2 and end_row == 0:
                self.grid[end_row, end_col] = 4
        else:
            raise ValueError("Invalid move")
