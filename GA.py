from __future__ import print_function
from numpy import *
from scipy import stats
from hunt import *
import pylab
import copy




def GA(popSize, maxEvaluations):
    evaluations = 0
    games = 5
    
    #----- Initialise the population ------
    population = [[0,0]]*popSize
    for i in range(len(population)):
        population[i] = [zeros(5),5000]
        for j in range(len(population[i])):
            population[i][0][j] = random.random()
        population[i][0] = asarray(population[i][0])/sum(population[i][0])
        population[i][1] = fitnessCalculator(population[i][0],games)
        evaluations += 1
        
    #----- Perform optimisation -----
    while evaluations < maxEvaluations:
        fitnesses = fitnessExtractor(population)
        print(fitnesses)
        pylab.ion()
        print(evaluations, 'evaluations so far and the best fitness is', min(fitnesses))
        #pylab.plot( evaluations, median(fitnesses), 'bo') #median
        #pylab.plot( evaluations, min(fitnesses), 'go') #minimum
        #pylab.plot( evaluations, stats.scoreatpercentile(fitnesses, 10), 'yx') #10th percentile
        #pylab.plot( evaluations, stats.scoreatpercentile(fitnesses, 90), 'rx') #90th percentile
        #pylab.show(block=False)

        # selection
        parentOne = binaryTournament(population)
        parentTwo = binaryTournament(population)
        # crossover
        childOne, childTwo = crossover(parentOne, parentTwo, 2)
        # mutation
        childOne = mutation(childOne,1)
        childTwo = mutation(childTwo,1)
        # evaluate children
        childOne[0] = asarray(childOne[0])/sum(childOne[0])
        childOne[1] = fitnessCalculator(childOne[0],games)
        evaluations += 1
        childTwo[0] = asarray(childTwo[0])/sum(childTwo[0])
        childTwo[1] = fitnessCalculator(childTwo[0],games)
        evaluations += 1
        
        #replace the worst in the population
        currentWorstI = worstFinder(population)
        if childOne[1] < population[currentWorstI][1]:
            print(population[currentWorstI][1], 'replaced with c1', childOne[1])
            population[currentWorstI] = childOne
        currentWorstI = worstFinder(population)
        if childTwo[1] < population[currentWorstI][1]:
            print(population[currentWorstI][1], 'replaced with c2', childTwo[1])
            population[currentWorstI] = childTwo
            
    pylab.show(block=True)
    bestI = bestFinder(population)
    print('the best genome was', population[bestI][0])
    print('this had a fitness of', population[bestI][1])
    return population[bestI]

def crossover(parentOne, parentTwo, swaps):
    childOne = copy.deepcopy(parentOne)
    childTwo = copy.deepcopy(parentTwo)
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
    
def fitnessExtractor(population):
    fitnesses = []
    for individual in population:
        fitnesses.append(individual[1])
    return fitnesses

def fitnessCalculator(genome,games):
    totalTurns = 0
    for i in range(games):
        totalTurns += hunt(genome, [0.0,0.0,0.0,0.0,1.0], 5000, False)
    return totalTurns/games
    
a = GA(5,50)
print(a)