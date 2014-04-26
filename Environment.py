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
    predators = [Predator(id="Predator %d" % i) for i in range(3)]
    polygon = [[20,10],[70,10],[90,50],[70,90],[20,90],[0,50],[20,10]]
    printing = False
    
    def __init__(self, predatorGenome, preyGenome, printing):
        if self.printing == True: print('initialised environment')
        self.printing = printing
        self.drawArena()
        #----- Initialise prey position -----
        self.prey[0].location = [45.0,85.0]
        #----- Initialise predator positions -----
        self.predators[0].location = [45.0,15.0]    
        #self.predators[1].location = [100.0,100.0]
        #self.predators[2].location = [10.0,95.0]
        #----- Initialise prey facing -----
        self.prey[0].facing = pi*3/2
        #----- Initialise predator facings -----
        self.predators[0].facing = pi*1/2
        #self.predators[1].facing = pi+pi*1/4
        #self.predators[2].facing = pi+pi*3/4
        #----- Print initial positions -----
        for prey in self.prey:
            prey.plt('r',self.printing)
        for predator in self.predators:
            predator.plt('b',self.printing)
        
        #initialise prey probabilities
        for prey in self.prey:    
            prey.defineProbabilities(preyGenome)
        #initialise predator probabilities
        for predator in self.predators:
            predator.defineProbabilities(predatorGenome)
            
        if self.printing == True:
            for prey in self.prey:
                print(prey.id,'initialised')
            for predator in self.predators:
                print(predator.id,'initialised')
        
            
    def turn(self):
    #Run a full turn for all predators and prey
        if self.printing == True: print('---------- New Turn ----------')
        turnCapture = False
        #----Prey movement----
        if self.printing == True: print('---------- prey ----------')
        for i, prey in enumerate(self.prey):
            if turnCapture != True:
                prey.facing = fmod(prey.facing,(2*pi))
                turnCapture = prey.act(self.predators, self.prey, self.polygon, self.printing)
                if self.printing == True: pylab.show(block=False)
        
        #----Predator movement----
        if self.printing == True: print('---------- predators ----------')
        for i, predator in enumerate(self.predators):
            if turnCapture != True:
                predator.facing = fmod(predator.facing,(2*pi))
                turnCapture = predator.act(self.predators, self.prey, self.polygon, self.printing)
                if self.printing == True: pylab.show(block=False)
        
        if self.printing == True: pylab.ion()
        if self.printing == True: print('Turn Result, capture =', turnCapture)
        #time.sleep(1)
        return turnCapture
        
    def drawArena(self):
        if self.printing == True: pylab.plot(*zip(*self.polygon),color='g')