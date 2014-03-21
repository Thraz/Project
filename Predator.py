from __future__ import print_function
from numpy import *
from cmath import pi
from Entity import *

class Predator(Entity):
    speed = 3.0
    def __init__(self, id):
        print('a predator was initialised')
        Entity.__init__(self, id=id)

        
    def action_chase(self,prey):
        # Chases the closest visible prey, takes in the list of all prey and returns True if
        # the prey was captured. Also plots the action.
        visible, closest = self.checkVision(prey)
        if visible == True:
            self.facing = self.getBearingToTarget(prey[closest].location)
            self.plt('b')
            VV = self.getVV()
            capture = self.checkCapture(prey,VV)
            self.move()
            print ('predator movement',capture) 
            if capture == True:
                return capture
        return False

    #def action_flank(self,prey):
    #    visible, closest = self.checkVision(prey)
    #    if visible == True:
    #        if 
    #        self.facing =  self.getBearingToTarget(prey[closest].location)
    #        self.plt('b')    