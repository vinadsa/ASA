# Punya Kevin Adi Santoso
arr = [int(num) for num in input()[1:-1].split(",") if num.strip()]
X = int(input())

def binary_search(arr, i, j, X):
    if len(arr) == 0:
        return '"Tidak ditemukan"'
    
    if i > j:
        return '"Tidak ditemukan"'
    
    is_ascending = True
    if len(arr) > 1 and arr[0] > arr[-1]:
        is_ascending = False
    
    mid = (i + j) // 2

    if arr[mid] == X:
        return mid
    
    if is_ascending:
        # ascending
        if X > arr[mid]:
            return binary_search(arr, mid + 1, j, X)
        else:
            return binary_search(arr, i, mid - 1, X)
    else:
        # descending
        if X < arr[mid]:
            return binary_search(arr, mid + 1, j, X)
        else:
            return binary_search(arr, i, mid - 1, X)
            
print(binary_search(arr, 0, len(arr) - 1, X))