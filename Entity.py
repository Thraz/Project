from __future__ import print_function
from cmath import pi
from math import cos, atan2, sin
from numpy import *
import pylab
class Entity:
    speed = 5.0
    visionDistance = 50.0
    FOV = pi/2
    proximity = 10.0
    captureDistance = 1.0
    location = array([0.0,0.0])
    facing = 0.0
    currentState = 0
    id = None
    
    def __init__(self, id=None):
        self.id = id
        print('entity', self.id,  'was initialised')
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
    


    def getVV(self):
        return array([self.speed*cos(self.facing),self.speed*sin(self.facing)])
    
    def move(self):
    #move the entity in direction theta
        velocityVector = self.getVV()
        self.location += velocityVector

    def getBearingToTarget(self,targetLocation):
        vector = targetLocation - self.location
        targetBearing = atan2(vector[1],vector[0])
        return targetBearing
        
    def getDistanceToTarget(self,target):
        vector = self.location - target
        distance = sqrt(vector[0]*vector[0]+vector[1]*vector[1])
        return distance
		
    def checkVision(self,targets):
    #Check the vision and proximity of an entity, returning True and the index of the closest
    #target if one of the targets is visible and False and 0 if none are. 
        self.facing = fmod(self.facing,2*pi)
        closestTarget = 1000000
        closestTargetI = -1
        for i, target in enumerate(targets):
            target.facing = fmod(target.facing,2*pi)
            distance  = self.getDistanceToTarget(target.location)
            #print('Distance between', self.id, 'and', target.id, 'is', distance)
            #print('Bearing between', self.id, 'and', target.id, 'is', abs(self.getBearingToTarget(target.location)-self.facing), "compared to",  self.FOV/2)
            #print(self.getBearingToTarget(target.location)-self.facing)
            if distance < self.visionDistance:
                #print("less than vision")
                if distance < self.proximity: #and distance < closestTarget:
                    #print ("less than proximity")
                    closestTarget = distance
                    closestTargetI = i
                elif abs(self.getBearingToTarget(target.location)-self.facing) < self.FOV/2: #and distance < closestTarget: 
                    #print ("less than FOV")
                    closestTarget = distance
                    closestTargetI = i
        #print(closestTarget,closestTargetI) 
        if closestTargetI >= 0:
            return True, closestTargetI
        else:
            return False, 0
            
    def checkCapture(self,targets,vV):
    #Checks the movement of an entity to check for capture during its movement, returning true if a
    #prey has been captured and false otherwise
        for i in range(len(targets)):            
            targetVector = targets[i].location - self.location
            time =  dot(vV,targetVector)/dot(vV,vV)
            closestApproach = targetVector + vV*time
            closestD = sqrt(closestApproach[0]**2 + closestApproach[1]**2)
            print('Current distance between', self.id, 'and', targets[i].id, 'is', self.getDistanceToTarget(targets[i].location))
            print('Closest approach distance between', self.id, 'and', targets[i].id, 'is', closestD)
            if closestD < self.captureDistance: 
                return True
            else:
                return False
                
    def plt(self,colour):
        nextLocation = self.location + self.getVV()
        pylab.plot(self.location[0],self.location[1],colour + 'o')
        pylab.plot([self.location[0],nextLocation[0]],[self.location[1],nextLocation[1]],colour)