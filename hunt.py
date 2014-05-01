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
        #time.sleep(10)
        
    if printing == True: pylab.show(block=True)
    return turnCount

#print(hunt( [0.105,0.302,0.243,0.172,0.176,
#            0.425,0.251,0.154,0.126,0.044,
#            0.003,0.306,0.386,0.112,0.193,
#            0.270,0.318,0.274,0.034,0.105],
#            [0.221,0.233,0.248,0.093,0.204,
#            0.349,0.410,0.076,0.101,0.064,
#            0.024,0.341,0.202,0.142,0.291,
#            0.148,0.072,0.46,0.078,0.238],
#    1000, True))

