from __future__ import print_function
from numpy import *
from random import random
from cmath import pi
from Predator import *
from Prey import *
import pylab
import time

class Environment():
    colours = ["bo","b^","bx"]
    isOver = False
    vertexes = zeros((4,2))
    prey = [Prey(id='Prey')]
    predators = [Predator(id="Predator %d" % i) for i in range(1)]    
    def __init__(self):
        print('initialised environment')
        self.prey[0].location = [50.0,50.0]
        for i in range(len(self.predators)):
            self.predators[i].location = array([25.0,25.0])
            
    def turn(self):
    #Run a full turn for all predators and prey
        print('---------- New Turn ----------')
        turnCapture = False
        #----Prey movement----
        if turnCapture != True:
            turnCapture = self.prey[0].randomMovement(self.predators)
            pylab.show(block=False)
        
        #----Predator movement----
        for i, predator in enumerate(self.predators):
            if turnCapture != True:
                turnCapture = predator.chase(self.prey)
                pylab.show(block=False)
        
        pylab.ion()
        print('Turn Result, capture =', turnCapture)
        #time.sleep(1)
        return turnCapture