from functions import displayMetrics, inputMetrix, product


print("Input Metrix 1")
M1 = inputMetrix()
displayMetrics(M1)

print("Input Metrix 2")
M2 = inputMetrix()
displayMetrics(M2)

NR1 = len(M1)
NC1 = len(M1[0])
NR2 = len(M2)
NC2 = len(M2[0])

if NC1 != NR2:
    print("Multiplication cannot be possible")

else:
    R = product(M1, M2)
    print("Result: ")
    displayMetrics(R)