from operator import eq
from display_metrics import displayMetrics

# input number of rows and columns
NR = int(input("Enter number of rows :"))
NC = int(input("Enter number of columns :"))

# initialize metrics to empyt list
M = []

# input metrics
for row in range(NR):
    equation = []
    for col in range(NC):
        equation.append(int(input(f"Enter M[{row}][{col}] element :")))
    M.append(equation)

# display metrics
displayMetrics(M)

# Repeat below stpes to the number of unknows
for _ in range(NC-1):
    # input pivot row
    pr = int(input("Enter pivot row :"))

    # input pivot column
    pc = int(input("Enter pivot column"))

    # Find pivot element
    pe = M[pr][pc]

    # Make pivot element to 1
    # for that Divide pivot row by the pivot element
    # pr is remain same column change one by one
    for c in range(NC):
        M[pr][c] = M[pr][c] / pe

    # Make elements of pivot Column to zero except pe
    # loop through all the row by variable r
    # if r == pr : continue
    # set variable makeZero to M[r][pc] because pc remain constant
    # loop throught all the column by variable c
    # update the element M[r][c] by M[r][c] - makeZero * M[pr][c]
    for r in range(NR):
        if (r == pr):
            continue
        makeZero = M[r][pc]
        for c in range(NC):
            M[r][c] = M[r][c] - makeZero * M[pr][c]

    displayMetrics(M)
