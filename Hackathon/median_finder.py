# Punya Kevin Adi Santoso
def quickSelect(arr, kiri, kanan, k):
    if kiri == kanan:
        return arr[kiri]
    
    pivot = partisi(arr, kiri, kanan) 
    
    if pivot == k:
        return arr[pivot]
    elif k < pivot:
        return quickSelect(arr, kiri, pivot - 1, k)
    else:
        return quickSelect(arr, pivot + 1, kanan, k)

def partisi(arr, kiri, kanan):
    pivot = arr[kanan]
    i = kiri
    
    for j in range(kiri, kanan):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[kanan] = arr[kanan], arr[i]
    return i


n = int(input())
arr = [int(x) for x in input().split()]
k = (n - 1) // 2

median = quickSelect(arr, 0, n-1, k)
print(median)