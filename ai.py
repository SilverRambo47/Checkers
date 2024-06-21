import pandas as pd
import numpy as np

class AI:
    def __init__(self):
        self.moves_dict = {}

    def evaluate_moves(self, board):
        moves = self.get_all_possible_moves(board)
        for move in moves:
            self.moves_dict[move] = self.evaluate_move(board, move)

    def evaluate_move(self, board, move):
        start_pos, end_pos = move
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = board.grid[start_row, start_col]

        score = 0
        direction = 1 if piece == 1 else -1

        if abs(end_row - start_row) == 2:
            score += 10

        if 2 <= end_row <= 5 and 2 <= end_col <= 5:
            score += 3

        if (piece == 1 and end_row == 7) or (piece == 2 and end_row == 0):
            score += 5

        return score

    def get_all_possible_moves(self, board):
        moves = []
        for row in range(8):
            for col in range(8):
                if board.grid[row, col] != 0:
                    piece = board.grid[row, col]
                    direction = 1 if piece == 1 else -1
                    for d_row, d_col in [(direction, 1), (direction, -1), (2 * direction, 2), (2 * direction, -2)]:
                        new_row, new_col = row + d_row, col + d_col
                        if board.is_valid_move((row, col), (new_row, new_col)):
                            moves.append(((row, col), (new_row, new_col)))
        return moves

    def choose_best_move(self):
        best_move = max(self.moves_dict, key=self.moves_dict.get)
        return best_move