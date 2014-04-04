from __future__ import print_function
from Environment import Environment
import sys, time
import pylab
    
def hunt(predatorGenome, preyGenome, turnlimit, printing):
    env = Environment(predatorGenome, preyGenome, printing)
    capture = False
    turnCount = 0
    while capture != True:
        if turnCount == turnlimit:
            break
        capture = env.turn()
        turnCount += 1
        #time.sleep(3)
        
    pylab.show(block=True)
    return turnCount
    
a = hunt([0.68566336,0.7014364,0.30479355,0.15918317,0.46731013],[0.0,0.0,0.0,0.0,1.0], 1000, True)
print(a)