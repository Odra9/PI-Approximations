from ApproxFormatLib import *
from random import uniform

N = getN(1e3)

R = 50      #radius of the circle

pointsInCircle=0
for i in range(N):
    x = uniform(-R, R)          #creates a random point (coordinates x, y)
    y = uniform(-R, R)          #inside of the square
    if (x*x + y*y < R*R) :
        #if the check is passed, the point is also inside of the circle
        pointsInCircle+=1


piApprox = 4*pointsInCircle/N          

displayApprox(piApprox)