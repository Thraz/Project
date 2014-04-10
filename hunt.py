from __future__ import print_function
from Environment import Environment
import sys, time
import pylab
    
def hunt(predatorGenome, preyGenome, turnlimit, printing):
    env = Environment(predatorGenome, preyGenome, printing)
    capture = False
    turnCount = 0
    while capture != True:
        if turnCount == turnlimit:
            break
        capture = env.turn()
        turnCount += 1
        #time.sleep(3)
        
    if printing == True: pylab.show(block=True)
    return turnCount
    
    #env [0,0],[100,0],[130,120],[0,100],[50,30],[0,0]
    #----- Initialise prey position -----
    #    self.prey[0].location = [90.0,95.0]
    #    #----- Initialise predator positions -----
    #    self.predators[0].location = [20.0,5.0]    
    #    #self.predators[1].location = [100.0,100.0]
    #    #self.predators[2].location = [10.0,95.0]
    #    #----- Initialise prey facing -----
    #    self.prey[0].facing = pi*1/2
    #    #----- Initialise predator facings -----
    #    self.predators[0].facing = pi*3/4
    #    #self.predators[1].facing = pi+pi*1/4
    #    #self.predators[2].facing = pi+pi*3/4
a = hunt([0.01104371,0.98895629,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0], 1000, True)
print(a)


#b = hunt([0.89685834,0.63050405,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0], 1000, True)
#print(b)