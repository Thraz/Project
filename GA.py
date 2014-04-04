from __future__ import print_function
from numpy import *
from hunt import *


def GA(popSize, maxEvaluations):
    evaluations = 0
    games = 5
    
    #----- Initialise the population ------
    population = [[0,0]]*popSize
    for i in range(len(population)):
        population[i] = [zeros(5),5000]
        for j in range(len(population[i])):
            population[i][0][j] = random.random()
        population[i][1] = fitnessCalculator(population[i][0],games)
        evaluations += 1
        
    #----- Perform optimisation -----
    while evaluations < maxEvaluations:
        # selection
        parentOne = binaryTournament(population)
        parentTwo = binaryTournament(population)
        # crossover
        childOne, childTwo = crossover(parentOne, parentTwo, 2)
        # mutation
        childOne = mutation(childOne,1)
        childTwo = mutation(childTwo,1)
        # evaluate children
        childOne[1] = fitnessCalculator(childOne[0],games)
        evaluations += 1
        childTwo[1] = fitnessCalculator(childTwo[0],games)
        evaluations += 1
        #replace the worst in the population
        currentWorst = worstFinder(population)
        if childOne[1] < population[currentWorst][1]:
            population[currentWorst] = childOne
        currentWorst = worstFinder(population)
        if childTwo[1] < population[currentWorst][1]:
            population[currentWorst] = childTwo
    bestI = bestFinder(population)
    print('the best genome was', population[bestI][0])
    print('this had a fitness of', population[bestI][1])
    return population[bestI]

def crossover(parentOne, parentTwo, swaps):
    childOne = parentOne
    childTwo = parentTwo
    for i in range(swaps):
        r = random.randint(0,len(parentOne[0]))
        childOne[0][r] = parentTwo[0][r]
        childTwo[0][r] = parentOne[0][r]
    return childOne, childTwo

def mutation(child,mutations):
    for i in range(mutations):
        r = random.randint(0,len(child[0]))
        child[0][r] = random.random()
    return child
      
def binaryTournament(population):
    index1 = 0
    index2 = 0
    while index1 == index2:
        index1 = random.randint(0,len(population)-1)
        index2 = random.randint(0,len(population)-1) 
    if population[index1][1] > population[index2][1]:
        return population[index2]
    else:
        return population[index1]

def worstFinder(population):
    worst = 0
    worstI = 0
    for i in range(len(population)):
        if population[i][1] > worst:
            worst = population[i][1]
            worstI = i
    return worstI
    
def bestFinder(population):
    best = 1000000
    bestI = 0
    for i in range(len(population)):
        if population[i][1] < best:
            best = population[i][1]
            bestI = i
    return bestI

def fitnessCalculator(genome,games):
    totalTurns = 0
    for i in range(games):
        totalTurns += hunt(genome, [0.0,0.0,0.0,0.0,1.0], 5000, False)
    return totalTurns/games
    
a = GA(100,5000)