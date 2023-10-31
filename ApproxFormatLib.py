import sys
import numpy as np

# Returns the number of iterations. See README.md
def getN(N0 = 10):
    if (len(sys.argv) == 1):
        N = N0
    else:
        N = sys.argv[1]
      
    N = int(N)      
    print(f"N has been chosen to be: {N}\n")  
    return N

# Displays the Approximation. See README.md
def displayApprox(approx):
    DELTA = np.abs(approx-np.pi)
    
    print("Pi has been approximated to", approx)
    print("Pi is actually equal to", np.pi)
    print("Delta:", DELTA)
    print(f"err%: {np.abs(DELTA/np.pi)*100}%")