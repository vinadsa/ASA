# Punya Kevin Adi Santoso
n = int(input())
arr = [int(x) for x in input().split()]

def koin_palsu(arr, i, j):
    if i == j:
        return i
    
    mid = (i + j) // 2
    
    if (j - i + 1) % 2 == 0:  # jika genap
        sum_kiri = sum(arr[i:mid + 1])
        sum_kanan = sum(arr[mid + 1:j + 1])
        
        if sum_kiri < sum_kanan:
            return koin_palsu(arr, i, mid)
        else:
            return koin_palsu(arr, mid + 1, j)
    else:  # jika ganjil
        sum_kiri = sum(arr[i:mid])
        sum_kanan = sum(arr[mid + 1:j + 1])
        
        if sum_kiri == sum_kanan:
            return mid
        elif sum_kiri < sum_kanan:
            return koin_palsu(arr, i, mid - 1)
        else:
            return koin_palsu(arr, mid + 1, j)

print(koin_palsu(arr, 0, n - 1))