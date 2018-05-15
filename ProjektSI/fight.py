import math
import chess
import chess.variant
import random
from organism import Organism

def match(whitePlayer, blackPlayer, searchDepth):
    #print("\n")
    board = chess.variant.KingOfTheHillBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

    while True:
        move = (whitePlayer.alphabeta(board, searchDepth, -float("inf"), float("inf"), True ))[1]
        board.push(move)
        #print(board)
        #print("\n")
        if board.is_game_over():
            if board.result() == "1-0":
                return 1
            else:
                return 0

        move = (blackPlayer.alphabeta(board, searchDepth, -float("inf"), float("inf"), False ))[1]
        board.push(move)
        #print(board)
        #print("\n")
        if board.is_game_over():
            if board.result() == "0-1":
                return -1
            else:
                return 0

def evolution(searchDepth, primaryPopulation, numberOfGenerations):

    population = initPopulation(primaryPopulation)
    generations = numberOfGenerations

    for generation in range(generations):
        print("Generation " +  str(generation) + "\n")
        (parents, population) = selection(population,searchDepth)
        children = crossover(parents)
        population.append(children[0])
        population.append(children[1])
        population = mutation(population)

    return population

def initPopulation(orgNumber):
    return [Organism([random.uniform(1,3), random.uniform(1,3), random.randint(10,30), random.randint(5,25), random.randint(10,30), random.randint(10,30), random.randint(0,10), random.randint(0,20)]) for _ in range(orgNumber)]

def selection(population, searchDepth):
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

    if(match(a,b, searchDepth) - match(b, a, searchDepth) > 0):
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

    if(match(c,d, searchDepth) - match(d,c, searchDepth) > 0):
        population.remove(d)
        secondWiner = c
    else:
        population.remove(c)
        secondWiner = d

    return((firstWiner,secondWiner), population)

def crossover(parents):
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

def mutation(population):
    for organism in population:
        for param in organism.playerParam:
             if random.random() <= 0.05:
                 param = param + random.uniform(-(1/10)*param,(1/10)*param)
    return population

finalPopulation = evolution(3, 40, 30)
for org in finalPopulation:
    print(org.playerParam)
    org.fitness = match(org,Organism([5,10,5,5,8,10]),2) - match(Organism([5,10,5,5,8,10]),org, 2)
    print(org.fitness)


#firstOrganism = Organism([5,10,5,5,8,10])
#secondOrganism = Organism([5,10,5,5,8,10])
#
#score = match(firstOrganism,secondOrganism,1)
#score -= match(secondOrganism,firstOrganism,1)
#print(score)
