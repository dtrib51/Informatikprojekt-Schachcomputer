import numpy as np
import chess
from chess_manual_eval import get_features

#Csv in Python Liste umwandeln, jeweils 1 Spiel = 1 Tuple mit der End Position und wer das Spiel gewonnen hat
def get_data(path):
    games = []
    data = np.loadtxt(path,delimiter=",", skiprows=1,dtype=str,)
    for game in data:
        winner = game[0]
        position = game[1]
        if winner == "White":
            score = 1
        elif winner == "Black":
            score = -1
        else: 
            score = 0
        games.append((position,score))
    return games

#Für jeden Zug in einem Spiel werden alle Features ausgenommen. Jede Position in einem Spiel wird zur eigenen Date für das Training
def split_up_moves(data):
    board = chess.Board()
    final_data = []
    for game in data:
        board.reset()
        winner = game[1]
        moves = game[0]
        for move in moves.split():
            board.push_san(move)
            features = get_features(board)
            final_data.append((features, winner))
    return final_data

path = "C:/Users/dario/OneDrive/Desktop/School/WF Infromatik/Chess/chess_games.csv"
