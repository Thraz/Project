from __future__ import print_function
from numpy import *
from scipy import stats
from hunt import *
import pylab
import copy

def coevGA(popSize,maxEvaluations):
    evaluations = 0
    games = 5
    flag = False
    genomeLength = 20
    
    #----- Initialise the populations ------
    predPop = [[0,0]]*popSize
    preyPop = [[0,0]]*popSize
    for i in range(popSize):
        preyPop[i] = [zeros(genomeLength),10000]
        predPop[i] = [zeros(genomeLength),10000]
        for j in range(genomeLength):
            predPop[i][0][j] = random.random()
            preyPop[i][0][j] = random.random()
        predPop[i][0] = normalise(predPop[i][0])
        preyPop[i][0] = normalise(preyPop[i][0])
        
    for i in range(popSize):
        predPop[i][1] = fitnessCalculator(predPop[i][0],'predator',games,popSize,preyPop,predPop)
        preyPop[i][1] = fitnessCalculator(preyPop[i][0],'prey',games,popSize,preyPop,predPop)
        evaluations += 2
    
    initalPreyPop = copy.deepcopy(preyPop)
    initalPredPop = copy.deepcopy(predPop)
     
     #----- Perform optimisation -----
    while evaluations < maxEvaluations:
        if maxEvaluations - maxEvaluations/4 <= evaluations and flag == False:
            flag = True
            games = 5
            predPop = evaluatePopulation(predPop,'predator',games,popSize,preyPop,predPop)
            preyPop = evaluatePopulation(preyPop,'prey',games,popSize,preyPop,predPop)
            print('re-evaluating population')
            
        pylab.xlabel('Fitness Evaluations')
        pylab.ylabel('Fitness')
    
    #----- Predator optimisation -----
        bestPredI = bestFinder(predPop,'predator')
        worstPredI = worstFinder(predPop,'predator')
        pylab.plot( evaluations, predPop[bestPredI][1], 'bo') #maximum
        pylab.plot( evaluations, predPop[worstPredI][1], 'bo') #minimum
        pylab.show(block=False)
        print(evaluations, 'evaluations so far')
        print('The best predator genome was solution', bestPredI, 'with a genome of', predPop[bestPredI][0])
        print('this had a fitness of', preyPop[bestPredI][1])
        
        
        # selection
        parentOne = binaryTournament(predPop)
        parentTwo = binaryTournament(predPop)
        # crossover
        childOne, childTwo = crossover(parentOne, parentTwo, 2)
        # mutation
        childOne = mutation(childOne,1)
        childTwo = mutation(childTwo,1)
        # evaluate children
        childOne[0] = normalise(childOne[0])      
        childOne[1] = fitnessCalculator(childOne[0],'predator',games,popSize,preyPop,predPop)
        evaluations += 1
        childTwo[0] = normalise(childTwo[0])
        childTwo[1] = fitnessCalculator(childTwo[0],'predator',games,popSize,preyPop,predPop)
        evaluations += 1
        # replace the worst in the population
        if childOne[1] < predPop[worstPredI][1]:
            predPop[worstPredI] = childOne
        worstPredI = worstFinder(predPop,'predator')
        if childTwo[1] < predPop[worstPredI][1]:
            predPop[worstPredI] = childTwo
    
    #----- Prey optimisation -----
        bestPreyI = bestFinder(preyPop,'prey')
        worstPreyI = worstFinder(preyPop,'prey')
        pylab.plot( evaluations, preyPop[bestPreyI][1], 'ro') #maximum
        pylab.plot( evaluations, preyPop[worstPreyI][1], 'ro') #minimum
        pylab.show(block=False)
        print(evaluations, 'evaluations so far')
        print('The best prey genome was solution', bestPreyI, 'with a genome of', preyPop[bestPreyI][0])
        print('this had a fitness of', preyPop[bestPreyI][1])
   
        # selection
        parentOne = binaryTournament(preyPop)
        parentTwo = binaryTournament(preyPop)
        # crossover
        childOne, childTwo = crossover(parentOne, parentTwo, 2)
        # mutation
        childOne = mutation(childOne,1)
        childTwo = mutation(childTwo,1)
        # evaluate children
        childOne[0] = normalise(childOne[0])      
        childOne[1] = fitnessCalculator(childOne[0],'prey',games,popSize,preyPop,predPop)
        evaluations += 1
        childTwo[0] = normalise(childTwo[0])
        childTwo[1] = fitnessCalculator(childTwo[0],'prey',games,popSize,preyPop,predPop)
        evaluations += 1
        #replace the worst in the population
        if childOne[1] > preyPop[worstPreyI][1]:
            preyPop[worstPreyI] = childOne
        worstPreyI = worstFinder(preyPop,'prey')
        if childTwo[1] > preyPop[worstPreyI][1]:
            preyPop[worstPreyI] = childTwo

     
    bestPredI = bestFinder(predPop,'predator')
    initialBestPredI = bestFinder(initalPredPop,'predator')
    print('The best predator genome was solution', bestPredI, 'with a genome of', predPop[bestPredI][0])
    print('this had a fitness of', predPop[bestPredI][1])
    print(' ')
    print('Whereas the best inital predator genome was solution', initialBestPredI, 'with a genome of', predPop[initialBestPredI][0])
    print('this had a fitness of', predPop[initialBestPredI][1])
    print(' ')
    
    bestPreyI = bestFinder(preyPop,'prey')
    initialBestPreyI = bestFinder(initalPreyPop,'prey')
    print('The best prey genome was solution', bestPreyI, 'with a genome of', preyPop[bestPreyI][0])
    print('this had a fitness of', preyPop[bestPreyI][1])
    print(' ')
    print('Whereas the best inital prey genome was solution', initialBestPreyI, 'with a genome of', predPop[initialBestPreyI][0])
    print('this had a fitness of', predPop[initialBestPreyI][1])
    print(' ')
    
    pylab.show(block=True)
    
    pylab.clf()
    
    for i in range(popSize):
        pylab.plot(0,initialPredPop[i][1])
        pylab.plot(1,predPop[i][1])
        pylab.plot(2,initialPreyPop[i][1])
        pylab.plot(3,preyPop[i][1])
    
    pylab.show(block=True)
    
    return predPop[bestPredI],preyPop[bestPreyI],preyPop,predPop,initialPreyPop,initialPredPop
    
    
    
    
    
def fitnessCalculator(genome,type,games,popSize,preyPop,predPop):
    totalTurns = 0
    print(genome)
    if type == 'predator':
        for i in range(games):
            index =  random.randint(0,popSize - 1)
            print('game', i)
            totalTurns += hunt(genome, preyPop[index][0], 10000, False)
    else:
        for i in range(games):
            index =  random.randint(0,popSize - 1)
            print('game', i)
            totalTurns += hunt(predPop[index][0], genome, 10000, False)
    return totalTurns/games

    
def evaluatePopulation(population,type,games,popSize,preyPop,predPop):
    """
    Does not count towards the evaluation count
    """
    for i in population:
        i[1] = fitnessCalculator(i[0],type,games,popSize,preyPop,predPop)
    return population
    
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
        child[0][r] = round(random.random(),7)
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

def worstFinder(population, type):
    if type == 'predator':
        worst = 0
        worstI = 0
        for i in range(len(population)):
            if population[i][1] > worst:
                worst = population[i][1]
                worstI = i
    else:
        worst = 10000
        worstI = 0
        for i in range(len(population)):
            if population[i][1] < worst:
                worst = population[i][1]
                worstI = i
    return worstI
    
def bestFinder(population, type):
    if type == 'predator':
        best = 1000000
        bestI = 0
        for i in range(len(population)):
            if population[i][1] < best:
                best = population[i][1]
                bestI = i
    else:            
        best = 0
        bestI = 0
        for i in range(len(population)):
            if population[i][1] > best:
                best = population[i][1]
                bestI = i
    return bestI
    
def fitnessExtractor(population):
    fitnesses = []
    for individual in population:
        fitnesses.append(individual[1])
    return fitnesses
    
def genomeExtractor(population):
    genomes = []
    for individual in population:
        genomes.append(individual[0])
    return genomes

def normalise(genome):
    genome[0:5] = genome[0:5]/sum(genome[0:5])           
    genome[5:10] = genome[5:10]/sum(genome[5:10])  
    genome[10:15] = genome[10:15]/sum(genome[10:15])  
    genome[15:20] = genome[15:20]/sum(genome[15:20])  
    genome = round_(genome,7)
    return genome

a,b,c,d,e,f = coevGA(5,20)
#print(a)

