from ApproxFormatLib import *

N = getN(1e3)

piApprox = 0
for i in range(N+1):
    piApprox += np.power(-1,i)/(2*i+1)  #see README.md

piApprox*=4 

displayApprox(piApprox)