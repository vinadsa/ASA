#Punya Kevin Adi Santoso
def selisih_optimal(array, i, j):
    if i > j:
        return 0
    
    pilih_kiri = array[i] - selisih_optimal(array, i + 1, j)
    pilih_kanan = array[j] - selisih_optimal(array, i, j - 1)
    
    return max(pilih_kiri, pilih_kanan)

array = list(map(int, input().split()))
n = len(array)

selisih = selisih_optimal(array, 0, n - 1)

print("True"    if selisih >= 0 
                else "False") 