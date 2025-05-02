def quicksort(arr, i, j):
    if i >= j: # basis partisi
        return
        
    pivot = arr[(i + j) // 2]
    
    # partisi
    kiri = i
    kanan = j
    
    # logic quicksort
    while kiri <= kanan: 
        while kiri <= j and arr[kiri] < pivot:
            kiri += 1
            
        while kanan >= i and arr[kanan] > pivot:
            kanan -= 1
            
        if kiri <= kanan:
            arr[kiri], arr[kanan] = arr[kanan], arr[kiri]
            kiri += 1
            kanan -= 1
    
    # rekursi
    quicksort(arr, i, kanan)
    quicksort(arr, kiri, j)

N, K = map(int, input().split())
arr = [int(x) for x in input().split()]
quicksort(arr, 0, len(arr) - 1)

print(arr[-K]) # output terbesar ke K