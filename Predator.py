from __future__ import print_function
from numpy import *
from cmath import pi
from Entity import *

class Predator(Entity):
    speed = 3.0
    colour = 'b'
    def __init__(self, id):
        print('a predator was initialised')
        Entity.__init__(self, id=id)
        
    def action_chase(self,prey,polygon):
        """
        Chases the closest visible prey, takes in the list of prey and the walls of the arena.
        Plots the action.
        Returns true if the prey was captured in the action.
        """
        print('predator', self.id, 'chase')
        visible, closest = self.checkVision(prey,polygon)
        if visible == True:
            self.facing = self.getBearingToTarget(prey[closest].location)
            self.plt(self.colour)
            VV = self.getVV()
            capture = self.checkCapture(prey,VV)
            self.move(polygon)
            print ('predator',self.id ,'movement', capture) 
            if capture == True:
                return capture
        return False

    def action_flank(self,prey,polygon):
        print('predator', 'flank')
        return False
        
    def action_pause(self,prey,polygon):
        print('predator', 'pause')
        return False
        
    def action_look(self,prey,polygon):
        print('predator', 'flank')
        return False
        
    def action_randomMove(self,prey,polygon):
        print('predator',self.id, 'flank')
        sign = 1 if random.rand() > 0.5 else -1
        self.facing +=  sign*random.random()*pi/4
        self.plt(self.colour)
        capture = self.checkCapture(prey,self.getVV())
        self.move(polygon)
        print ('predator',self.id ,'movement', capture) 
        return  capture