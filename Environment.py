from numpy import *
from random import random
from cmath import pi
from Predator import *
from Prey import *
import pylab
class Environment():
    colours = ["bo","b^","bx"]
    isOver = False
    vertexes = zeros((4,2))
    prey = array([Prey()])
    predators = array([Predator()]*3)
    
    def __init__(self):
        print('initialised environment')
        self.prey[0].location = [50,50]
        for i in range(len(self.predators)):
            self.predators[i].location = array([45+i,45+i])
            
    def turn(self):
    #Run a full turn for all predators and prey
        capture = False
        #Prey movement
<<<<<<< HEAD
        capture = self.prey[0].action_randomMovement(self.predators)#[1]
=======
        capture = self.prey[0].randomMovement(self.predators)
>>>>>>> 00af54529e293be5eeb2f4ffccda79603d0f6ec6
        pylab.plot(self.prey[0].location[0],self.prey[0].location[1],"ro")
        if capture == True:
            return capture
        
        #predator movement
        for i in range(self.predators.size):
            # print 'predator start at ',self.predators[i].location
<<<<<<< HEAD
            capture = self.predators[i].action_chase(self.prey)#[1]
=======
            capture = self.predators[i].chase(self.prey)
>>>>>>> 00af54529e293be5eeb2f4ffccda79603d0f6ec6
            pylab.plot(self.predators[i].location[0], self.predators[i].location[1],self.colours[i])
            pylab.show(block=False)
            if capture == True:
                return capture
        return capture