import chess
from chess_manual_eval import evaluate_position


def minimax(board, depth, weights, bias):
    #Falls Schachmatt oder unentscheiden.
    if board.is_game_over():
        if board.is_checkmate():
            if board.turn == chess.WHITE:
                return -999999, None
            else:
                return 999999, None
        return 0, None
    #Rekursiver Loop brechen
    if depth == 0:
        return evaluate_position(board, weights, bias), None
    
    best_move = None
    possible_moves = list(board.legal_moves)
    if board.turn == chess.WHITE:
        best_evaluation = -99999999999999 #Sehr Teife Evaluation, damit it es sicher einen Zug gibt mit einer bessere Evaluation.
        for move in possible_moves:
            #Macht den Zug, evaluariert die Position und macht den Zug rückgängig
            board.push(move)
            evaluation, move_2 = minimax(board,depth-1,weights,bias)
            board.pop()
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                best_move = move
    else:
        best_evaluation = 99999999999999
        for move in possible_moves:
            board.push(move)
            evaluation, move_2 = minimax(board,depth-1,weights,bias)
            board.pop()
            if evaluation < best_evaluation:
                best_evaluation = evaluation
                best_move = move
    return best_evaluation, best_move

#Nimmt nur die besten 50% der Züge: Minimax kann schneller durchgeführt werden.
def best_moves(board,weights,bias,percentage):
    possible_moves = board.legal_moves
    evals = []
    for move in possible_moves:
        board.push(move)
        evaluation = evaluate_position(board,weights,bias)
        evals.append((evaluation,move))
        board.pop()
    #Sagt dem Programm ob es die Liste nach rückwerts oder nicht sortieren muss
    min = False
    if board.turn == chess.BLACK:
        min = True
    evals.sort(key=lambda x:x[0],reverse=min)
    percentage = int(len(evals)*percentage)
    evals = evals[:percentage]
    return evals