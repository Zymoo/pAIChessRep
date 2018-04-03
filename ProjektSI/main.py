import Knight
import chess
import chess.svg
from IPython.display import SVG
from random import *

def evaluatePosition(board):
    return randint(1,100)

def nextMove(board, depth):
    movesList = board.legal_moves
    bestScore = 0
    #chosenMove = movesList
    for move in movesList:
        board.push(move)
        score = minmax(0, depth, board, False)
        board.pop()
        if score > bestScore:
            bestScore = score
            chosenMove = move
    return chosenMove

def minmax(currentDepth, maxDepth, currentBoard, maxPlayer):
    if currentDepth == maxDepth:
        return (evaluatePosition(currentBoard))
    else:
        movesList = currentBoard.legal_moves
        if maxPlayer:
            bestScore = 0
            for move in movesList:
                currentBoard.push(move)
                score = minmax(currentDepth + 1, maxDepth, currentBoard, True)
                currentBoard.pop()

                if score > bestScore:
                    bestScore = score
        else:
            bestScore = 100
            for move in movesList:
                currentBoard.push(move)
                score = minmax(currentDepth + 1, maxDepth, currentBoard, False)
                currentBoard.pop()

                if score < bestScore:
                    bestScore = score

        return bestScore



print("\n")
board = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

while True:
    board.push(nextMove(board, 3))
    print(board)
    move = input()
    print(move)
    board.push(chess.Move.from_uci(move))
    print(board)
