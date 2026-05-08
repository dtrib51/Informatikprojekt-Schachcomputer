import chess
import random as rn
from chess_dataset_edit import get_data,split_up_moves
#Geleiches Dictionary als Features, einfach mit den Gewichten dafür.
weights = {
        "pawns": 0,
        "knights": 0,
        "bishops": 0,
        "rooks": 0,
        "queens": 0,
        "legal_moves": 0,
        "doubled_pawns": 0,
        "isolated_pawns": 0,
        "connected_pawns": 0,
        "passed_pawns": 0,
        "good_pawns": 0,
        "good_bishops": 0,
        "good_bishops_2": 0,
        "good_knights": 0,
        "good_rooks": 0,
        "connected_rooks": 0,
        "king_has_castled": 0,
        "king_can_castle": 0,
        "king_in_check": 0,
    }
#Jedes gewicht bekommt am anfang einen zufälligen Wert
for weight in weights:
    weights[weight] += rn.uniform(-1,1)

#trainiert das Perzeptron
def training(data, weights, epochs, learning_rate, bias):
    for epoch in range(epochs):
        #Progressbar/ Zwischenresultate Speichern
        if epoch % 100 == 0:
            print(epoch)
            if epoch % 1000 ==0:
                print(weights)
        #Passt die Gewichte an
        for features, winner in data:
            sum = bias
            for weight in weights:
                sum += weights[weight]*features[weight]
            deviation = winner-sum
            for weight_2 in weights:
                weights[weight_2] += learning_rate * deviation * features[weight_2]
            bias += learning_rate * deviation
    return weights, bias

path = path = "C:/Users/dario/OneDrive/Desktop/School/WF Infromatik/Chess/chess_games.csv"
a,b = training(data = split_up_moves(get_data(path)),weights=weights,epochs=5000,learning_rate=0.00001,bias=0 )

print(a)
print(b)