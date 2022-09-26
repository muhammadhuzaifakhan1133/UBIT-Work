def inputMetrix():
    NR = int(input("Enter no of rows: "))
    NC = int(input("Enter no of columns: "))
    metrics = []
    for r in range(NR):
        row = []
        for c in range(NC):
            val = int(input(f"Enter M[{r}][{c}]: "))
            row.append(val)
        metrics.append(row)
    return metrics

def makeOne(M:list, pr:int, pe:int):
    NR = len(M)
    for c in range(NR):
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
    for i in range(NR):
        pe = M[i][i]
        M = makeOne(M, i, pe)
        M = makeZero(M, i, i)
    return M

def displayMetrics(metrics: list):
    NR = len(metrics)
    NC = len(metrics[0])
    for row in range(NR):
        for col in range(NC):
            print(f"{metrics[row][col]:5.2f}", end="\t")
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
    
