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
    
#hunt([0.0133539744,0.347452920,0.00100763565,0.000771219581,0.00133539744,0.067874531,0.00129531869,0.00127263707,0.00308184369,0.489856628,0.000255049452,0.0607118620,0.000557363496,0.00127120389,0.000388407717,0.000379825482,0.00366157555,0.000664292292,0.000532966040,0.00147615212],
#    [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0], 1000, True)

#print(hunt([  0.2699263,0.442999,0.1099021,0.0943593,0.0828125,
#        0.1297317,0.0645124,0.3338118,0.3614249,0.1105182,
#        0.1422333,0.6645046,0.1054266,0.0562425,0.0315929,
#        0.3906863,0.1109692,0.1129949,0.1735148,0.2118348],
#     [  0.0,0.0,0.0,0.0,1.0,
#        0.0,0.0,0.0,0.0,1.0,
#        0.0,0.0,0.0,0.0,1.0,
#        0.0,0.0,0.0,0.0,1.0],
#    1000, True))

