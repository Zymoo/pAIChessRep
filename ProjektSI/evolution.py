import math
import chess
import chess.variant
import random
from organism import Organism

class Evolution:
    def __init__(self, searchDepth, populationSize, numberofGenerations):
        self.searchDepth = searchDepth
        self.populationSize = populationSize
        self.numberOfGenerations = numberofGenerations

    # [mobilityPar, territoryPar, controlPar, centerControlPar, pawnStructurePar, kingSafetyPar] = [5,10,5,5,8,10]
    def initPopulation(self, orgNumber):
        return [Organism([random.uniform(1, 3), random.uniform(1, 3), random.randint(10, 30), random.randint(5, 25),
                            random.randint(10, 30), random.randint(10, 30), random.randint(0, 10),
                            random.randint(0, 20)]) for _ in range(orgNumber)]

    def match(self, whitePlayer, blackPlayer, searchDepth):
        board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

        while True:
            move = (whitePlayer.alphabeta(board, searchDepth, -float("inf"), float("inf"), True ))[1]
            board.push(move)
            if board.is_game_over():
                if board.result() == "1-0":
                    return 1
                else:
                    return 0

            move = (blackPlayer.alphabeta(board, searchDepth, -float("inf"), float("inf"), False ))[1]
            board.push(move)
            if board.is_game_over():
                if board.result() == "0-1":
                    return -1
                else:
                    return 0

    def evolution(self):

        population = self.initPopulation(self.populationSize)
        generations = self.numberOfGenerations
        searchDepth = self.searchDepth

        for generation in range(generations):
            print("Generation " +  str(generation) + "\n")
            (parents, population) = self.selection(population)
            children = self.crossover(parents)
            population.append(children[0])
            population.append(children[1])
            population = self.mutation(population)
            Organism.pickleOrganisms(population, 'generation' + str(generation)+'.pkl')

        return population

    def selection(self, population):

        searchDepth = self.searchDepth
        population = population
        populationSize = len(population) - 1

        aIndex = random.randint(0, populationSize)
        bIndex = random.randint(0, populationSize)
        while True:
            if aIndex != bIndex:
                break
            aIndex = random.randint(0, populationSize)
            bIndex = random.randint(0, populationSize)

        a = population[aIndex]
        b = population[bIndex]

        if(self.match(a,b, searchDepth) - self.match(b, a, searchDepth) > 0):
            population.remove(b)
            firstWiner = a
        else:
            population.remove(a)
            firstWiner = b

        populationSize = len(population) - 1

        cIndex = random.randint(0, populationSize)
        dIndex = random.randint(0, populationSize)
        while True:
            if cIndex != dIndex:
                break
            cIndex = random.randint(0, populationSize)
            dIndex = random.randint(0, populationSize)

        c = population[cIndex]
        d = population[dIndex]

        if(self.match(c,d, searchDepth) - self.match(d,c, searchDepth) > 0):
            population.remove(d)
            secondWiner = c
        else:
            population.remove(c)
            secondWiner = d

        return((firstWiner,secondWiner), population)

    def crossover(self, parents):
        (firstParent,secondParent) = parents
        firstChild = []
        secondChild = []
        for i in range(8):
            if random.random() > 0.5:
                firstChild.append(firstParent.playerParam[i])
            else:
                firstChild.append(secondParent.playerParam[i])
            if random.random() > 0.5:
                secondChild.append(secondParent.playerParam[i])
            else:
                secondChild.append(firstParent.playerParam[i])

        return (Organism(firstChild), Organism(secondChild))

    def mutation(self, population):
        for organism in population:
            for param in organism.playerParam:
                 if random.random() <= 0.05:
                     param = param + random.uniform(-(1/10)*param,(1/10)*param)
        return population


fight = Evolution(searchDepth=3, populationSize=40, numberofGenerations=30)
finalPopulation = fight.evolution()


