from __future__ import print_function
from numpy import *
from scipy import stats
from hunt import *
import pylab
import copy

total = 0
games = 1
predGenome = [0.1,0.9,0.0,0.0,0.0,0.1,0.9,0.0,0.0,0.0,0.1,0.9,0.0,0.0,0.0,0.1,0.9,0.0,0.0,0.0]
preyGenome  = [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0]

for i in range(games):
    total += hunt(predGenome,preyGenome,10000,False)
    
print(total/games)
    