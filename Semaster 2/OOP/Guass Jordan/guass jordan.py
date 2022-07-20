def displayMetrics(metrics):
    print("==============================")
    for row in metrics:
        for element in row:
            print(f"{element:.2f}", end=" ")
        print("")
    print("==============================")

def enterPivotRowColumn():
    global pr, pc
    pr = int(input("Enter pivot row :"))
    pc = int(input("Enter pivot column :"))
    pr -= 1
    pc -= 1

M = [[1, 1, 2, 9],[2, 4, -3, 1], [3, 6, -5, 0]]
NumberOfRows = 3
NumberOfColumns = 4
displayMetrics(M)


enterPivotRowColumn()

while((pr >= 0) or (pc >= 0)):
    
    pe = M[pr][pc]
    if (pe == 0):
        print("Zero cannot be pivot element")
        enterPivotRowColumn()
        continue

    # Make One
    for c in range(NumberOfColumns):
        M[pr][c] = M[pr][c] / pe


    # Make Zero
    for r in range(NumberOfRows):
        if (r == pr):
            continue
        makeZero = M[r][pc]
        for c in range(NumberOfColumns):
            M[r][c] = M[r][c] - M[pr][c] * makeZero

    displayMetrics(M)

    enterPivotRowColumn()