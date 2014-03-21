from __future__ import print_function
from Entity import *
from numpy import *
class Prey(Entity):
    speed = 3.0
    def __init__(self, id):
        print('a prey was initialised')
        Entity.__init__(self, id=id)
        
      
    def randomMovement(self,predators):
    #The prey moves in a random direction. Predators is a list of predators
        sign = 1 if random.rand() > 0.5 else -1
        self.facing +=  sign*random.random()*pi/3
        self.plt('r')
        VV = self.getVV()
        capture = self.checkCapture(predators,VV)
        self.move()
        print( 'prey movement', capture)
        return  capture
