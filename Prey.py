from __future__ import print_function
from Entity import *
from numpy import *
class Prey(Entity):
    speed = 5
    colour = 'r'
    def __init__(self, id):
        Entity.__init__(self, id=id)
        
        
      
    def action_randomMovement(self,predators,polygon,printing):
        """
        The prey moves in a random direction, taking in the list of predators and and the
        walls of the arena. 
        Plots the action.
        Returns true if the prey was captured in the action.
        """
        if printing == True: print('prey', self.id, 'randomMovement')
        sign = 1 if random.rand() > 0.5 else -1
        self.facing +=  sign*random.random()*pi/4
        self.plt(self.colour,printing)
        VV = self.getVV()
        capture = self.checkCapture(predators,VV)
        self.move(polygon)
        if printing == True: print( 'prey movement', self.id, capture)
        return  capture, True

    def action_flee(self,predators,polygon,printing):
        if printing == True: print('prey', self.id, 'flee')
        visible, closest = self.checkVision(predators,polygon)
        if visible == True:
            self.facing = self.getBearingToTarget(predators[closest].location) + pi
            self.plt(self.colour,printing)
            VV = self.getVV()
            capture = self.checkCapture(predators,VV)
            self.move(polygon)
            if printing == True: print ('prey',self.id ,'movement', capture) 
            if capture == True:
                return capture, True
        return False, False
        
    def action_split(self,predators,polygon,printing):
        if printing == True: print('prey', self.id, 'split')
        visible, closest = self.checkVision(predators,polygon)
        if visible == True:
            self.facing = self.getBearingToTarget(predators[closest].location) + pi/2
            self.plt(self.colour,printing)
            VV = self.getVV()
            capture = self.checkCapture(predators,VV)
            self.move(polygon)
            if printing == True: print ('prey',self.id ,'movement', capture) 
            if capture == True:
                return capture, True
        return False, False
    
    def action_pause(self,predators,polygon,printing):
        if printing == True: print('prey', self.id, 'pause')
        return False, True
        
    def action_look(self,predators,polygon,printing):
        if printing == True: print('prey', self.id, 'look')
        sign = 1 if random.rand() > 0.5 else -1
        for i in range(8):
            self.facing += sign*(pi/4)
            visible, closest = self.checkVision(predators,polygon)
            if visible == True:
                self.facing = self.getBearingToTarget(predators[closest].location)
                self.plt(self.colour,printing)
                return False, True
        return False, True