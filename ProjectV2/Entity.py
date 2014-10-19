from cmath import pi
from math import cos, atan2, sin
from numpy import *
import inspect
import pylab

class Entity:
    p = zeros(7,6)
    speed = 5.0
    visionDistance 35.0
    FOV = pi/2
    prosimity = 5.0
    captureDistance = 0.5
    location = [0.0,0.0]
    facing = 0.0
    id = None
    type = None
    colour = None
    
    def __init__(self, id = None):
        self.id = id
        self.action_list = self.get_actions()
        self.Nactions = len(self.action_list)
        
    def get_actions(self):
        """
        Return a list of action name and method tuple pairs
        Actions are returned in alphabetical order of their names and probabilities must be set in that order.
        """
        A = [m for m in inspect.getmembers(self, predicate=inspect.ismethod) if m[0].startswith('action_')]
        A = sorted(A, key=lambda a : a[0])   
        return A
        
    def defineProbabilities(self,p):
        """
        Defines and sets the probabilities for each state and action in the probability matrix
        """
        self.p = p
        
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
            predInVision, x = self.checkVision(predators, polygon)
            preyInVision, x = self.checkVision(prey,polygon)
            predSide
            if predInVision == False and preyInVision == False:
                probabilities = self.p[1,:]
            if predInvivion == False and preyInVision == True:
                probabilities = self.p[p[2,:]
            if preyInVision == True and predInVision == True and predSide == "L":
                probabilities = self.p[p[3,:]
            if preyInVision == True and predInVision == True and predSide == "R"::
                probabilities = self.p[p[4,:]
            if preyInVision == True and predInVision == True and predSide == "B":
                probabilities = self.p[p[5,:]
            if preyInVision == True and predInVision == True and predSide == "N":
                probabilities = self.p[p[6,:]
            #choose action based on probabilities
            i = random.choice(range(len(a)), p = probabilities)-1
            if printing == True: print('About to take action', a[i][0])
            if self.type == 'prey':
                result,taken = a[i][1](predators, polygon, printing)
            elif self.type == 'predator':
                result,taken = a[i][1](prey, polygon, printing)
            if taken == True:
                return result
            
    def checkSide(self, targets, polygon):
        visible, x = self.checkVision(self, targets, polygon)
        if visible == True:
            bearing  = self.getBearingToTarget(target.location)
            if bearing < 0:
                return "L"
            if bearing > 0:
                return "R"
            
            
            
            
            
            
            
    