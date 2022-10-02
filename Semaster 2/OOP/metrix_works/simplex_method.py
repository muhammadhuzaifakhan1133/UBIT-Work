from functions import *

M = inputMetrix()

displayMetrics(M)

NR = len(M)
NC = len(M[0])

for c in range(NC):
    M[0][c] *= -1

minimum = min(M[0])
while (minimum < 0):
    pc = M[0].index(minimum)
    pr = 1
    smallest_ratio = M[1][-1] / M[1][pc]
    for r in range(1, NR):
        ratio = M[r][-1] / M[r][pc]
        if ratio < smallest_ratio:
            smallest_ratio = ratio
            pr = r
    pe = M[pr][pc]    
    makeOne(M, pr, pe)
    makeZero(M, pr, pc)
    minimum = min(M[0])

displayMetrics(M)