from Entity import *
from numpy import *
class Prey(Entity):
    speed = 3.0
    visiblePredators = [0,0,0]
    def __init__(self):
        print('a prey was initialised')
        visiblePredators = [False,False,False]
        Entity.__init__(self)
        
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
                
<<<<<<< HEAD
    def action_randomMovement(self,predators):
=======
    def randomMovement(self,predators):
>>>>>>> 00af54529e293be5eeb2f4ffccda79603d0f6ec6
    #The prey moves in a random direction. Predators is a list of predators
        theta = (random.random()*2*pi)
        vV = self.move(theta)
        self.facing += theta
        return self.checkCapture(predators,vV)
