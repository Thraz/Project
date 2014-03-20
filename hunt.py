from __future__ import print_function
from Environment import Environment
import sys, time

import pylab

#pylab.plot(pylab.rand(20))
#pylab.show(block=False)

#time.sleep(3)
#print("Second plot")
#sys.stdout.flush()

#pylab.hold(True)
#pylab.plot(pylab.rand(30), 'r')
#pylab.show(block=True)

#sys.exit()
env = Environment()
turnCount = 0
capture = False

while capture != True:
    if turnCount > 500:
        break
    capture = env.turn()
    turnCount += 1

if capture == True:
    print ('the prey was captured')
else:
    print ('the prey escaped')