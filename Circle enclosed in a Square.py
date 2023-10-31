from ApproxFormatLib import *
from random import uniform

R = 50
inside = 0

N = getN(1e3)

for i in range(N):
    x = uniform(-R, R)
    y = uniform(-R, R)
    if (x*x + y*y < R*R) :
        #dentro cerchio
        inside+=1


piApprox = 4*inside/N          #approx finale

displayApprox(piApprox)