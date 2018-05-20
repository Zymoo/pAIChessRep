import math
import chess
import chess.variant
import random
from organism import Organism


class PrimaryFitnessEvaluation:

    def __init__(self, startNumber):
        self.startNumber = startNumber
        self.population = self.initPopulation(startNumber)

    def initPopulation(self, orgNumber):
        return [Organism([random.uniform(1, 3), random.uniform(1, 3), random.randint(10, 30), random.randint(5, 25),
                          random.randint(10, 30), random.randint(10, 30), random.randint(0, 10), random.randint(0, 20)])
                for _ in range(orgNumber)]

    def figthWithWhiteGameMaster(self, organism, gamesRange, depth):
        score = 0
        fileBlack = open('gamesBlack.txt', "r")
        lines = fileBlack.readlines()
        for _ in range(gamesRange):  
            gameScore = 0
            line = lines[random.randint(0, 49)]
            moves = line.split(" ")
            whiteMoves = moves[1::3]
            blackMoves = moves[2::3]
            board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

            for i in range(len(whiteMoves)):
                board.push_san(whiteMoves[i])
                foundMove = (organism.alphabeta(board, depth, -float("inf"), float("inf"), False ))[1]
                if board.san(foundMove) == blackMoves[i]:
                    gameScore = gameScore + 1
                board.push_san(blackMoves[i])
            gameScore = gameScore/len(whiteMoves)
            score += gameScore
        score = score/gamesRange
        return score

    def figthWhithBlackGameMaster(self, organism, gamesRange, depth):
        score = 0
        fileBlack = open('gamesWhite.txt', "r")
        lines = fileBlack.readlines()
        for _ in range(gamesRange):
            gameScore = 0
            line = lines[random.randint(0, 49)]
            moves = line.split(" ")

            whiteMoves = moves[1::3]
            blackMoves = moves[2::3]
            board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

            for i in range(len(whiteMoves) - 1):
                foundMove = (organism.alphabeta(board, depth, -float("inf"), float("inf"), True))[1]
                if board.san(foundMove) == whiteMoves[i]:
                    gameScore = gameScore + 1
                board.push_san(whiteMoves[i])
                board.push_san(blackMoves[i])

            foundMove = (organism.alphabeta(board, depth, -float("inf"), float("inf"), True))[1]
            if board.san(foundMove) == whiteMoves[i]:
                gameScore = gameScore + 1

            gameScore = gameScore/len(whiteMoves)
            score += gameScore
        score = score/gamesRange
        return score

    def select(self, numberOfGames, depth):
        for organism in self.population:
            scoreWhite = self.figthWhithBlackGameMaster(organism, numberOfGames, depth)
            scoreBlack = self.figthWithWhiteGameMaster(organism, numberOfGames, depth)
            organism.fitness = (scoreWhite + scoreBlack)/2
        return sorted(self.population,key=lambda organism: organism.fitness)


selec = PrimaryFitnessEvaluation(startNumber=60)
organisms = selec.select(numberOfGames=2, depth=3)
