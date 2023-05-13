arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 0
high = len(arr) -1

def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return print(f"Found at index {mid}")
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)
        elif arr[mid] < key:
            return binary_search(arr, mid+1, high, key)
        
binary_search(arr, 0, len(arr))