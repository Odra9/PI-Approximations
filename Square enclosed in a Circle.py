from ApproxFormatLib import *
from random import uniform

R = 50
A = R/np.sqrt(2)        #"apotema"

insideCircle = 0
insideSquare = 0

N = getN(1e3)

for i in range(N):
    x = uniform(-R, R)
    y = uniform(-R, R)
    if (x*x + y*y < R*R) :
        #dentro cerchio
        insideCircle+=1
        if (-A <= x <= A and -A <= y <= A):
            insideSquare+=1


piApprox = 2*insideCircle/insideSquare          #approx finale

displayApprox(piApprox)