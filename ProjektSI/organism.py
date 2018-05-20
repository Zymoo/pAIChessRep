import math
import chess
import chess.variant
from random import *


class Organism:
    pieceScore = {'P': 100, 'N': 280, 'B': 320, 'R': 479, 'Q': 929, 'K': 6000, 'p': 100, 'n': 280, 'b': 320, 'r': 479,
                  'q': 929, 'k': 6000}

    piecesPositionEvaluationWhite = {
        'P': (0, 0, 0, 0, 0, 0, 0, 0,
              -31, 8, -7, -37, -36, -14, 3, -31,
              -22, 9, 5, -11, -10, -2, 3, -19,
              -26, 3, 10, 19, 20, 1, 0, -23,
              -17, 16, -2, 15, 14, 0, 15, -13,
              7, 29, 21, 44, 40, 31, 44, 7,
              78, 83, 86, 73, 102, 82, 85, 90,
              0, 0, 0, 0, 0, 0, 0, 0,),

        'N': (-74, -23, -26, -24, -19, -35, -22, -69,
              -23, -15, 2, 0, 2, 0, -23, -20,
              -18, 10, 13, 22, 18, 15, 11, -14,
              -1, 5, 31, 21, 22, 35, 2, 0,
              24, 24, 45, 37, 33, 41, 25, 17,
              10, 67, 1, 74, 73, 27, 62, -2,
              -3, -6, 100, -36, 4, 62, -4, -14,
              -66, -53, -75, -75, -10, -55, -58, -70),

        'B': (-7, 2, -15, -12, -14, -15, -10, -10,
              19, 20, 11, 6, 7, 6, 20, 16,
              14, 25, 24, 10, 8, 25, 20, 15,
              13, 10, 17, 23, 17, 16, 0, 7,
              25, 17, 20, 34, 26, 25, 15, 10,
              -9, 39, -32, 41, 52, -10, 28, -14,
              -11, 20, 35, -42, -39, 31, 2, -22,
              -59, -78, -82, -76, -23, -107, -37, -50),

        'R': (-30, -24, -18, 10, -2, -18, -31, -32,
              -53, -38, -31, -26, -29, -43, -44, -53,
              -42, -28, -42, -25, -25, -35, -26, -46,
              18, -35, -16, -21, -13, -29, -46, 10,
              20, 5, 16, 13, 18, -4, -9, 10,
              19, 35, 28, 33, 45, 27, 25, 15,
              55, 29, 56, 67, 55, 62, 34, 60,
              35, 29, 33, 4, 37, 33, 56, 50),

        'Q': (-39, -30, -31, 0, -30, -36, -34, -42,
              -36, -18, 0, 10, 5, -15, -21, -38,
              -30, -6, -13, 12, -16, 10, -16, -27,
              13, -15, -2, -5, -1, 11, -20, -22,
              1, -16, 22, 17, 25, 20, -13, -6,
              -2, 43, 32, 50, 50, 63, 43, 2,
              15, 40, 60, -10, -20, -76, -57, -24,
              6, 1, -8, -80, 69, 24, 88, 26),

        'K': (17, 30, 7, -14, 6, -1, 40, 18,
              -4, 3, -14, 1, 15, -18, 13, 4,
              -47, -42, -43, 10, 40, -32, -29, -32,
              -55, -43, 5, 0, 0, 2, -8, -50,
              -55, 50, 11, 0, 0, 13, 0, -49,
              -62, 12, -57, 44, -67, 28, 37, -31,
              -32, 10, 55, 56, 56, 55, 10, 3,
              4, 54, 47, -99, -99, 60, 83, 10),
    }

    piecesPositionEvaluationBlack = {
        'p': (0, 0, 0, 0, 0, 0, 0, 0,
              78, 83, 86, 73, 102, 82, 85, 90,
              7, 29, 21, 44, 40, 31, 44, 7,
              -17, 16, -2, 15, 14, 0, 15, -13,
              -26, 3, 10, 19, 20, 1, 0, -23,
              -22, 9, 5, -11, -10, -2, 3, -19,
              -31, 8, -7, -37, -36, -14, 3, -31,
              0, 0, 0, 0, 0, 0, 0, 0),
        # a   #b   #c  #d   #e   #f   #g   #h

        'n': (-66, -53, -75, -75, -10, -55, -58, -70,
              -3, -6, 100, -36, 4, 62, -4, -14,
              10, 67, 1, 74, 73, 27, 62, -2,
              24, 24, 45, 37, 33, 41, 25, 17,
              -1, 5, 31, 21, 22, 35, 2, 0,
              -18, 10, 13, 22, 18, 15, 11, -14,
              -23, -15, 2, 0, 2, 0, -23, -20,
              -74, -23, -26, -24, -19, -35, -22, -69),
        # a   #b   #c  #d   #e   #f   #g   #h

        'b': (-59, -78, -82, -76, -23, -107, -37, -50,
              -11, 20, 35, -42, -39, 31, 2, -22,
              -9, 39, -32, 41, 52, -10, 28, -14,
              25, 17, 20, 34, 26, 25, 15, 10,
              13, 10, 17, 23, 17, 16, 0, 7,
              14, 25, 24, 10, 8, 25, 20, 15,
              19, 20, 11, 6, 7, 6, 20, 16,
              -7, 2, -15, -12, -14, -15, -10, -10),
        # a   #b   #c  #d   #e   #f   #g   #h

        'r': (35, 29, 33, 4, 37, 33, 56, 50,
              55, 29, 56, 67, 55, 62, 34, 60,
              19, 35, 28, 33, 45, 27, 25, 15,
              20, 5, 16, 13, 18, -4, -9, 10,
              18, -35, -16, -21, -13, -29, -46, 10,
              -42, -28, -42, -25, -25, -35, -26, -46,
              -53, -38, -31, -26, -29, -43, -44, -53,
              -30, -24, -18, 10, -2, -18, -31, -32),
        # a   #b   #c  #d   #e   #f   #g   #h

        'q': (6, 1, -8, -80, 69, 24, 88, 26,
              15, 40, 60, -10, -20, -76, -57, -24,
              -2, 43, 32, 50, 50, 63, 43, 2,
              1, -16, 22, 17, 25, 20, -13, -6,
              13, -15, -2, -5, -1, 11, -20, -22,
              -30, -6, -13, 12, -16, 10, -16, -27,
              -36, -18, 0, 10, 5, -15, -21, -38,
              -39, -30, -31, 0, -30, -36, -34, -42),
        # a   #b   #c  #d   #e   #f   #g   #h

        'k': (4, 54, 47, -99, -99, 60, 83, 10,
              -32, 10, 55, 56, 56, 55, 10, 3,
              -62, 12, -57, 44, -67, 28, 37, -31,
              -55, 50, 11, 0, 0, 13, 0, -49,
              -55, -43, 5, 0, 0, 2, -8, -50,
              -47, -42, -43, 10, 40, -32, -29, -32,
              -4, 3, -14, 1, 15, -18, 13, 4,
              17, 30, 7, -14, 6, -1, 40, 18),
    }

    def __init__(self, organismParam):
        self.playerParam = organismParam
        self.fitness = 0

    def file(self, square):
        return square % 8

    def rank(self, square):
        return square / 8

    def isSuported(self, board, square, color):
        if color == chess.WHITE:
            if self.file(square) != 0:     #jesli pionek nie jest na lewym brzegu planszy
                if board.piece_at(square - 9) != None and board.piece_at(square - 9).piece_type == chess.PAWN:
                    return True

            if self.file(square) != 7:     #jesli pionek nie jest na prawym brzegu planszy
                if board.piece_at(square - 7) != None and board.piece_at(square - 7).piece_type == chess.PAWN:
                    return True
        if color == chess.BLACK:
            if self.file(square) != 7:  # jesli pionek nie jest na lewym brzegu planszy
                if board.piece_at(square + 9) != None and board.piece_at(square + 9).piece_type == chess.PAWN:
                    return True

            if self.file(square) != 0:  # jesli pionek nie jest na prawym brzegu planszy
                if board.piece_at(square + 7) != None and board.piece_at(square + 7).piece_type == chess.PAWN:
                    return True
        return False

    def isPhalanx(self, board, square):
        if self.file(square) != 0:     #jesli pionek nie jest na lewym brzegu planszy
            if board.piece_at(square - 1) != None and board.piece_at(square - 1).piece_type == chess.PAWN:
                return True

        if self.file(square) != 7:     #jesli pionek nie jest na prawym brzegu planszy
            if  board.piece_at(square + 1) != None and board.piece_at(square + 1).piece_type == chess.PAWN:
                return True

        return False

    def pawnStructure(self, board, color):
        score = 0
        for pawn in board.pieces(chess.PAWN, color):
            if (self.isPhalanx(board, pawn) or self.isSuported(board,pawn,color)):
                score = score + 1

        return score

    def evaluatePosition(self, board):
        scoreWhite = 0
        scoreBlack = 0
        whiteOccupancy = 0
        blackOccupancy = 0

        [positionPar, piecePar, mobilityPar, territoryPar, controlPar, centerControlPar, pawnStructurePar, kingSafetyPar] = self.playerParam

        if board.is_game_over():
            if (board.result() == "1-0"):
                return 10000000
            else:
                if (board.result() == "0-1"):
                    return -10000000
                else:
                    return 0


        whiteKingArea = board.attacks(board.king(chess.WHITE))
        blackKingArea = board.attacks(board.king(chess.BLACK))

        for s in chess.SQUARES:
            currentPiece = board.piece_at(s)
            if currentPiece != None:
                if currentPiece.color == chess.WHITE:
                    scoreWhite += self.piecesPositionEvaluationWhite[currentPiece.symbol()][s] / positionPar
                    scoreWhite += self.pieceScore[currentPiece.symbol()] * piecePar
                    if currentPiece.piece_type != chess.KING:
                        scoreWhite += len(board.attacks(s)) * mobilityPar                             #mobility - wszystkie pola ktore atakuje dana figura
                else:
                    scoreBlack += self.piecesPositionEvaluationBlack[currentPiece.symbol()][s] / positionPar
                    scoreBlack += self.pieceScore[currentPiece.symbol()]* piecePar
                    if currentPiece.piece_type != chess.KING:
                        scoreBlack += len(board.attacks(s)) * mobilityPar

            whiteOccupancy = len(board.attackers(chess.WHITE, s))
            blackOccupancy = len(board.attackers(chess.BLACK, s))

            if whiteOccupancy > blackOccupancy:                 #territory
                scoreWhite += territoryPar
                if s in blackKingArea:                          #kings safety
                    scoreBlack -= kingSafetyPar
            else:
                if blackOccupancy > whiteOccupancy:
                    scoreBlack += territoryPar
                    if s in whiteKingArea:                      #kings safety
                        scoreWhite -= kingSafetyPar

            if s == chess.E4 or s == chess.E5 or s == chess.D4 or s == chess.D5:
                scoreWhite += whiteOccupancy * centerControlPar              #it is extremaly important to control the central squares
                scoreBlack += blackOccupancy * centerControlPar
            scoreWhite += whiteOccupancy * controlPar                  #threats and control
            scoreBlack += blackOccupancy * controlPar


        scoreWhite += self.pawnStructure(board,chess.WHITE) * pawnStructurePar                        #bonus for good structure of pawns
        scoreBlack += self.pawnStructure(board,chess.BLACK) * pawnStructurePar

        return scoreWhite - scoreBlack

    def alphabeta(self, board, depth, alpha, beta, maxPlayer):
        if depth == 0 or board.is_game_over():
            return (self.evaluatePosition(board), None)
        if maxPlayer:
            score = -float("inf")
            chosenMove = None
            movesList = board.legal_moves
            for move in movesList:
                board.push(move)
                (curentScore, curentMove) = self.alphabeta(board, depth - 1, alpha, beta, False)
                board.pop()
                if (curentScore > score):
                    score = curentScore
                    chosenMove = move
                if (score > alpha):
                    alpha = score
                if (beta <= alpha):
                    break
            return (score, chosenMove)
        else:
            score = float("inf")
            chosenMove = None
            movesList = board.legal_moves
            for move in movesList:
                board.push(move)
                (curentScore, curentMove) = self.alphabeta(board, depth - 1, alpha, beta, True)
                board.pop()
                if (curentScore < score):
                    score = curentScore
                    chosenMove = move
                if (score < beta):
                    beta = score
                if (beta <= alpha):
                    break
            return (score, chosenMove)

    def __str__(self):
        return str("Fitness: " + str(self.fitness) +" Params: " + str(self.playerParam))
