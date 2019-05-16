from ChessProgram import ChessPiece as pieceModule
import numpy as np

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
white_king_row = 7
white_king_col = 4

# piece_to_remove = 0
piece_to_remove = pieceModule.ChessPiece(0, "dummy")

# listOfPawnMoves = np.array([[2, 0], [1, 0], [1, 1], [1, -1]])
# listOfRookMoves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
# listOfCavalierMoves = np.array([[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]])
# listOfBishopMoves = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
# listOfQueenMoves = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]])
# listOfKingMoves = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]])

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
    global white_king_row
    global white_king_col
    global black_king_row
    global black_king_col
    global piece_to_remove

    while 1:
        print_board()
        if is_move_valid:
            if not player:
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
        if new_position[0] not in listOfColumns or new_position[1] not in listOfRows or new_position == current_position:
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
                    continue
                elif is_move_available(piece):
                    chessboard[piece.curr_row][piece.curr_col] = " "
                    piece.last_row = piece.curr_row
                    piece.last_col = piece.curr_col
                    piece.curr_row = piece.new_row
                    piece.curr_col = piece.new_col
                    chessboard[piece.curr_row][piece.curr_col] = piece.type
                    if put_own_king_in_check(player):
                        if piece_to_remove.type != "dummy":     # if there was a piece removed, put it back
                            listOfPieces.append(piece_to_remove)
                            chessboard[piece_to_remove.curr_row][piece_to_remove.curr_col] = str(piece_to_remove.type)
                            piece_to_remove = pieceModule.ChessPiece(0, "dummy")
                            print("here D:")
                        else:
                            chessboard[piece.curr_row][piece.curr_col] = " "
                        piece.curr_row = piece.last_row
                        piece.curr_col = piece.last_col
                        chessboard[piece.curr_row][piece.curr_col] = str(piece.type)
                        is_move_valid = False
                        print("You would be in check")
                        continue

                    if piece.type == king and player == white_player:
                        white_king_row = piece.curr_row
                        white_king_col = piece.curr_col
                    elif piece.type == king and player == black_player:
                        black_king_row = piece.curr_row
                        black_king_col = piece.curr_col

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
            chessboard[piece.curr_row][piece.curr_col] = str(piece.type)


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
    global piece_to_remove

    mvmt = np.array([piece.curr_row - piece.new_row, piece.curr_col - piece.new_col])
    # check if the move is possible for the type of piece
    if piece.type == rook or piece.type == bishop or piece.type == queen:
        if mvmt[0] != 0 and mvmt[1] != 0 and abs(mvmt[0]) != abs(mvmt[1]):
            return False
    if piece.type == pawn:
        if abs(mvmt[0]) == 2 and abs(mvmt[1]) != 0:
            return False
        elif abs(mvmt[1]) > 1 or abs(mvmt[0]) > 2:
            return False
        elif abs(mvmt[1]) == 1 and (abs(mvmt[0]) == 0 or abs(mvmt[0]) > 1):
            return False
        elif (piece.color == white_player and mvmt[0] < 0) or (piece.color == black_player and mvmt[0] > 0):
            return False
        elif abs(mvmt[0]) == 2 and piece.color == 1 and piece.curr_row != 6:
            return False
        elif abs(mvmt[0]) == 2 and piece.color == 0 and piece.curr_row != 1:
            return False
        elif mvmt[1] == 0 and chessboard[piece.new_row][piece.new_col] != " ":
            return False
    elif piece.type == rook and not (mvmt[0] != 0 or mvmt[1] != 0):
        return False
    elif piece.type == cavalier and not((abs(mvmt[0]) == 2 and abs(mvmt[1]) == 1) or (abs(mvmt[0]) == 1 and abs(mvmt[1]) == 2)):
        return False
    elif piece.type == bishop and not abs(mvmt[0]) == abs(mvmt[1]):
        return False
    elif piece.type == queen and not(abs(mvmt[0]) == abs(mvmt[1]) or mvmt[0] == 0 or mvmt[1] == 0):
        return False
    elif piece.type == king and not (abs(mvmt[0]) <= 1 and abs(mvmt[0]) <= 1):
        return False

    # Check if there is no piece in the way
    if piece.type != cavalier:
        row_increment = 0
        col_increment = 0
        if mvmt[0] > 0:
            row_increment = -1
        elif mvmt[0] < 0:
            row_increment = 1
        if mvmt[1] > 0:
            col_increment = -1
        elif mvmt[1] < 0:
            col_increment = 1
        if abs(mvmt[0]) > abs(mvmt[1]):
            for i in range(1, abs(mvmt[0])):
                if chessboard[piece.curr_row + i*row_increment][piece.curr_col + i*col_increment] != " ":
                    print("A piece is blocking the way")
                    return False
        else:
            for i in range(1, abs(mvmt[1])):
                if chessboard[piece.curr_row + i * row_increment][piece.curr_col + i * col_increment] != " ":
                    print("A piece is blocking the way")
                    return False
    # if it removes the opponent's piece
    if chessboard[piece.new_row][piece.new_col] != " " and chessboard[piece.new_row][piece.new_col] != king:
        for elem in listOfPieces:
            if elem.curr_row == piece.new_row and elem.curr_col == piece.new_col:
                if piece.color == elem.color:
                    return False
                piece_to_remove = pieceModule.ChessPiece(elem.color, elem.type)
                piece_to_remove.curr_col = elem.curr_col
                piece_to_remove.curr_row = elem.curr_row
                listOfPieces.remove(elem)
                return True
    return True


def put_own_king_in_check(player):
    global white_king_row
    global white_king_col
    global black_king_row
    global black_king_col

    for elem in listOfPieces:
        if elem.color != player:
            if player == white_player:
                elem.new_row = white_king_row
                elem.new_col = white_king_col
            else:
                elem.new_row = black_king_row
                elem.new_col = black_king_col
            if is_move_available(elem):
                print("danger:", elem.type, " color: ", elem.color, " row: ", listOfRows[elem.curr_row],
                      " col: ", listOfColumns[elem.curr_col])
                return True
    return False


if __name__ == "__main__":
    main()
