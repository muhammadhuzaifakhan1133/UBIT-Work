
def inputMetrix():
    NR = int(input("Enter no of rows: "))
    NC = int(input("Enter no of columns: "))
    metrics = metrixOfZeros(NR, NC)
    for r in range(NR):
        for c in range(NC):
            metrics[r][c] = int(input(f"Enter M[{r}][{c}]: "))
    return metrics

def makeOne(M:list, pr:int, pe:int):
    NC = len(M[0])
    for c in range(NC):
        M[pr][c] = M[pr][c] / pe
    return M

def makeZero(M: list, pr, pc):
    NR = len(M)
    NC = len(M[0])
    for r in range(NR):
        if (r == pr):
            continue
        valueToBeZero = M[r][pc]
        for c in range(NC):
            M[r][c] = M[r][c] - valueToBeZero*M[pr][c]
    return M

def getReducedRowEcholonForm(M:list):
    NR = len(M)
    NC = len(M[0])
    k = 0
    for c in range(NC):
        count = 0
        for r in range(k, NR):
            if (M[r][c] != 0):
                break
            else:
                count += 1
        if (count == NR-k):
            continue  
        pe = M[r][c]
        M = makeOne(M, r, pe)
        M = makeZero(M, r, c)
        k = r+1
    return M

def displayMetrics(metrics: list):
    NR = len(metrics)
    NC = len(metrics[0])
    for row in range(NR):
        for col in range(NC):
            print(f"{metrics[row][col]}", end="\t")
        print()


def product(metrix1, metrix2):
    Result = []
    NR = len(metrix1)
    NC = len(metrix2[0])

    for r in range(NR):
        row = []
        for c in range(NC):
            ans = 0
            for i in range(len(metrix1[0])):
                ans += metrix1[r][i]*metrix2[i][c]
            row.append(ans)
        Result.append(row)
    return Result


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