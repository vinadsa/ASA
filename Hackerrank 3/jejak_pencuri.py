# Punya Kevin Adi Santoso
a = [int(x) for x in input().split()]
N = a[0]
X = a[1]
arr = [int(x) for x in input().split()]

def pencarian_first(arr, kiri, kanan, X):
    if kiri > kanan:
        return -1
    
    mid = (kiri + kanan) // 2
    
    if arr[mid] == X: # kalau tengah == X, cek kirinya
        first = pencarian_first(arr, kiri, mid - 1, X)
        if first and first != -1:
            return first
        else:
            return mid + 1
    elif arr[mid] < X: # kalau tengah < X, berarti pasti di kanan
        return pencarian_first(arr, mid + 1, kanan, X)
    else:
        return pencarian_first(arr, kiri, mid - 1, X)

    # 8 8 9 9 10 10 11 11 11 13 18 18
def pencarian_last(arr, kiri, kanan, X):
    if kiri > kanan:
        return -1
    
    mid = (kiri + kanan) // 2
    
    if arr[mid] == X: # kalau tengah == X, cek kanannya
        last = pencarian_last(arr, mid + 1, kanan, X)
        if last and last != -1:
            return last
        else:
            return mid + 1
    elif arr[mid] > X: # kalau tengah > X, berarti pasti di kiri
        return pencarian_last(arr, kiri, mid - 1, X)
    else:
        return pencarian_last(arr, mid + 1, kanan, X)
    
first = pencarian_first(arr, 0, len(arr) - 1, X)
last = pencarian_last(arr, 0, len(arr) - 1, X)

print(first, last)
    