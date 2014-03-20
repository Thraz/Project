from __future__ import print_function
from Entity import *
from numpy import *
class Prey(Entity):
    speed = 3.0
    def __init__(self, id):
        print('a prey was initialised')
        Entity.__init__(self, id=id)
        
    #def checkVision(predators):
    #   for entity in predator:
    #        if getDistanceToTarget(entity.getLocation()) < visionDistance:
    #            if getBearingToTarget(entity.getBearing()) - facing < FOV:
    #                self.preyVisible = True
    #        else:
    #            self.preyVisible = False
                
    #def checkCaptured(self,predators,vV):
    #    for i in range(predators.size):            
    #        predatorLocation = predators[i].location - self.location
    #        timeOfClosestApproach =  dot(vV.T,self.location)/dot(vV.T,vV)
    #        closestApproach = predators[i].location - dot(vV,timeOfClosestApproach)
    #        closestApproachDistance = sqrt(closestApproach[0]**2+closestApproach[1]**2)
    #        if closestApproachDistance < self.captureDistance:
    #            captured = True
    #        else:
    #            captured = False
                
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
