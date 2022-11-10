class cMetrics(list):

    def __init__(self, M:list=[]):
        super().__init__(M) # call list constructor
        self.__updateNoOfRowAndCol() # update NR (no of rows) and NC (no of cols)
        
        
    def __str__(self):
        """
        print list of list in Metrix Form
        """
        NR = self.NR
        NC = self.NC
        string = "[" # outer open bracket
        for row in range(NR):
            string += "[" #  inner open bracket
            for col in range(NC):
                string += "%5.2f" % (self[row][col])
                if (col != NC-1): # if entry is not at last of row
                    string += "\t"
            string += "]" # inner closing bracket
            if (row != NR-1): # if row is not the last row of metrics
                string += "\n "
        string += "]" # outer closing brakcet
        return string

    def __eq__(self, M2):
        if (self.NR != M2.NR) or (self.NC != M2.NC): 
            return False
        for r in range(self.NR):
            for c in range(self.NC):
                if (self[r][c] != M2[r][c]):
                    return False
        return True
    
    def __add__(self, M2):
        if (self.NR != M2.NR) or (self.NC != M2.NC):
            raise ValueError("for addition both metrics must be of same size")
        Result = cMetrics() # Empty Metrics
        for r in range(self.NR):
            row = [] # empty row
            for c in range(self.NC):
                row.append(self[r][c] + M2[r][c])
            Result.append(row) # append row to metrics
        return Result

    def __sub__(self, M2):
        R = M2 * -1 # changing sign of second metrics and apply addition process is same as subtraction
        return self + R

    def __getSpecifcEntriesofProduct(self, M2, i, j):
        """
        get specific entry of product Metrics (M1*M2) at row i col j
        """
        if (self.NC != M2.NR): # if matrix product rule does not satisfy
            raise ValueError("column of metrics 1 must be equal to row of metrics 2")
        answer = 0 # entry at row i and col j in product Metrics
        # Multiply corresponding element of row i of M1 and col j of M2 and add up all results
        for k in range(self.NC):
            answer += self[i][k] * M2[k][j]
        return answer

    def __getProductMetrics(self, M2, NR, NC, row=None, col=None):
        """
        get product Metrics (self * M2)\n
        here:\n
        NR is number of rows of product Metrics\n
        NC is number of columns of product Metrics\n
        row must be given when you want to get specific row of product Metrics\n
        col must be given when you want to get specific column of product Metrics\n
        """
        R = cMetrics()
        for r in range(NR):
            temp = []
            for c in range(NC):
                if (row == None) and (col == None): # if row and column is None get entries of all location
                    answer = self.__getSpecifcEntriesofProduct(M2, r, c)
                elif (row != None) and (col == None): # if row is given, get entries of that row for all columns c
                    answer = self.__getSpecifcEntriesofProduct(M2, row, c)
                elif (row == None) and (col != None): # if column is given, get entries of that col for all row r
                    answer = self.__getSpecifcEntriesofProduct(M2, r, col)
                temp.append(answer)
            R.append(temp)
        return R
    
    def product(self, M2, i=None, j=None, row = None, col = None):
        """
        find product of self and M2\n
        here:\n
        'r' and 'c' is given if you want to get specific entry of product metrics at row r and column c\n
        'row' is given if you want to get specific row of product metrics\n
        'col' is given if you want to get specific column of product metrics\n
        """
        if self.NC != M2.NR: # check for metrix product rule
            raise ValueError("column of metrics 1 must be equal to row of metrics 2")
        
        # handle arguments
        if (i != None) and (j == None): # if r is given for specific entry but c is not given
            raise ValueError("provide column number too for specific entry")
        if (i == None) and (j != None): # if c is given for specific entry but r is not given
            raise ValueError("provide row number too for specific entry")
        if ((row != None) and (col != None)): # if row and col both given at same time
            raise ValueError("You dont get specific row and specifc column at a time")
        if ((i != None)or(j!=None)) and ((row != None)or(col!=None)): # if r or c is given and row or col is given
            raise ValueError("You dont get specific entry and specific row or column at same time")

        if (i == None) and (j == None) and (row == None) and (col == None):
            # if you want to get all entries of product Metrics
            return self.__getProductMetrics(M2, NR=self.NR, NC=M2.NC)
        if (i != None) and (j != None):
            # if you want to get specific entry of product metrics and 'r' and 'c' is given
            return self.__getSpecifcEntriesofProduct(M2, i, j)
        if (row != None):
            # if you want to get specific 'row' of product metrics. 
            # Here output is a row vector, so NR (number of rows of product metrics) is 1
            return self.__getProductMetrics(M2, NR=1, NC=M2.NC, row=row)
        if (col != None):
            # if you want to get specific 'col' of product metrics. 
            # Here output is a col vector, so NC (number of column of product metrics) is 1
            return self.__getProductMetrics(M2, NR=self.NR, NC=1, col=col)



    def __updateNoOfRowAndCol(self):
        """
        update NR and NC attribute of Metrix
        """
        self.NR = len(self) # Number of rows
        if self.NR != 0 and isinstance(self[0], list): # if (list is not empty) and (list contain list)
            self.NC = len(self[0]) # length of inner list
        else:
            self.NC = 0 # otherwise list a row vector

    def append(self, __object) -> None:
        super().append(__object)
        self.__updateNoOfRowAndCol()

    def insert(self, __index, __object) -> None:
        super().insert(__index, __object)
        self.__updateNoOfRowAndCol()

    def copy(self):
        """
        make copy of metrix
        """
        R = cMetrics()
        for r in range(self.NR):
            row = []
            for c in range(self.NC):
                row.append(self[r][c])
            R.append(row)
        return R


    def __mul__(self, k):
        """
        multipy metrix by scalar 'k'
        """
        R = cMetrics()
        for r in range(self.NR):
            row = []
            for c in range(self.NC):
                row.append(self[r][c] * k)
            R.append(row)
        return R
    
    def __makeOne(self, row, pivotElement):
        """
        Make 1 to pivot element.\n
        (Divide metrix row 'row' by pivot element)
        """
        R = self.copy()
        for col in range(R.NC):
            R[row][col]= R[row][col] / pivotElement
        return R

    def __makeZero(self, pr:int, pc:int, upperEntries=True, lowerEntries=True):
        """
        make zero to below and above numbers of pivot element at pivot column 'pc'\n
        if you don't want to make zero to entries above pivot row 'pr', change argument upperEntries to False\n
        if you don't want to make zero to entries below pivot row 'pr'., change argument lowerEtnries to False\n
        """
        if not(upperEntries) and not(lowerEntries):
            raise ValueError("atleast one argument is true; upperTriangular, lowerTriangular")

        
        R = self.copy()
        for r in range(R.NR):
            # loop all row except pivot row
            if r == pr:
                continue
            
            # if you don't want to make zero to entries above pr.
            if not(upperEntries) and r<pr:
                continue
            
            # if you don't want to make zero to entries below pr.
            if not(lowerEntries) and r>pr:
                continue
            # number in pivot column which is either below or above the pivot element 
            # which we want to be zero
            valueToBeZero = R[r][pc]
            # for make zero we have to loop through all column to apply operation
            for c in range(R.NC):
                R[r][c] = R[r][c] -valueToBeZero * R[pr][c]
            # eg.  R1   = R1     - 5*R3
            # 5 = value to be zeor
            # R3 = pivot row
            # R1 is the row which contain 5 at pivot column
        return R

    def interchangeTwoRow(self, pos1:int, pos2:int):
        """
        Interchange two row of metrix which are at position 'pos1' and 'pos2'
        """
        # Create copy of metrix to prevent changing in original metrix
        R = self.copy()
        temp = R[pos1] 
        R[pos1] = R[pos2]
        R[pos2] = temp
        return R

    def interchangeTwoColumn(self, pos1:int, pos2:int):
        """
        Interchange two columns of metrix which are at positions 'pos1' and 'pos2'
        """
        R = self.copy()
        for r in range(R.NR):
            temp = R[r][pos1]
            R[r][pos1] = R[r][pos2]
            R[r][pos2] = temp
        return R

    def getReducedRowEcholonForm(self):
        """
        Reduced metrix to row echolon form
        """
        R = self.copy()
        pr = 0
        for pc in range(R.NC):
            # 1.Locate the left most column that does not consist entirely of zeros
            for r in range(pr,R.NR):
                if (R[r][pc] != 0):
                    break
            # if the column does not contain non zero number, continue (move to the next column)
            if (r == R.NR-1) and (R[r][pc] == 0):
                continue
            # 2.Interchange top row 'pr' with row 'r' to bring non zero entry (at row r) to top row (pr)
            if (r != pr):
                R = R.interchangeTwoRow(r, pr)
            pivotElement = R[pr][pc]
            # 3. make pivot element to 1
            R = R.__makeOne(pr, pivotElement)
            # 4. Add sutiable multiples of top row 'pr' to rows below and above so that 
            #    all entries below and above leading 1 is zero 
            R = R.__makeZero(pr, pc)
            # cover top row and begin again with step 1 applied to the submetrix that remains
            pr += 1
            # if pivot row number is greater than the number of rows of oirginal metrix which is happened 
            # due to number of column is greater than number of row in original metrix
            #     and
            # if previous submetix is only contain last row of original metrix then stop processing.
            if (pr > R.NR-1):
                break
        return R

    def transpose(self):
        """
        Interchanging Rows and Columns of Metrix
        if A is (m x n) metrix then transpose of A will be (n x m) metrix
        """
        R = cMetrics() # create empty metrix
        # transpose(Mij) = Mji
        for r in range(self.NC):
            row = []
            for c in range(self.NR):
                # append column entries of original metrix to row of transpose metrix
                row.append(self[c][r])
            R.append(row)
        return R

    def trace(self):
        """
        calculate the trace of scalar metrix\n
        if A is a square metrix then the trace of A is sum of the entries on the main diagonal of A\n
        if A is not a square metrix then trace of metrix is undefined
        """
        if self.NR != self.NC:
            raise ValueError("Trace is undefined")
        answer = 0
        for i in range(self.NR):
            answer += self[i][i]
        return answer
    
    def determinant(self):
        """
        Determinant only exist for Square Metrix\n
        We use Row Reduction method to find deteminant
        """
        # check for determinant condition
        if self.NR != self.NC:
            raise ValueError("Determinat only exist for square metrix")
        # Make copy of original
        R = self.copy()
        # consant will be the deteminant of Metrix
        constant = 1
        for i in range(R.NR):
            pivot = R[i][i]

            # if pivot is zero
            if (pivot == 0):
                # Look through the pivot's right entries for any non-zero entry.
                for c in range(i+1, R.NC):
                    if R[i][c] != 0:
                        break
                # if last entry is zero or there is no non zero entry to left of pivot element, then deteminant is zero
                if (i+1 >= R.NC) or ((c == R.NC-1) and (R[i][c] == 0)):
                    return 0
                # otherwise interchange the column where you find non zero entry, from the pivot column.
                else:
                    R = R.interchangeTwoColumn(i, c)
                    constant *= -1
                    # update pivot element
                    pivot = R[i][i]

            # common number from pivot row to make pivot element 1
            constant *= pivot
            R = R.__makeOne(i, pivot)

            # make zero 
            R = R.__makeZero(i, i, upperEntries=False)
        return constant

    def __deleteRowColumn(self, row, col):
        """
        Delete given row and column from matrix
        """
        # make copy of original metrix
        R = self.copy()
        # delete row but R is now a list object not cMetric object
        R = R[:row] + R[row+1:]

        # delete column
        for r in range(len(R)):
            R[r] = R[r][:col] + R[r][col+1:]

        return cMetrics(R)
        

    def minor(self, i, j):
        if (self.NR != self.NC):
            raise ValueError("A is not a square metrix")

        subMetrix = self.__deleteRowColumn(i, j)
        
        if (subMetrix.NR == 1) and (subMetrix.NC == 1):
            return subMetrix[0][0]
        
        return subMetrix.determinant()


    def applySimplexMethod(self):
        """
        Simplex Method is usually perform on metrix which contains a methamtical model of a business problem\n
        After performing simplex method, the answer is business problem found at last column of metrix
        """
        R = self.copy()

        # multipy top row with -1
        for c in range(R.NC):
            R[0][c] *= -1

        minimum = min(R[0])
        # we apply this process unitll the minimum of top row is greater than 0
        while (minimum < 0):
            # pc-> pivot column: column number which contain most negative number at top row
            pc = R[0].index(minimum)
            # find pivot row; pivot row is the row which 
            # have smallest ratio of (number of row at last column / number of row in pivot column)
            pr = 1 # let the row after top row is pivot row
            smallest_ratio = R[1][-1] / R[1][pc] # let the row after top row have smallest ratio
            # loop through all rows 
            for r in range(1, R.NR):
                ratio = R[r][-1] / R[r][pc] # ratio of rth Row
                # if roatio of rth Row is smaller than samallest ratio
                if ratio < smallest_ratio:
                    # update smallest ratio
                    smallest_ratio = ratio
                    # update pivot row 'pr' to the row r
                    pr = r
            # take out pivot element
            pe = R[pr][pc]

            R.makeOne(pr, pe)
            R.makeZero(pr, pc)
            minimum = min(R[0])


M2 = cMetrics([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(M2.minor(0, 0))
print(M2)