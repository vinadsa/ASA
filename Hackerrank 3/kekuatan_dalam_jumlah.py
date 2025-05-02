# Punya Kevin Adi Santoso
def elemen_mayoritas(arr, kiri, kanan):
    if kiri == kanan: # basis partisi
        return arr[kiri]
    
    tengah = (kiri + kanan) // 2 
    mayoritas_kiri = elemen_mayoritas(arr, kiri, tengah) #rekursi partisi kiri->tengah
    mayoritas_kanan = elemen_mayoritas(arr, tengah + 1, kanan) #rekursi partisi tengah->kanan
    
    if mayoritas_kiri == mayoritas_kanan:
        return mayoritas_kiri
    
    count_kiri = sum(1 for x in arr[kiri:kanan + 1] if x == mayoritas_kiri) 
    count_kanan = sum(1 for x in arr[kiri:kanan + 1] if x == mayoritas_kanan)
    
    if count_kiri > count_kanan:
        return mayoritas_kiri
    else:
        return mayoritas_kanan

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    kandidat = elemen_mayoritas(arr, 0, n - 1)
    if arr.count(kandidat) > n // 2:
        print(kandidat)
    else:
        print(-1)

main()
