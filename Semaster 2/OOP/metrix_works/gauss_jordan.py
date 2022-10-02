from functions import *

M = inputMetrix()
displayMetrics(M)
M = getReducedRowEcholonForm(M)
displayMetrics(M)