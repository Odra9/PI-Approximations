from ApproxFormatLib import *
from random import randint

R = int(1e5)
N = getN(R/10)

count = 0
for i in range(N): 
    a = randint(0, R)
    b = randint(0, R)
    if (np.gcd(a, b)==1):   #verifica siano coprimi
        count+=1
        
ratio = count/R
piApprox = np.sqrt(6/ratio)

displayApprox(piApprox)