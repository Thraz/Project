from cmath import pi
from math import cos, atan2, sin
from numpy import *
class Entity:
    speed = 5.0
    visionDistance = 40.0
    FOV = pi/4
    proximity = 10
    captureDistance = 50.0
    captured = False
    location = array([0,0])
    facing = 0.0
    currentState = 0

    def __init__(self):
        print('an entity was initialised')
        #self.action_list = self.get_actions()
        #self.Nactions = len(self.action_list)
        #self.p = np.zeros(self.Nactions)

    #def get_actions(self):
    #    """Return a list of tuples of action names and methods
    #    
    #    Actions are returned in alphabetical order of their names and probabilities must be set in that order.
    #    
    #    """
    #    A = [m for m in inspect.getmembers(self, predicate=inspect.ismethod) if m[0].startswith('action_')]
    #    A = sorted(A, key=lambda a : return a[0])    
        
    #def actions_probabilities(self, p):
    #    assert len(p) == self.p.shape[0]
    #    self.p = np.asarray(p, 'f').copy()
    #    self.p = self.p/np.sum(self.p)
        
    #def act(self):
    #    """Take a random action based on the current probabilities"""
    #    while True:
    #        a = np.random.choice(self.action_list, p=self.p)
    #        print 'About to take action', a[0]
    #        success = a[1][0]()
    #        if success:
    #            print 'Success!'
    #            return
    


    
    def move(self,theta):
    #move the entity in direction theta
        velocityVector = array([self.speed*cos(theta),self.speed*sin(theta)])
        self.location += velocityVector
        return velocityVector

    def getBearingToTarget(self,target):
        vector = self.location - target
        targetBearing = atan2(target[1],target[0])
        return targetBearing
        
    def getDistanceToTarget(self,target):
        vector = self.location - target
        distance = sqrt(vector[0]*vector[0]+vector[1]*vector[1])
        return distance
		
    def checkVision(self,targets):
    #Check the vision and proximity of an entity, returning True and the index of the closest
    #target if one of the targets is visible and False and 0 if none are. 
        closestTarget = 1000000
        closestTargetI = -1
        for i in range(targets.size):
            distance  = self.getDistanceToTarget(targets[i].location)
            if  distance < self.visionDistance and self.getBearingToTarget(targets[i].location)-self.facing < self.FOV:
                if distance < closestTarget:
                    closestTarget = distance
                    closestTargetI = i
            elif distance < self.proximity:
                if distance < closestTarget:
                    closestTarget = distance
                    closestTargetI = i
        if closestTarget == -1:
            return False, 0
        else:
            return True, closestTargetI
            
    def checkCapture(self,targets,vV):
    #Checks the movement of an entity to check for capture during its movement, returning true if a
    #prey has been captured and false otherwise
        for i in range(targets.size):            
            distance = targets[i].location - self.location
            time =  dot(vV.T,distance)/dot(vV.T,vV)
            closestApproach = distance - dot(vV,time)
            closestD = sqrt(closestApproach[0]**2 + closestApproach[1]**2)
            if closestD < self.captureDistance: 
                return True
            else:
                return False