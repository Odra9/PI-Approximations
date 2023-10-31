from ApproxFormatLib import *

N = getN()

piApprox = np.power(np.power(N, 0.5-N) * np.exp(N) * np.math.factorial(N-1), 2)/2 #see README.md

displayApprox(piApprox)