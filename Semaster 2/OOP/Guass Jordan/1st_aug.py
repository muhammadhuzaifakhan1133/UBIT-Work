from display_metrics import displayMetrics

M = [[1, 1, 2, 9],
     [2, 4, -3, 1], 
     [3, 6, -5, 0]]
NR = len(M)
NC = len(M[0])
displayMetrics(M)
pr = int(input("Enter pivot row :"))
pc = int(input("Enter pivot column :"))
while (pr >= 0 and pc >= 0):
    pr -= 1
    pc -= 1
    pe = M[pr][pc]
    if (pe == 0): continue
    for col in range(NC):
        M[pr][col] = M[pr][col] / pe

    for r in range(NR):
        if (r == pr): continue
        makeZero = M[r][pc]
        for c in range(NC):
            M[r][c] = M[r][c] - makeZero*M[pr][c]

    displayMetrics(M)
    pr = int(input("Enter pivot row :"))
    pc = int(input("Enter pivot column :"))