from __future__ import print_function
from numpy import *
from cmath import pi
from Entity import *
class Predator(Entity):
    speed = 3.0
    def __init__(self, id):
        print('a predator was initialised')
        Entity.__init__(self, id=id)

    #def checkVision(self,prey):
    ##check the vision and proximity of a predator
    #    for i in range(prey.size):
    #        if self.getDistanceToTarget(prey[0].location) < self.visionDistance:
    #            if self.getBearingToTarget(prey[0].location) - self.facing < self.FOV:
    #                return = True
    #            else:
    #                return = False
    #        elif self.getDistanceToTarget(prey[0].location) < self.proximity:
    #            return = True
    #        else:
    #            return = False
            
    #def checkCapture(self,prey,vV):
    #    for i in range(prey.size):            
    #        preyLocation = prey[i].location - self.location
    #        timeOfClosestApproach =  dot(vV.T,self.location)/dot(vV.T,vV)
    #        closestApproach = prey[i].location - dot(vV,timeOfClosestApproach)
    #        closestApproachDistance = sqrt(closestApproach[0]**2+closestApproach[1]**2)
    #        if closestApproachDistance < self.captureDistance:
    #            captured = True
    #        else:
    #            captured = False
    
    #def checkCapture(self,prey,vV):
    #    for i in range(prey.size):            
    #        preyLocation = prey[i].location - self.location
    #        timeOfClosestApproach =  dot(vV.T,self.location)/dot(vV.T,vV)
    #        closestApproach = prey[i].location - dot(vV,timeOfClosestApproach)
    #        closestApproachDistance = sqrt(closestApproach[0]**2+closestApproach[1]**2)
    #        if closestApproachDistance < self.captureDistance:
    #            captured = True
    #        else:
    #            captured = False
                
    def chase(self,prey):
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

        
    #def flank(prey):
    #self.preyVisibe, self.closest = self.checkVision(prey)
    #    if preyVisible == True:
    #        facing = getBearingToTarget(prey) + pi/4
    #        vV = move(facing)
    #        checkCapture(prey,vV)
    #        facing = getBearingToTarget(prey)        