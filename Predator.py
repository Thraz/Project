from numpy import *
from cmath import pi
from Entity import *
class Predator(Entity):
    speed = 3.0
    preyVisible = False
    closest = 0
    def __init__(self):
        print('a predator was initialised')
        Entity.__init__(self)

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
            
                
<<<<<<< HEAD
                
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
                
    def action_chase(self,prey):
=======
                
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
>>>>>>> 00af54529e293be5eeb2f4ffccda79603d0f6ec6
        self.preyVisibe, self.closest = self.checkVision(prey)
        if self.preyVisible == True:
            self.facing += self.getBearingToTarget(prey[self.closest].location)
            vV = self.move(self.facing)
<<<<<<< HEAD
            return  self.checkCapture(prey,vV)
        return  False
=======
            return self.checkCapture(prey,vV)
>>>>>>> 00af54529e293be5eeb2f4ffccda79603d0f6ec6

        
    #def flank(prey):
    #self.preyVisibe, self.closest = self.checkVision(prey)
    #    if preyVisible == True:
    #        facing = getBearingToTarget(prey) + pi/4
    #        vV = move(facing)
    #        checkCapture(prey,vV)
    #        facing = getBearingToTarget(prey)        