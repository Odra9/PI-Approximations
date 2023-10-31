from ApproxFormatLib import *
from random import randint

R = int(500)        #the upper limit of the range in between which to generate a random integer
totalCouples = getN(R/10)

coprimeCouples = 0
for i in range(totalCouples):
    a = randint(0, R)
    b = randint(0, R)
    if (np.gcd(a, b)==1):   #if GCD(a,b)=1 then a and b are coprime
        coprimeCouples+=1
        

piApprox = np.sqrt((6*totalCouples)/coprimeCouples)     #see README.md

displayApprox(piApprox)