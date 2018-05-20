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

    def playerComputerMatch(self, computer, depth, white):
        print("\n")
        board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        if white == True:
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
        else:
            while True:
                move = computer.alphabeta(board, depth, -float("inf"), float("inf"), True)[1]
                board.push(move)
                print(board)
                print("\n")
                if board.is_game_over():
                    break
                move = input()
                print(move)
                board.push(chess.Move.from_uci(move))
                print(board)
                print("\n")
                if board.is_game_over():
                    break

firstOrganism = Organism([1.7882712821646762, 2.0117582809407675, 20, 8, 14, 12, 7, 10])    #two best finalists
secondOrganism = Organism([1.8121153745983598, 2.557559664770355, 11, 8, 16, 22, 7, 10])
sm = SimpleMatch()
score = sm.computersMatch(secondOrganism,firstOrganism, 3)
