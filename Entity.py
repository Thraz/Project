from __future__ import print_function
from cmath import pi
from math import cos, atan2, sin
from numpy import *
import inspect
import pylab

class Entity:
    # Define the probabilities for each entity state
    p1 = [0.0,0.0,0.0,0.0,0.0]
    p2 = [0.0,0.0,0.0,0.0,0.0]
    p3 = [0.0,0.0,0.0,0.0,0.0]
    p4 = [0.0,0.0,0.0,0.0,0.0]
    #set default parameters
    speed = 5.0
    visionDistance = 35.0
    FOV = pi/2
    proximity = 5.0
    captureDistance = 0.5
    location = array([0.0,0.0])
    facing = 0.0
    id = None
    type = None
    colour = None
    
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
        """
        Defines and sets the probabilities for each state
        Takes in an array (p) of 20 probabilities, 5 for each state
        """
        temp = asarray(p, 'f').copy()
        #p1 defines probabilities for no visible prey or predators
        self.p1 = temp[0:5]
        self.p1 = self.p1/sum(self.p1)
        #p2 defines probabilities for only visible predators
        self.p2 = temp[5:10]
        self.p2 = self.p2/sum(self.p2)
        #p3 defines probabilities for only visible prey
        self.p3 = temp[10:15]
        self.p3 = self.p3/sum(self.p3)
        #p4 defines probabilities for visible prey and predators
        self.p4 = temp[15:20]
        self.p4 = self.p4/sum(self.p4)

        
        
    def act(self, predators, prey, polygon, printing):
        """
        Take a random action based on the current probabilities
        predators - a list of all predators in the game
        prey - a list of all prey in the game
        polygon -  the vertexes that define the arena
        printing -  boolean defining whether printing is turned off or on
        """
        while True:
            a = self.action_list
            #select the state
            predatorsInVision, x = self.checkVision(predators,polygon)
            preyInVision, x = self.checkVision(prey,polygon)
            if predatorsInVision == False and preyInVision == False: 
                probabilities = self.p1
            if predatorsInVision == True and preyInVision == False: 
                probabilities = self.p2
            if predatorsInVision == False and preyInVision == True: 
                probabilities = self.p3
            if predatorsInVision == True and preyInVision == True: 
                probabilities = self.p4
            #choose an action based on the state probabilities            
            i = random.choice(range(len(a)), p = probabilities)-1
            #take the action
            if printing == True: print('About to take action', a[i][0])
            if self.type == 'prey':
                result,taken = a[i][1](predators, polygon, printing)
            elif self.type == 'predator':
                result,taken = a[i][1](prey, polygon, printing)
            if taken == True:
                return result
    


    def getVV(self):
        """
        Return the velocity vector calculated using the entities current parameters
        """
        return array([self.speed*cos(self.facing),self.speed*sin(self.facing)])
    
    def move(self,polygon):
        """
        Move the entity along according to their current parameters, checking for and handling 
        intersections with walls
        polygon -  the vertexes that define the arena
        """
        intersect, reflection = self.checkWall(polygon) #check wall intersection
        if intersect == None:
            velocityVector = self.getVV()
            self.location += velocityVector
        else: 
            self.location = intersect
            self.facing = reflection
        

    def getBearingToTarget(self,targetLocation):
        """
        Returns the bearing between the entity and its target
        targetLocation -  the targets current location
        """
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
            if target.id == self.id: continue
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
        """
        Plots the current location of the entity and, and its Velocity Vector (a line
        showing its next movement).
        colour - the colour which you want the line to be plotted in in the plot format
            ie green = g, blue = b
        printing -  boolean defining whether printing is turned off or on
        """
        if printing == True:
            nextLocation = self.location + self.getVV()
            pylab.plot(self.location[0],self.location[1],colour + 'o')
            pylab.plot([self.location[0],nextLocation[0]],[self.location[1],nextLocation[1]],colour)
        
    def reflectBearing(self,a,b,v):
        """
        returns the reflected vector in the wall the entity is about to cross
        """
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
