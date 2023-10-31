from ApproxFormatLib import *

N = getN()
    
def reciprocalArctan(x):      #calculates the arctan(1/x) using the MacLaurin series to the Nth term
    x = 1/x
    arctan = 0
    
    for i in range(N+1):
        arctan += np.power(-1, i)*(np.power(x, 2*i + 1)/(2*i + 1))
        
    return arctan
        
piApprox = 16*reciprocalArctan(5) - 4*reciprocalArctan(239)     #pi/4 = 4atan(1/5)-atan(1/239)

displayApprox(piApprox)