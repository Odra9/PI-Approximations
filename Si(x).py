from ApproxFormatLib import *

#define Si(x) = sinx/x for every x != 0 and Si(0)=1 
def Si(x):
    if (x==0):
        return 1
    else:
        return np.sin(x)/x

WIDTH = getN(1e5)
DELTAX = 0.001
Area = 0
for i in range(WIDTH+1):
    Area += (Si(i*DELTAX)+Si((i+1)*DELTAX))*DELTAX    #see README.md

displayApprox(Area)