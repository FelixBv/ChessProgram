class ChessPiece:
    def __init__(self, color, type):
        self.type = type
        self.color = color
        self.last_row = 9
        self.last_col = 9
        self.curr_row = 9
        self.curr_col = 9
        self.new_row = 9
        self.new_col = 9

    def current_position(self, row, col):
        self.curr_row = row
        self.curr_col = col

    def new_position(self, row, col):
        self.new_row = row
        self.new_col = col
