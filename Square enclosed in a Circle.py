from ApproxFormatLib import *
from random import uniform

N = getN(1e3)

R = 50              #radius of the circle
A = R/np.sqrt(2)    #A is defined as the side of the square divided by 2

pointsInCircle = 0
pointsInSquare = 0
for i in range(N):
    x = uniform(-R, R)
    y = uniform(-R, R)
    if (x*x + y*y < R*R) :
        #if the check is passed, the point is inside of the circle
        pointsInCircle+=1
        if (-A <= x <= A and -A <= y <= A):
            #if the check is also passed, the point is also inside of the square
            pointsInSquare+=1


piApprox = 2*pointsInCircle/pointsInSquare

displayApprox(piApprox)