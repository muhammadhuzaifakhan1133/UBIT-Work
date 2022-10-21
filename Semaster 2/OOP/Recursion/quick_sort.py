def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low,  pi-1)
        quickSort(arr, pi+1, high)


def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    return i + 1

M = [-3, 2, 1, -12, 99, 45, 0, 4]
quickSort(M, 0, len(M)-1)
print(M)