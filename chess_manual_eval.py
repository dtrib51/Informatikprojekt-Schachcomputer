import chess
import random as rn


def get_features(chess_board):
    #Material Eval
    pieces = {"P":0,"N":0,"B":0,"R":0,"Q":0, "K":0}

    for square, piece in chess_board.piece_map().items():
        if piece.color == chess.WHITE:
            pieces[str(piece)] += 1
        else:
            pieces[str(piece).upper()] -= 1
            

    #mobility Eval (The more active pieces, the more moves you can play)
    legal_moves = 0
    if chess_board.turn:
        legal_moves += len(list(chess_board.legal_moves))
    else:
        legal_moves -= len(list(chess_board.legal_moves))

    # pawn structure Eval
    pawn_list_white = []
    pawn_list_black = []
    doubled_pawns = 0
    passed_pawns = 0
    isolated_pawns = 0
    connected_pawns = 0


    #punishes doubled pawns
    for square, piece in chess_board.piece_map().items():
        if piece.symbol() == "P":
            if (square%8) in pawn_list_white:
                doubled_pawns += 1
            pawn_list_white.append((square%8))
        elif piece.symbol() == "p":
            if (square%8) in pawn_list_black:
                doubled_pawns -= 1
            pawn_list_black.append((square%8))
    #rewards pawns with another next to them or passed pawns, punishes isolated pawns
    for file in pawn_list_white:
        if (file+1) in pawn_list_white or (file-1) in pawn_list_white:
            connected_pawns +=1
        else:   
            isolated_pawns +=1
        if file not in pawn_list_black and (file+1) not in pawn_list_black and  (file-1) not in pawn_list_black:
            passed_pawns +=1
    for file in pawn_list_black:
        if (file+1) in pawn_list_black or (file-1) in pawn_list_black:
            connected_pawns -=1
        else: 
            isolated_pawns -=1
        if file not in pawn_list_white and (file+1) not in pawn_list_white and  (file-1) not in pawn_list_white:
            passed_pawns -=1

    #if pieces are on a good square rewarded:
    #pawns = good if in last 3 rows, or in the center., #nights in the middle of the board, bishops in the 3 longest coloumms, rooks in an open file or both connected.
    good_pawns = 0
    good_bishops = 0
    good_bishops_2 = 0
    good_knights = 0
    good_rooks = 0
    connected_rooks = 0
    bishop_good_squares = [[0,9,18,27,36,45,54,63,7,14,21,28,35,42,49,56],[1,6,8,10,13,15,17,19,20,22,26,29,34,37,41,43,44,46,48,50,53,55,57,62]]
    knight_good_sqaures = [18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]
    rooks_white = []
    rooks_black = []

    for square, piece in chess_board.piece_map().items():
        #pawns = good if in the last 3 rows (danger of promoting)
        if piece.symbol() == "P":
            if 31 < int(square) < 56:
                good_pawns += 1
        elif piece.symbol() == "p":
            if 7 < int(square) < 32:
                good_pawns -= 1
        #Bishops = Verg good if in longest diagonal, good if in 3 longest diagonals
        elif piece.symbol() =="B":
            if int(square) in bishop_good_squares[0]:
                good_bishops_2 +=1
            elif int(square) in bishop_good_squares[1]:
                good_bishops +=1
        elif piece.symbol() =="b":
            if int(square) in bishop_good_squares[0]:
                good_bishops_2 -=1
            elif int(square) in bishop_good_squares[1]:
                good_bishops -=1
        #Knights = good if in center 
        elif piece.symbol() == "N":
            if int(square) in knight_good_sqaures:
                good_knights += 1
        elif piece.symbol() == "n":
            if int(square) in knight_good_sqaures:
                good_knights -= 1
        #rooks = good if in empty file
        elif piece.symbol() == "R":
            if int(square) % 8 not in pawn_list_white and int(square) % 8 not in pawn_list_black:
                good_rooks += 1
                rooks_white.append(square)
                
        elif piece.symbol() == "r":
            if int(square) % 8 not in pawn_list_white and int(square) % 8 not in pawn_list_black:
                good_rooks -= 1
                rooks_black.append(square)
        #rooks = very good if connected (no pieces in between)
    if len(rooks_white) == 2:
        if rooks_white[0] % 8 == rooks_white[1] % 8 or rooks_white[0]//8 == rooks_white[1]//8:
            connected_counter = 0
            between = chess.SquareSet(chess.between(rooks_white[0], rooks_white[1]))            
            for square in between:
                if not chess_board.piece_at(square):
                    connected_counter += 1
            if connected_counter == len(between):
                connected_rooks += 1
    if len(rooks_black) == 2:
        if rooks_black[0] % 8 == rooks_black[1] % 8 or rooks_black[0]//8 == rooks_black[1]//8:
            connected_counter = 0
            between = chess.SquareSet(chess.between(rooks_black[0],rooks_black[1]))
            for square in between:
                if not chess_board.piece_at(square):
                    connected_counter += 1
            if connected_counter == len(between):
                connected_rooks -= 1

    #King saftey: if castled, can castle, not in check
    king_has_castled = 0
    king_can_castle = 0
    king_in_check = 0

    if chess_board.turn:
        if not chess_board.has_castling_rights(chess.WHITE):
            if chess_board.king(chess.WHITE)in [chess.G1,chess.C1]:
                king_has_castled += 1
            if chess_board.is_check():
                king_in_check += 1
        else:
            king_can_castle += 1
            
    else:
        if not chess_board.has_castling_rights(chess.BLACK):
            if chess_board.king(chess.BLACK)in [chess.G1,chess.C1]:
                king_has_castled -= 1
            if chess_board.is_check():
                king_in_check -= 1
        else:
            king_can_castle -=0.5

    features = {
        "pawns": pieces["P"],
        "knights": pieces["N"],
        "bishops": pieces["B"],
        "rooks": pieces["R"],
        "queens": pieces["Q"],
        "legal_moves": legal_moves,
        "doubled_pawns": doubled_pawns,
        "isolated_pawns": isolated_pawns,
        "connected_pawns": connected_pawns,
        "passed_pawns": passed_pawns,
        "good_pawns": good_pawns,
        "good_bishops": good_bishops,
        "good_bishops_2": good_bishops_2,
        "good_knights": good_knights,
        "good_rooks": good_rooks,
        "connected_rooks": connected_rooks,
        "king_has_castled": king_has_castled,
        "king_can_castle": king_can_castle,
        "king_in_check": king_in_check,
    }
    return features

def evaluate_position(board, weights, bias):
    features = get_features(board)
    eval = bias
    for weight in weights:
        eval += weights[weight] * features[weight]
    return eval