from __future__ import print_function
from Entity import *
from numpy import *
class Prey(Entity):
    speed = 5
    colour = 'r'
    def __init__(self, id):
        print('a prey was initialised')
        Entity.__init__(self, id=id)
        
        
      
    def action_randomMovement(self,predators,polygon):
        """
        The prey moves in a random direction, taking in the list of predators and and the
        walls of the arena. 
        Plots the action.
        Returns true if the prey was captured in the action.
        """
        print('prey', self.id, 'randomMovement')
        sign = 1 if random.rand() > 0.5 else -1
        self.facing +=  sign*random.random()*pi/4
        self.plt(self.colour)
        VV = self.getVV()
        capture = self.checkCapture(predators,VV)
        self.move(polygon)
        print( 'prey movement', capture)
        return  capture

    def action_flee(self,predators,polygon):
        print('prey', self.id, 'flee')
        return False
        
    def action_circle(self,predators,polygon):
        print('prey', self.id, 'flee')
        return False
    
    def action_pause(self,predators,polygon):
        print('prey', self.id, 'pause')
        return False
        
    def action_look(self,predators,polygon):
        print('prey', self.id, 'look')
        return False