



def determinant(M):
    NR = len(M)
    NC = len(M[0])
    if (NR == 2) and (NC == 2):
        d = (M[0][0] * M[1][1]) - (M[0][1] * M[1][0])
        return d
    d = 0
    for c in range(NC):
        subM = subMetrix(M, 0, c)
        subDeterminant = M[0][c]*determinant(subM)
        if (c % 2 != 0):
            subDeterminant *= -1
        d += subDeterminant        
    return d

def subMetrix(M, skiprow, skipcol):
    R = []
    M = M[:skiprow] + M[skiprow+1:]
    for row in M:
        row = row[:skipcol] + row[skipcol+1:]
        R.append(row)
    return R


def minor(M, row, col):
    M = subMetrix(M, row, col)
    return determinant(M)


def cofactor(M, row, col):
    MINOR = minor(M, row, col)
    cofac = pow(-1, row + col) * MINOR
    return cofac

def getCofactorMetrix(M):
    NR = len(M)
    NC = len(M[0])
    cofactorMetrix = metrixOfZeros(NR, NC)
    for r in range(NR):
        for c in range(NC):
            cofactorMetrix[r][c] = cofactor(M, r, c)
    return cofactorMetrix

def getAdjointMetrix(M):
    cofactorMetrix = getCofactorMetrix(M)
    Adjoint = transpose(cofactorMetrix)
    return Adjoint

def metrixOfZeros(no_of_rows, no_of_cols):
    M = []
    for r in range(no_of_rows):
        row = []
        for c in range(no_of_cols):
            row.append(0)
        M.append(row)
    return M

def transpose(M):
    NR = len(M)
    NC = len(M[0])
    R = metrixOfZeros(NR, NC)
    for r in range(NR):
        for c in range(NC):
            R[c][r] = M[r][c]
    return R

def inverse(M):
    d = determinant(M)
    if (d == 0):
        print("Inverse does not exist: deteminant is zero")
        return []
    adjointMetrix = getAdjointMetrix(M)
    NR = len(M)
    NC = len(M[0])
    A = metrixOfZeros(NR, NC)
    for r in range(NR):
        for c in range(NC):
            A[r][c] = adjointMetrix[r][c] * (1/d)
    return A

