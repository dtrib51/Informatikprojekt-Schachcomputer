import chess
import random as rn
from Minimax_chess import minimax

chess_board = chess.Board()

#Zufällige Farb Zuteillung
white_or_black = rn.randint(0,1)
if white_or_black == 0:
    Bot_white = True
else:
    Bot_white = False

#Parameter für den Bot: Weights wurden im Voraus berechnet
bot_depth = 3
bot_weights = {'pawns': -0.0865842893403609, 'knights': 0.2142580746469879, 'bishops': 0.28789284240878116, 'rooks': 0.3555097478918298, 'queens': 0.6156249907585952, 'legal_moves': 0.0025973905564111023, 'doubled_pawns': -0.06329057300666685, 'isolated_pawns': 0.2070744338662182, 'connected_pawns': 0.22958824933375124, 'passed_pawns': -0.00016018103927607126, 'good_pawns': 0.06765805338553976, 'good_bishops': 0.06349670933448692, 'good_bishops_2': 0.059218349826875925, 'good_knights': 0.07725094671692503, 'good_rooks': 0.07295828668211636, 'connected_rooks': 0.003480404323767182, 'king_has_castled': -0.0025140768108256675, 'king_can_castle': -0.059472909344017916, 'king_in_check': -0.11073303687542309}
bot_bias = 0

while not chess_board.is_game_over():
    print(chess_board)
    moved = False

    #Zugwahl
    while not moved:  
        if chess_board.turn:
            if Bot_white:
                print("White to move. Computer Thinking...")
                a,move = minimax(chess_board, bot_depth,bot_weights,bot_bias)
                print(move)
                print(a)
            else:
                print("White to move. Please enter your move")
                move_input = input()
                move = chess.Move.from_uci(move_input)
        else:
            if Bot_white:
                print("Black to move. Please enter your move")
                move_input = input()
                move = chess.Move.from_uci(move_input)
            else:
                print("Black to move. Computer Thinking...")
                a,move = minimax(chess_board, bot_depth,bot_weights,bot_bias)
                print(move)
                print(a)
    #Zug machen
        if move in chess_board.legal_moves:
            chess_board.push(move)
            moved = True
        else:
            print("You entered an Illegal move, Please try again")

result = chess_board.result()
print(f"Checkmate", result)
if result == "1-0":
    print("White wins")
elif result == "0-1":
    print("Black wins")
elif result == "1/2-1/2":
    print("Draw")