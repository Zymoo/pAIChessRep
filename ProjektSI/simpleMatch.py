import math
import chess
import chess.svg
import chess.variant
from IPython.display import SVG
from random import *
from organism import Organism



class SimpleMatch:

    def computersMatch(self, whitePlayer, blackPlayer, depth):
        print("\n")
        board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

        while True:
            move = whitePlayer.alphabeta(board, depth, -float("inf"), float("inf"), True)[1]
            board.push(move)
            print(board)
            print("\n")
            if board.is_game_over():
                break

            move = blackPlayer.alphabeta(board, depth, -float("inf"), float("inf"), False)[1]
            board.push(move)
            print(board)
            print("\n")
            if board.is_game_over():
                break

    def playerComputerMatch(self, computer, depth):
        print("\n")
        board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

        while True:
            move = input()
            print(move)
            board.push(chess.Move.from_uci(move))
            print(board)
            print("\n")
            if board.is_game_over():
                break

            move = computer.alphabeta(board, depth, -float("inf"), float("inf"), False)[1]
            board.push(move)
            print(board)
            print("\n")
            if board.is_game_over():
                break

firstOrganism = Organism([3,2,5,10,5,5,8,10])
secondOrganism = Organism([3,2,5,10,5,5,8,10])
sm = SimpleMatch()
score = sm.computersMatch(firstOrganism,secondOrganism, 3)