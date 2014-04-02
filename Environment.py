from __future__ import print_function
from numpy import *
from random import random
from cmath import pi
from Predator import *
from Prey import *
import pylab
import time

class Environment():
    isOver = False
    vertexes = zeros((4,2))
    prey = [Prey(id='Prey')]
    predators = [Predator(id="Predator %d" % i) for i in range(1)]
    polygon = [[0,0],[100,0],[130,120],[0,100],[50,30],[0,0]]
    
    def __init__(self):
        print('initialised environment')
        self.drawArena()
        #----- Initialise prey position -----
        self.prey[0].location = [20.0,90.0]
        #----- Initialise predator positions -----
        self.predators[0].location = [20.0,5.0]    
        #self.predators[1].location = [100.0,100.0]
        #self.predators[2].location = [10.0,95.0]
        #----- Initialise prey facing -----
        self.prey[0].facing = 0.0
        #----- Initialise predator facings -----
        self.predators[0].facing = pi*1/4
        #self.predators[1].facing = pi+pi*1/4
        #self.predators[2].facing = pi+pi*3/4
        #----- Print initial positions -----
        for prey in self.prey:
            prey.plt('r')
        for predator in self.predators:
            predator.plt('b')
        
        #initialise prey probabilities
        for prey in self.prey:    
            prey.defineProbabilities([1.0])
        #initialise predator probabilities
        for predator in self.predators:
            predator.defineProbabilities([1.0,1.0,1.0,1.0,1.0])
        
            
    def turn(self):
    #Run a full turn for all predators and prey
        print('---------- New Turn ----------')
        turnCapture = False
        #----Prey movement----
        for i, prey in enumerate(self.prey):
            if turnCapture != True:
                prey.facing = fmod(prey.facing,(2*pi))
                turnCapture = prey.act(self.predators,self.polygon)
                pylab.show(block=False)
        
        #----Predator movement----
        for i, predator in enumerate(self.predators):
            if turnCapture != True:
                predator.facing = fmod(predator.facing,(2*pi))
                turnCapture = predator.act(self.prey,self.polygon)
                pylab.show(block=False)
        
        pylab.ion()
        print('Turn Result, capture =', turnCapture)
        #time.sleep(1)
        return turnCapture
        
    def drawArena(self):
        pylab.plot(*zip(*self.polygon),color='g')