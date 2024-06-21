class Game:
    def __init__(self):
        self.board = None
        self.turn = 'human'  # or 'AI'

    def set_board(self, board):
        self.board = board

    def reset(self):
        if self.board:
            self.board.reset()

    def make_move(self, start_pos, end_pos):
        if self.board:
            self.board.make_move(start_pos, end_pos)
            self.switch_turn()

    def switch_turn(self):
        self.turn = 'AI' if self.turn == 'human' else 'human'