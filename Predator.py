from __future__ import print_function
from numpy import *
from cmath import pi
from Entity import *

class Predator(Entity):
    speed = 3.0
    colour = 'b'
    def __init__(self, id):
        Entity.__init__(self, id=id)
        
    def action_chase(self,prey,polygon,printing):
        """
        Chases the closest visible prey, takes in the list of prey and the walls of the arena.
        Plots the action.
        Returns true if the prey was captured in the action.
        """
        if printing == True: print('predator', self.id, 'chase')
        visible, closest = self.checkVision(prey,polygon)
        if visible == True:
            self.facing = self.getBearingToTarget(prey[closest].location)
            self.plt(self.colour,printing)
            VV = self.getVV()
            capture = self.checkCapture(prey,VV)
            self.move(polygon)
            if printing == True: print ('predator',self.id ,'movement', capture) 
            if capture == True:
                return capture, True
        return False, False

    def action_flank(self,prey,polygon,printing):
        if printing == True: print('predator', self.id, 'flank')
        visible, closest = self.checkVision(prey,polygon)
        if visible == True:
            sign = 1 if random.rand() > 0.5 else -1
            self.facing = self.getBearingToTarget(prey[closest].location)+(pi/4)*sign
            self.plt(self.colour,printing)
            VV = self.getVV()
            capture = self.checkCapture(prey,VV)
            self.move(polygon)
            if printing == True: print ('predator',self.id ,'movement', capture) 
            if capture == True:
                return capture, True
        return False, False
        
    def action_pause(self,prey,polygon,printing):
        if printing == True: print('predator', self.id, 'pause')
        return False, True
        
    def action_look(self,prey,polygon,printing):
        if printing == True: print('predator', self.id, 'look')
        sign = 1 if random.rand() > 0.5 else -1
        for i in range(8):
            self.facing += sign*(pi/4)
            visible, closest = self.checkVision(prey,polygon)
            if visible == True:
                self.facing = self.getBearingToTarget(prey[closest].location)
                self.plt(self.colour,printing)
                return False, True
        return False, True
        
    def action_randomMove(self,prey,polygon,printing):
        if printing == True: print('predator',self.id, 'flank')
        sign = 1 if random.rand() > 0.5 else -1
        self.facing +=  sign*random.random()*pi/4
        self.plt(self.colour,printing)
        capture = self.checkCapture(prey,self.getVV())
        self.move(polygon)
        if printing == True: print ('predator',self.id ,'movement', capture) 
        return  capture, True