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
<<<<<<< HEAD

=======
>>>>>>> 00af54529e293be5eeb2f4ffccda79603d0f6ec6
while turnCount < 500:
    env.IsOver = env.turn()
    turnCount += 1
    #print env.isOver
    if env.isOver == True:
        print 'the prey was captured'
        break