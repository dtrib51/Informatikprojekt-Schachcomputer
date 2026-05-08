# Informatikprojekt-Schachcomputer
Programme:
Chess_vs_Bot.py = Hauptprogramm: Gegen den Bot spielen
chess_manual_eval.py = Führt die Evaluation der Position durch und extrahiert die Features aus der Position
chess_dataset_edit.py = Passt die Daten für das Perzeptron an
chess_Perzeptron.py = Trainiert das Perzeptron
Minimax_chess.py = Führt den Minimax-Algorithmus aus und wählt die besten 50% der Züge aus
chess_games.csv = Datensatz, den ich verwendet habe

Chess_dataset_edit.py und chess_Perzeptron.py müssen Sie nicht öffnen, da ich die Gewichte bereits im Voraus trainiert habe.

In Chess_vs_Bot.py können Sie gegen den Bot spielen. Das Programm gibt den Zug und die Evaluation in der Konsole aus und stellt das Schachbrett dar. Die Darstellung ist von python-chess und ist nicht sehr übersichtlich. Ich fand es einfacher, die Züge auf ein Onlinebrett zu übertragen, zum Beispiel:
https://www.365chess.com/analysis_board.php

Sie müssen Ihren Zug in der Konsole im UCI-Format eingeben:

- Normaler Zug: e2e4
- Rochade: Anfangsfeld des Königs + Zielfeld des Königs, z. B. e1g1
- Umwandlung: Zug + Buchstabe der gewünschten Figur, z. B. a7a8q
Beispiel: e2e4 bedeutet, dass der Bauer von e2 nach e4 zieht.

Gewichte (schon im Programm): {'pawns': -0.0865842893403609, 'knights': 0.2142580746469879, 'bishops': 0.28789284240878116, 'rooks': 0.3555097478918298, 'queens': 0.6156249907585952, 'legal_moves': 0.0025973905564111023, 'doubled_pawns': -0.06329057300666685, 'isolated_pawns': 0.2070744338662182, 'connected_pawns': 0.22958824933375124, 'passed_pawns': -0.00016018103927607126, 'good_pawns': 0.06765805338553976, 'good_bishops': 0.06349670933448692, 'good_bishops_2': 0.059218349826875925, 'good_knights': 0.07725094671692503, 'good_rooks': 0.07295828668211636, 'connected_rooks': 0.003480404323767182, 'king_has_castled': -0.0025140768108256675, 'king_can_castle': -0.059472909344017916, 'king_in_check': -0.11073303687542309}

Hier ein paar Beispielsspiele:


Gegen Mich(Schwarz) auf Depth 3:
71.8% Accuracy
1. Nf3 Nf6 2. Ne5 $6 d6 3. Nc4 $6 e5 4. Nc3 Bf5 $6 5. e4 $6 Nxe4 6. Nxe4 $2 Bxe4 7. d3
Bc6 $2 8. Qe2 $9 Be7 9. Be3 $6 Bg5 $2 10. Bxg5 $2 Qxg5 11. h4 Qf6 12. h5 Qg5 $6 13. d4
Bxg2 $2 14. Rg1 Bxf1 15. Kxf1 (15. Qxf1) 15... Qf6 $6 16. dxe5 dxe5 17. Nxe5 O-O $1
18. Re1 Nc6 19. Nxc6 $9 Qxc6 20. Qd3 $6 Rfe8 $6 21. Rxe8+ Rxe8 22. h6 $2 g6 $9 23. f3
Qa4 $2 24. Rg4 Qxa2 25. Kg2 $2 Qxb2 26. Rd4 a5 27. Rd8 Kf8 $1 28. Qd2 a4 29. Kh3 $6 a3
30. Qd7 Qe5 $1 31. Rxe8+ Qxe8 32. Qg4 $6 a2 33. Qb4+ Qe7 34. c3 Qxb4 35. cxb4 a1=Q
36. b5 f5 37. Kg3 $6 Qg1+ 38. Kf4 b6 39. Ke5 Qe3+ 40. Kf6 Qe7# 0-1


Gegen Stockfish18(Schwarz) auf Depth 3:
70.1% Accuracy, 

1. Nf3 d5 2. Nc3 $6 d4 3. Ne4 Nf6 $6 4. Nxf6+ exf6 5. Rg1 $2 c5 6. g4 $2 Bd6 $6 7. Rg2 $2
O-O $6 8. Rg1 $6 Nc6 9. h3 Re8 10. Bg2 f5 11. g5 Bd7 12. Bh1 Re7 13. Bg2 Qa5 14.
a4 Rae8 15. Bh1 Nb4 16. Bg2 Rxe2+ 17. Qxe2 Nxc2+ 18. Kf1 Rxe2 19. Kxe2 d3+ 20.
Kxd3 Nxa1 21. Re1 $2 Bb5+ 22. axb5 Qxb5+ 23. Ke3 Nc2# 0-1
