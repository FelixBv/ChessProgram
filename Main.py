from ChessProgram import ChessPiece as pieceModule

white_player = True
black_player = False
listOfRows = ["1", "2", "3", "4", "5", "6", "7", "8"]
listOfColumns = ["A", "B", "C", "D", "E", "F", "G", "H"]
listOfPieces = []
pawn = "p"
bishop = "b"
cavalier = "c"
rook = "r"
king = "k"
queen = "q"

black_king_row = 0
black_king_col = 4
white_king_row = 4
white_king_col = 7

listOfPawnMoves = [[2, 0], [1, 0], [1, 1], [1, -1]]
listOfRookMoves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
listOfCavalierMoves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
listOfBishopMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
listOfQueenMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
listOfKingMoves = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]

chessboard = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
]


def main():
    create_pieces()
    player = black_player
    is_move_valid = True

    while 1:
        print_board()
        if is_move_valid:
            if not player:  # player != player    #So White is player == true
                player = white_player
                print("White turn")
            else:
                player = black_player
                print("Black turn")
        else:
            is_move_valid = True
            print("Move invalid, try again")
        current_position = (input('Select a piece: ')).upper()
        if current_position[0] not in listOfColumns or current_position[1] not in listOfRows:
            print("Invalid Position")
            is_move_valid = False
            continue
        new_position = (input('Enter your move: ')).upper()
        if new_position[0] not in listOfColumns or new_position[1] not in listOfRows:
            print("Invalid Position")
            is_move_valid = False
            continue

        piece_type = chessboard[listOfRows.index(current_position[1])][listOfColumns.index(current_position[0])]

        for elem in listOfPieces:
            if elem.type == piece_type and elem.color == player and elem.curr_row == listOfRows.index(
                    current_position[1]) and elem.curr_col == listOfColumns.index(current_position[0]):
                piece = elem
                piece.new_row = listOfRows.index(new_position[1])
                piece.new_col = listOfColumns.index(new_position[0])
                if player != piece.color:
                    is_move_valid = False
                elif is_move_available(piece):
                    chessboard[piece.curr_row][piece.curr_col] = " "
                    piece.last_row = piece.curr_row
                    piece.last_col = piece.curr_col
                    piece.curr_row = piece.new_row
                    piece.curr_col = piece.new_col
                    chessboard[piece.curr_row][piece.curr_col] = piece.type
                else:
                    is_move_valid = False
                break


def create_pieces():
    for i in range(8):
        player = 0
        if i == 6 or i == 7:
            player = 1
        for j in range(8):
            if i == 0 or i == 7:
                if j == 0 or j == 7:
                    piece = pieceModule.ChessPiece(player, rook)
                elif j == 1 or j == 6:
                    piece = pieceModule.ChessPiece(player, cavalier)
                elif j == 2 or j == 5:
                    piece = pieceModule.ChessPiece(player, bishop)
                elif j == 3:
                    piece = pieceModule.ChessPiece(player, queen)
                elif j == 4:
                    piece = pieceModule.ChessPiece(player, king)
                else:
                    break
            elif i == 1 or i == 6:
                piece = pieceModule.ChessPiece(player, pawn)
            else:
                continue
            listOfPieces.append(piece)
            piece.curr_row = i
            piece.curr_col = j
            piece.last_row = i
            piece.last_col = j
            chessboard[piece.curr_row][piece.curr_col] = piece.type


# chessboard[row][col] or [y][x]
def print_board():
    print("    A   B   C   D   E   F   G   H ")
    print("  ---------------------------------")
    print("1 |", ' | '.join(chessboard[0]), "| 1")
    print("2 |", ' | '.join(chessboard[1]), "| 2")
    print("3 |", ' | '.join(chessboard[2]), "| 3")
    print("4 |", ' | '.join(chessboard[3]), "| 4")
    print("5 |", ' | '.join(chessboard[4]), "| 5")
    print("6 |", ' | '.join(chessboard[5]), "| 6")
    print("7 |", ' | '.join(chessboard[6]), "| 7")
    print("8 |", ' | '.join(chessboard[7]), "| 8")
    print("  ---------------------------------")
    print("    A   B   C   D   E   F   G   H ")


def is_move_available(piece):
    if piece.color:
        position = [piece.curr_row - piece.new_row, piece.curr_col - piece.new_col]
    else:
        position = [piece.new_row - piece.curr_row, piece.curr_col - piece.new_col]

    if piece.type != cavalier:
        increment_y = 0
        increment_x = 0
        if position[0] < 0:
            increment_y = -1
        elif position[0] > 0:
            increment_y = 1
        if position[1] < 0:
            increment_x = -1
        elif position[1] > 0:
            increment_x = 1
        if abs(position[0]) > abs(position[1]):
            for i in range(piece.curr_row, piece.new_row, increment_y):
                if chessboard[piece.curr_row + increment_y][piece.curr_col + increment_x] != " ":
                    print("A piece is blocking the way")
                    return False
        else:
            for i in range(piece.curr_col, piece.new_col, increment_x):
                if chessboard[piece.curr_row + increment_y][piece.curr_col + increment_x] != " ":
                    print("A piece is blocking the way")
                    return False
    if piece.type == rook or piece.type == bishop or piece.type == queen:
        if position[0] != 0:
            position[0] = position[0] / position[0]  # ghetto normalisation
        if position[1] != 0:
            position[1] = position[1] / position[1]

    if piece.type == pawn:
        if position not in listOfPawnMoves:
            return False
        elif position[0] == 2 and piece.color == 1 and piece.curr_row != 6:
            return False
        elif position[0] == 2 and piece.color == 0 and piece.curr_row != 1:
            return False
        elif position[1] == 0 and chessboard[piece.new_row][piece.new_col] != " ":
            return False
        elif position[1] != 0 and chessboard[piece.new_row][piece.new_col] == " ":
            return False
    elif piece.type == rook and position not in listOfRookMoves:
        return False
    elif piece.type == cavalier and position not in listOfCavalierMoves:
        return False
    elif piece.type == bishop and position not in listOfBishopMoves:
        return False
    elif piece.type == queen and position not in listOfQueenMoves:
        return False
    elif piece.type == king and position not in listOfKingMoves:
        return False

    if chessboard[piece.new_row][piece.new_col] != " ":
        for elem in listOfPieces:
            if elem.curr_row == piece.new_row and elem.curr_col == piece.new_col:
                piece_to_delete = elem
                if piece.color == piece_to_delete.color:
                    return False
                listOfPieces.remove(piece_to_delete)
                break
    return True


if __name__ == "__main__":
    main()