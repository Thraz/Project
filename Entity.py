from __future__ import print_function
from cmath import pi
from math import cos, atan2, sin
from numpy import *
import inspect
import pylab
class Entity:
    p = [0.0,0.0,0.0,0.0,0.0]
    speed = 5.0
    visionDistance = 100.0
    FOV = pi/2
    proximity = 5.0
    captureDistance = 0.5
    location = array([0.0,0.0])
    facing = 0.0
    currentState = 0
    id = None
    lastAction = None
    
    def __init__(self, id=None):
        self.id = id
        self.action_list = self.get_actions()
        self.Nactions = len(self.action_list)
        self.p = zeros(self.Nactions)

    def get_actions(self):
        """
        Return a list of tuples of action names and methods
        Actions are returned in alphabetical order of their names and probabilities must be set in that order.
        """
        A = [m for m in inspect.getmembers(self, predicate=inspect.ismethod) if m[0].startswith('action_')]
        A = sorted(A, key=lambda a : a[0])   
        return A
        
    def defineProbabilities(self, p):
        assert len(p) == self.p.shape[0]
        self.p = asarray(p, 'f').copy()
        self.p = self.p/sum(self.p)
        
        
    def act(self, entities, polygon, printing):
        """
        Take a random action based on the current probabilities
        """
        while True:
            a = self.action_list
            i = random.choice(range(len(a)), p = self.p)-1
            if printing == True: print('About to take action', a[i][0])
            result,taken = a[i][1](entities, polygon, printing)
            self.lastAction = i
            if taken == True:
                return result
    


    def getVV(self):
        return array([self.speed*cos(self.facing),self.speed*sin(self.facing)])
    
    def move(self,polygon):
    #move the entity in direction theta (handles walls)
        intersect, reflection = self.checkWall(polygon) #check wall intersection
        if intersect == None:
            velocityVector = self.getVV()
            self.location += velocityVector
        else: 
            self.location = intersect
            self.facing = reflection
        

    def getBearingToTarget(self,targetLocation):
        vector = asarray(targetLocation) - asarray(self.location)
        targetBearing = atan2(vector[1],vector[0])
        return targetBearing
        
    def getDistanceToTarget(self,target):
        vector = asarray(self.location) - asarray(target)
        distance = sqrt(vector[0]*vector[0]+vector[1]*vector[1])
        return distance
		
    def checkVision(self,targets,polygon):
        """
        Check the vision and proximity of an entity, returning True and the index of the closest
        target if one of the targets is visible and False and 0 if none are. 
        """
        self.facing = fmod(self.facing,(2*pi))
        closestTarget = 1000000
        closestTargetI = -1
        for i, target in enumerate(targets):
            target.facing = fmod(target.facing,(2*pi))
            distance  = self.getDistanceToTarget(target.location)
            #print('Distance between', self.id, 'and', target.id, 'is', distance)
            #print('Bearing between', self.id, 'and', target.id, 'is', abs(fmod(self.getBearingToTarget(target.location) - self.facing,2*pi)), "compared to",  self.FOV/2)
            if distance < self.visionDistance:
                #print("less than vision")
                if self.checkIntersectingWall(polygon,target) == False:
                    #print ("less than proximity")
                    closestTarget = distance
                    closestTargetI = i
                elif abs(fmod(self.getBearingToTarget(target.location) - self.facing,2*pi)) < self.FOV/2 and distance < closestTarget: 
                    if self.checkIntersectingWall(polygon,target) == False:
                        #print ("less than FOV")
                        closestTarget = distance
                        closestTargetI = i
        #print(closestTarget,closestTargetI) 
        if closestTargetI >= 0:
            return True, closestTargetI
        else:
            return False, 0
            
    def checkCapture(self,targets,vV):
        """
        Checks the movement of an entity to check for capture during its movement, returning true if a
        prey has been captured and false otherwise
        """
        for i in range(len(targets)):            
            targetVector = asarray(targets[i].location) - asarray(self.location)
            time =  dot(vV,targetVector)/dot(vV,vV)
            #print(time)
            if time > 1:
                time = 1
            elif time < -1:
                time = -1
            #print(time)
            closestApproach = vV*time
            delta = targetVector - closestApproach
            closestD = linalg.norm(delta)
            #print('Current distance between', self.id, 'and', targets[i].id, 'is', self.getDistanceToTarget(targets[i].location))
            #print('Closest approach distance between', self.id, 'and', targets[i].id, 'is', closestD)
            if closestD < self.captureDistance: 
                return True
            else:
                return False
                
    def plt(self, colour, printing):
        if printing == True:
            nextLocation = self.location + self.getVV()
            pylab.plot(self.location[0],self.location[1],colour + 'o')
            pylab.plot([self.location[0],nextLocation[0]],[self.location[1],nextLocation[1]],colour)
        
    def reflectBearing(self,a,b,v):
        w = asarray(b) - asarray(a)
        wHat = w / linalg.norm(w)
        v2 = dot(v,wHat)*wHat
        v1 = v - v2
        vNew = v2-v1
        return atan2(vNew[1],vNew[0])
    
    def checkIntersectingWall(self,polygon,target):
        """
        Check for a wall between the entity and target entity, returning True if an intersection is
        present and False otherwise.
        """   
        for a in polygon:
            b = polygon[polygon.index(a)+1]
            u = self.location
            r = target.location
            v = asarray(r) - asarray(u)
            lmbda =(v[0]*a[1]-u[1]*v[0]-v[1]*a[0]+v[1]*u[0])/(a[1]*v[0]-b[1]*v[0]-a[0]*v[1]+b[0]*v[1])
            if lmbda >= 0 and lmbda <= 1:
                t = 1/v[0]*((1-lmbda)*a[0]+lmbda*b[0]-u[0])
                if t >= 0 and t <= 1:
                    return True
        return False
             
    def checkWall(self,polygon):
        """
        Check that the next move of the entity does not collide with a wall (defined by polygon)
        If an intersection will occur the entity is moved up to the edge of the wall and its 
        facing is set to a reflection from the wall.
        """
       #print('location is: ',self.location, 'heading is: ',self.facing)
        time = 100.0
        position = 0.0
        mirror = 0.0
        for a in polygon:
            #print('----- Checking intersect -----')
            b = polygon[polygon.index(a)+1]
            u = self.location
            u2 = self.location +self.getVV()
            v = self.getVV()
            lmbda =(v[0]*a[1]-u[1]*v[0]-v[1]*a[0]+v[1]*u[0])/(a[1]*v[0]-b[1]*v[0]-a[0]*v[1]+b[0]*v[1])
            if lmbda >= 0 and lmbda <= 1:
                #print('----- calculating t -----')
                t = 1/v[0]*((1-lmbda)*a[0]+lmbda*b[0]-u[0])
                if t >= 0 and t <= 1:
                    #print('----- intersection!!! -----')
                    if t < time:
                        mirror = self.reflectBearing(a,b,v)
                        position = u+(v*t)*0.9
                        return position , mirror
        return None, None
        
        
        
        
        
        
        
        
        