import math
import chess
import chess.variant
import random
from organism import Organism


class Selection:

    def __init__(self, startNumber, endNumber):
        self.startNumber = startNumber
        self.endNumber = endNumber
        self.population = self.initPopulation(startNumber)

    def initPopulation(self, orgNumber):
        return [Organism([random.randint(5, 30), random.randint(5, 30), random.randint(5, 30), random.randint(5, 30), random.randint(0, 10), random.randint(0, 20)]) for _ in range(orgNumber)]

    def figthWithWhiteGameMaster(self, organism, gamesRange, depth):
        score = 0
        fileBlack = open('C:/Users/Asus/PycharmProjects/AIv1/venv/Scripts/gamesBlack.txt', "r")
        lines = fileBlack.readlines()
        for _ in range(gamesRange):      #gra dwie partie czarnymi
            gameScore = 0
            line = lines[random.randint(0, 49)]
            moves = line.split(" ")
            print(moves);

            whiteMoves = moves[1::3]
            blackMoves = moves[2::3]
            board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

            for i in range(len(whiteMoves)):
                board.push_san(whiteMoves[i])
                print(whiteMoves[i])
                print(board)
                foundMove = (organism.alphabeta(board, depth, -float("inf"), float("inf"), False ))[1]
                print(foundMove)
                print(blackMoves[i])
                if board.san(foundMove) == blackMoves[i]:
                    gameScore = gameScore + 1
                board.push_san(blackMoves[i])
                print(board)
            gameScore = gameScore/len(whiteMoves)
            score += gameScore
        score = score/gamesRange
        print(score)
        return score

    def figthWhithBlackGameMaster(self, organism, gamesRange, depth):
        score = 0
        fileBlack = open('C:/Users/Asus/PycharmProjects/AIv1/venv/Scripts/gamesWhite.txt', "r")
        lines = fileBlack.readlines()
        for _ in range(gamesRange):      #gra dwie partie czarnymi
            gameScore = 0
            line = lines[random.randint(0, 49)]
            moves = line.split(" ")
            print(moves);

            whiteMoves = moves[1::3]
            blackMoves = moves[2::3]
            print(whiteMoves)
            print(blackMoves)
            board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

            for i in range(len(whiteMoves) - 1):
                foundMove = (organism.alphabeta(board, depth, -float("inf"), float("inf"), True))[1]
                print(foundMove)
                print(whiteMoves[i])
                if board.san(foundMove) == whiteMoves[i]:
                    gameScore = gameScore + 1
                board.push_san(whiteMoves[i])
                print(board)
                board.push_san(blackMoves[i])
                print(blackMoves[i])
                print(board)

            foundMove = (organism.alphabeta(board, depth, -float("inf"), float("inf"), True))[1]
            print(foundMove)
            print(whiteMoves[-1])
            if board.san(foundMove) == whiteMoves[i]:
                gameScore = gameScore + 1

            gameScore = gameScore/len(whiteMoves)
            score += gameScore
        score = score/gamesRange
        print(score)
        return score

    def select(self, numberOfGames, depth):
        for organism in self.population:
            scoreWhite = self.figthWhithBlackGameMaster(organism, numberOfGames, depth)
            scoreBlack = self.figthWithWhiteGameMaster(organism, numberOfGames, depth)
            organism.fitness = (scoreWhite + scoreBlack)/2
        return sorted(self.population,key=lambda organism: organism.fitness)


sel = Selection(4,4)
organisms = sel.select(2,1)
for organism in organisms:
    print(organism)
