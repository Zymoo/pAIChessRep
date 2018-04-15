import math
import chess
import chess.svg
import chess.variant
from random import *

pieceScore = { 'P': 100, 'N': 280, 'B': 320, 'R': 479, 'Q': 929, 'K': 6000,'p': 100, 'n': 280, 'b': 320, 'r': 479, 'q': 929, 'k': 6000 }

#biale maja niskie numery indeksow A1=0, B1=2
piecesPositionEvaluationWhite = {
    'P': (  0 ,  0 , 0 ,  0 ,  0 ,  0 , 0 , 0 ,
            -31 ,8 ,-7 ,-37 ,-36 ,-14 ,3 ,-31 ,
            -22 ,9 ,5 ,-11 ,-10 ,-2 ,3 ,-19 ,
            -26 ,3 ,10 ,9 ,6 ,1 ,0 ,-23 ,
            -17 ,16 ,-2 ,15 ,14 ,0 ,15 ,-13 ,
            7 ,29 ,21 ,44 ,40 ,31 ,44 ,7 ,
            78 ,83 ,86 ,73 ,102 ,82 ,85 ,90 ,
            0, 0, 0, 0, 0, 0, 0, 0,),

    'N': (-74 ,-23 ,-26 ,-24 ,-19 ,-35 ,-22 ,-69 ,
            -23 ,-15 ,2 ,0 ,2 ,0 ,-23 ,-20 ,
            -18 ,10 ,13 ,22 ,18 ,15 ,11 ,-14 ,
            -1 ,5 ,31 ,21 ,22 ,35 ,2 ,0 ,
            24 ,24 ,45 ,37 ,33 ,41 ,25 ,17 ,
            10 ,67 ,1 ,74 ,73 ,27 ,62 ,-2 ,
            -3 ,-6 ,100 ,-36 ,4 ,62 ,-4 ,-14 ,
            -66 ,-53 ,-75 ,-75 ,-10 ,-55 ,-58 ,-70),

    'B': ( -7 ,2 ,-15 ,-12 ,-14 ,-15 ,-10 ,-10 ,
            19 ,20 ,11 ,6 ,7 ,6 ,20 ,16 ,
            14 ,25 ,24 ,15 ,8 ,25 ,20 ,15 ,
            13 ,10 ,17 ,23 ,17 ,16 ,0 ,7 ,
            25 ,17 ,20 ,34 ,26 ,25 ,15 ,10 ,
            -9 ,39 ,-32 ,41 ,52 ,-10 ,28 ,-14 ,
            -11 ,20 ,35 ,-42 ,-39 ,31 ,2 ,-22 ,
            -59 ,-78 ,-82 ,-76 ,-23 ,-107 ,-37 ,-50),

    'R': (  -30 ,-24 ,-18 ,10 ,-2 ,-18 ,-31 ,-32 ,
            -53 ,-38 ,-31 ,-26 ,-29 ,-43 ,-44 ,-53 ,
            -42 ,-28 ,-42 ,-25 ,-25 ,-35 ,-26 ,-46 ,
            18 ,-35 ,-16 ,-21 ,-13 ,-29 ,-46 ,10 ,
            20 ,5 ,16 ,13 ,18 ,-4 ,-9 ,10 ,
            19 ,35 ,28 ,33 ,45 ,27 ,25 ,15 ,
            55 ,29 ,56 ,67 ,55 ,62 ,34 ,60 ,
            35 ,29 ,33 ,4 ,37 ,33 ,56 ,50),

    'Q': (   -39 ,-30 ,-31 ,0 ,-30 ,-36 ,-34 ,-42 ,
        -36 ,-18 ,0 ,10 ,5 ,-15 ,-21 ,-38 ,
        -30 ,-6 ,-13 ,12 ,-16 ,10 ,-16 ,-27 ,
        13 ,-15 ,-2 ,-5 ,-1 ,11 ,-20 ,-22 ,
        1 ,-16 ,22 ,17 ,25 ,20 ,-13 ,-6 ,
        -2 ,43 ,32 ,50 ,50 ,63 ,43 ,2 ,
        15 ,40 ,60 ,-10 ,-20 ,-76 ,-57 ,-24 ,
        6 ,1 ,-8 ,-80 ,69 ,24 ,88 ,26),

    'K': (   17 ,30 ,7 ,-14 ,6 ,-1 ,40 ,18 ,
            -4 ,3 ,-14 ,1 ,15 ,-18 ,13 ,4 ,
            -47 ,-42 ,-43 ,10 ,40 ,-32 ,-29 ,-32 ,
            -55 ,-43 ,0 ,10000 ,10000 ,2 ,-8 ,-50 ,
            -55 ,50 ,11 ,10000 ,10000 ,13 ,0 ,-49 ,
            -62 ,12 ,-57 ,44 ,-67 ,28 ,37 ,-31 ,
            -32 ,10 ,55 ,56 ,56 ,55 ,10 ,3 ,
            4 ,54 ,47 ,-99 ,-99 ,60 ,83 ,10),
}

piecesPositionEvaluationBlack = {
    'p': (  0 ,  0 , 0 ,  0 ,  0 ,  0 , 0 , 0 ,
            78,  83,  86,  73, 102,  82,  85,  90,
             7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
            0,    0,   0,   0,   0,   0,   0,  0),
            # a   #b   #c  #d   #e   #f   #g   #h

    'n': ( -66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69),
            # a   #b   #c  #d   #e   #f   #g   #h

    'b': ( -59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10),
            # a   #b   #c  #d   #e   #f   #g   #h

    'r': (  35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
            20,   5,  16,  13,  18,  -4,  -9,  10,
            18, -35, -16, -21, -13, -29, -46,  10,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,  10,  -2, -18, -31, -32),
             # a   #b   #c  #d   #e   #f   #g   #h

    'q': (   6,   1,  -8,-80,  69,  24,  88,  26,
            15,  40,  60, -10, -20, -76, -57, -24,
            -2,  43,  32,  50,  50,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
            13, -15,  -2,  -5,  -1,  11, -20, -22,
           -30,  -6, -13,  12, -16,  10, -16, -27,
           -36, -18,   0,  10,  5, -15, -21, -38,
           -39, -30, -31,  0,  -30, -36, -34, -42),
            #a   #b   #c  #d   #e   #f   #g   #h

    'k': (   4,  54,  47, -99, -99,  60,  83, 10,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,10000,10000,  13,   0, -49,
           -55, -43,  0, 10000, 10000, 2,  -8, -50,
           -47, -42, -43,  10,  40, -32, -29, -32,
            -4,   3, -14,  1,   15, -18,  13,   4,
            17,  30,  7, -14,   6,  -1,  40,  18),
}           #a   #b   #c  #d   #e   #f   #g   #h


# w tablicy boarda a1 = 0 - oznacza to ze wysokie indeksy wskazuja na czarne, niskie na biale
#ewaluacja pozycji dla czarnych!
def evaluatePosition(board):
    scoreWhite = 0
    scoreBlack = 0
    for s in chess.SQUARES:
        if board.piece_at(s) != None and board.piece_at(s).color == chess.WHITE:
            scoreWhite += piecesPositionEvaluationWhite[board.piece_at(s).symbol()][s]
            scoreWhite += pieceScore[board.piece_at(s).symbol()]
            scoreWhite += len(board.attacks(s)) * 5                             #mobility
        if board.piece_at(s) != None and board.piece_at(s).color == chess.BLACK:
            scoreBlack += piecesPositionEvaluationBlack[board.piece_at(s).symbol()][s]
            scoreBlack += pieceScore[board.piece_at(s).symbol()]
            scoreBlack += len(board.attacks(s)) * 5
        scoreWhite += len(board.attackers(chess.WHITE, s)) * 5                  #threats
        scoreBlack += len(board.attackers(chess.BLACK, s)) * 5

    return scoreWhite - scoreBlack


    return board.king(chess.WHITE)

def alphabeta(board, depth, alpha, beta, maxPlayer):
    if depth == 0 or board.is_checkmate():
        return (evaluatePosition(board), None)
    if maxPlayer:
        score = -float("inf")
        chosenMove = None
        movesList = board.legal_moves
        for move in movesList:
            board.push(move)
            (curentScore, curentMove) = alphabeta(board, depth - 1, alpha, beta, False )
            board.pop()
            if(curentScore > score):
                score = curentScore
                chosenMove = move
            if(score > alpha):
                alpha = score
            if(beta <= alpha):
                break
        return (score, chosenMove)
    else:
        score = float("inf")
        chosenMove = None
        movesList = board.legal_moves
        for move in movesList:
            board.push(move)
            (curentScore, curentMove) = alphabeta(board, depth - 1, alpha, beta, True )
            board.pop()
            if(curentScore < score):
                score = curentScore
                chosenMove = move
            if(score < beta):
                beta = score
            if(beta <= alpha):
                break
        return (score, chosenMove)




print("\n")
board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print(board.queens)

print(board.king(chess.WHITE))
print(board.king(chess.BLACK))
print(chess.SQUARES)


#teraz biale zaczynaja - komputer jest bialymi!
while True:

    board.push(alphabeta(board, 3, -float("inf"), float("inf"), True)[1])
    print(board)
    print("\n")
    move = input()
    print(move)
    board.push(chess.Move.from_uci(move))
    print(board)
    print("\n")
