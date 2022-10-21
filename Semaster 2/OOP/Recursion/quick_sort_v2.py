def quickSort(seq: list):
    length = len(seq)
    if length <= 1:
        return seq
    pivot = seq[0]
    less = []
    greater = []
    for i in seq[1:]:
        if i <= pivot:
            less.append(i)
        else:
            greater.append(i)
    return quickSort(less) + [pivot] + quickSort(greater)



M = [-3, 2, 1, -12, 99, 45, 0, 4]
sortedList = quickSort(M)
print(sortedList)

    
        
            