from __future__ import print_function
from numpy import *
from hunt import *

import pylab
import copy

def RTCoev(popSize, maxItterations):
    itteration = 1
    #------ Initialise Populations -----
    predPop = [[0, 0, 0]]*popSize
    preyPop = [[0, 0, 0]]*popSize
    for i in range(popSize):
        preyPop[i] = [genomeCreator(), 10000, zeros(3)]
        predPop[i] = [genomeCreator(), 10000, zeros(3)]
    
    # Calculate the first of the initial 3 fitnesses
    for i in range(popSize):
        fitness = fitnessCalculator(preyPop[i][0],predPop[i][0])
        preyPop[i][2][0] = fitness
        predPop[i][2][0] = fitness
    
    # Shuffle the populations in order to pair up different solutions
    random.shuffle(predPop)
    random.shuffle(preyPop)
    
    # Calculate the second of the initial 3 fitnesses
    for i in range(popSize):
        fitness = fitnessCalculator(preyPop[i][0],predPop[i][0])
        preyPop[i][2][1] = fitness
        predPop[i][2][1] = fitness
    
    # Shuffle the populations in order to pair up different solutions
    random.shuffle(predPop)
    random.shuffle(preyPop)
    
    # Calculate the third of the initial 3 fitnesses
    for i in range(popSize):
        fitness = fitnessCalculator(preyPop[i][0],predPop[i][0])
        preyPop[i][2][2] = fitness
        predPop[i][2][2] = fitness
    
    # ----- Optimisation ----- 
    while itteration <= maxItterations:
        flag = 'pred'
        
        # Update the median of all solutions
        for i in range(popSize):
            predPop[i][1] = medianCalculator(predPop[i][2])
            preyPop[i][1] = medianCalculator(preyPop[i][2])
            
        # Sort populations
        predPop.sort(key = lambda x:x[1])
        preyPop.sort(key = lambda x:x[1], reverse = True)     
        
        # Alternate between updating predator and prey
        if itteration % 2 == 1:
            primaryPop = copy.deepcopy(preyPop)
            secondaryPop = copy.deepcopy(predPop)
            flag = 'prey'
        else:
            primaryPop = copy.deepcopy(predPop)
            secondaryPop = copy.deepcopy(preyPop)
            flag = 'pred'
            
        # Plot graph
        med = popSize/2
        quat = popSize/4
        pylab.xlabel('Itteration')
        pylab.ylabel('Median Fitness')
        
        colour = 'r'
        if flag == 'pred':
            colour = 'b'
        
        pylab.plot(itteration, primaryPop[0][1], colour + 'o')
        pylab.plot(itteration, primaryPop[med][1], colour + 'x')
        pylab.plot(itteration, primaryPop[quat][1], colour + '^')
        pylab.plot(itteration, primaryPop[19][1], colour + 'o')

        # ----- Standard GA ------
        
        # Selection
        parent1 = primaryPop[binaryTournament(popSize)][0]
        parent2 = primaryPop[binaryTournament(popSize)][0]
        
        # Prepare new genomes
        child1Genome, child2Genome = crossover(parent1, parent2, 5)
        child1Genome = normalise(mutation(child1Genome,2))
        child2Genome = normalise(mutation(child2Genome,2))
        child1 = [child1Genome, 10000, zeros(3)]
        child2 = [child2Genome, 10000, zeros(3)]
        
        # Evaluation
        if flag == 'prey':
            # Against best opponent
            fitness = fitnessCalculator(child1[0], secondaryPop[0][0])
            child1[2][0] = fitness
            secondaryPop[0][2] = append(secondaryPop[0][2],fitness)
            
            fitness = fitnessCalculator(child2[0], secondaryPop[0][0])
            child2[2][0] = fitness
            secondaryPop[0][2] = append(secondaryPop[0][2],fitness)
            
            # Against median opponent 
            index = popSize/2
            
            fitness = fitnessCalculator(child1[0], secondaryPop[index][0])
            child1[2][1] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
            
            fitness = fitnessCalculator(child2[0], secondaryPop[index][0])
            child2[2][1] = fitness
            secondaryPop[index][2] =append(secondaryPop[index][2],fitness)
            
            # Against 25th percentile opponent
            index = popSize/4
            fitness = fitnessCalculator(child1[0], secondaryPop[index][0])
            child1[2][2] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
            
            fitness = fitnessCalculator(child2[0], secondaryPop[index][0])
            child2[2][2] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
            
        else:
            # Against best opponent
            fitness = fitnessCalculator(secondaryPop[0][0], child1[0])
            child1[2][0] = fitness
            secondaryPop[0][2] = append(secondaryPop[0][2],fitness)
            
            fitness = fitnessCalculator(secondaryPop[0][0], child2[0])
            child2[2][0] = fitness
            secondaryPop[0][2] = append(secondaryPop[0][2],fitness)
            
            # Against median opponent 
            index = popSize/2
            
            fitness = fitnessCalculator(secondaryPop[index][0], child1[0])
            child1[2][1] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
            
            fitness = fitnessCalculator(secondaryPop[index][0], child2[0])
            child2[2][1] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
            
            # Against 25th percentile opponent
            index = popSize/4
            
            fitness = fitnessCalculator(secondaryPop[index][0], child1[0])
            child1[2][2] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
            
            fitness = fitnessCalculator(secondaryPop[index][0], child2[0])
            child2[2][2] = fitness
            secondaryPop[index][2] = append(secondaryPop[index][2],fitness)
        
        child1[1] = medianCalculator(child1[2])
        child2[1] = medianCalculator(child2[2])
        
        # Replacement
        if flag == 'pred':
            if child1[1] < child2[1]:
                if primaryPop[19][1] > child2[1]:
                    primaryPop[19] = child2
                if primaryPop[19][1] > child1[1]:
                    primaryPop[19] = child1
                if primaryPop[18][1] > child1[1]:
                    primaryPop[19] = child1
            else:
                if primaryPop[19][1] > child1[1]:
                    primaryPop[19] = child1
                if primaryPop[19][1] > child2[1]:
                    primaryPop[19] = child2
                if primaryPop[18][1] > child2[1]:
                    primaryPop[19] = child2    
        else:
            if child1[1] > child2[1]:
                if primaryPop[19][1] < child2[1]:
                    primaryPop[19] = child2
                if primaryPop[19][1] < child1[1]:
                    primaryPop[19] = child1
                if primaryPop[18][1] < child1[1]:
                    primaryPop[19] = child1
            else:
                if primaryPop[19][1] < child1[1]:
                    primaryPop[19] = child1
                if primaryPop[19][1] < child2[1]:
                    primaryPop[19] = child2
                if primaryPop[18][1] < child2[1]:
                    primaryPop[19] = child2    
        
        # ----- Refinement ------
        
        eliteSize  = popSize/10
        # Select a member of the elite set to refine
        index = random.randint(0,eliteSize+1)
        # Evaluate more fitnesses
        if flag == 'prey':
            # Against best
            fitness = fitnessCalculator(primaryPop[index][0], secondaryPop[0][0])
            primaryPop[index][2] = append(primaryPop[index][2], fitness)
            secondaryPop[0][2] = append(secondaryPop[0][2], fitness)
            
            # Against median
            temp = popSize/2
            
            fitness = fitnessCalculator(primaryPop[0][0], secondaryPop[temp][0])
            primaryPop[index][2] = append(primaryPop[index][2], fitness)
            secondaryPop[temp][2] = append(secondaryPop[temp][2], fitness)
            
        else:
            # Against best
            fitness = fitnessCalculator(secondaryPop[0][0], primaryPop[index][0])
            primaryPop[index][2] = append(primaryPop[index][2], fitness)
            secondaryPop[0][2] = append(secondaryPop[0][2], fitness)
            
            # Against median
            temp = popSize/2
            
            fitness = fitnessCalculator(secondaryPop[temp][0], primaryPop[0][0])
            primaryPop[index][2] = append(primaryPop[index][2], fitness)
            secondaryPop[temp][2] = append(secondaryPop[temp][2], fitness)
        
        
        # Compiling the new populations
        if flag == 'pred':
            predPop = primaryPop
            preyPop = secondaryPop
        else:
            preyPop = primaryPop
            predPop = secondaryPop
        
        
        itteration += 1
        
        
    # Update the median of all solutions
    for i in range(popSize):
        predPop[i][1] = medianCalculator(predPop[i][2])
        preyPop[i][1] = medianCalculator(preyPop[i][2])
        
    # Sort populations
    predPop.sort(key = lambda x:x[1])
    preyPop.sort(key = lambda x:x[1], reverse = True)  

    # Plot final populations
    pylab.plot(itteration, predPop[0][1], 'bo')
    pylab.plot(itteration, predPop[med][1], 'bx')
    pylab.plot(itteration, predPop[quat][1], 'b^')
    pylab.plot(itteration, predPop[19][1], 'bo')
    
    pylab.plot(itteration, preyPop[0][1], 'bo')
    pylab.plot(itteration, preyPop[med][1], 'bx')
    pylab.plot(itteration, preyPop[quat][1], 'b^')
    pylab.plot(itteration, preyPop[19][1], 'bo')
    
    print('The best predator solution had a median fitness of', predPop[0][1])
    print('Its Genome was:')
    print(predPop[0][0])
    print('')
    print('The best prey solution had a median fitness of', preyPop[0][1])
    print('Its Genome was:')
    print(preyPop[0][0])
    pylab.show(block=True)
    
        
        
        
        
        
        
        
        
        
        

def genomeCreator():
    genome = []
    for i in range(20):
        genome.append(random.random())
    genome = normalise(genome)
    #print(genome)
    return genome
    
def normalise(genome):
    genome[0:5] = genome[0:5]/sum(genome[0:5])           
    genome[5:10] = genome[5:10]/sum(genome[5:10])  
    genome[10:15] = genome[10:15]/sum(genome[10:15])  
    genome[15:20] = genome[15:20]/sum(genome[15:20])  
    genome = round_(genome,7)
    return genome    
    
def fitnessCalculator(preyGenome, predGenome):
    fitness = hunt(predGenome, preyGenome, 10000, False)            
    return fitness
    
def medianCalculator(fitnesses):
    X = median(fitnesses)
    return X
   
def binaryTournament(popSize):
    index1 = random.randint(0,popSize-1)
    index2 = random.randint(0,popSize-1)
    if index1 > index2:
        return index1
    else:
        return index2

def crossover(parent1, parent2, swaps):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)
    for i in range(swaps):
        r = random.randint(0,20)
        child1[r] = parent2[r]
        child2[r] = parent1[r]    
    return child1, child2
    
def mutation(child,mutations):
    for i in range(mutations):
        r = random.randint(0,20)
        child[r] = round(random.random(),7)
    return child

   
    
    
    
    
RTCoev(25, 1000)