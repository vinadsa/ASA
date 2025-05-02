arr = [int(x) for x in input().split()]
X = int(input())

def binary_search(arr, i, j, X, kiri, kanan):
    if len(arr) == 0:
        return [kiri, kanan]
    
    if i > j:
        return [kiri, kanan]
    
    mid = (i + j) // 2
    
    # Handling index out of bounds
    if arr[mid] == X:
        # Periksa indeks sebelum dan sesudah, dengan perlindungan terhadap index out of bounds
        ada_kiri = mid > 0 and arr[mid - 1] == X
        ada_kanan = mid < len(arr) - 1 and arr[mid + 1] == X
        
        if not ada_kiri and not ada_kanan:
            # X hanya muncul sekali
            return [mid, mid]
        elif ada_kiri and ada_kanan:
            # X muncul di kedua sisi
            kiri_result = binary_search(arr, i, mid - 1, X, kiri, kanan)
            kanan_result = binary_search(arr, mid + 1, j, X, kiri_result[0], kiri_result[1])
            return [kiri_result[0], kanan_result[1]]
        elif ada_kiri:
            # X juga muncul di sebelah kiri, cari indeks awal X
            kiri_result = binary_search(arr, i, mid - 1, X, kiri, kanan)
            return [kiri_result[0], mid]
        elif ada_kanan:
            # X juga muncul di sebelah kanan, cari indeks akhir X
            kanan_result = binary_search(arr, mid + 1, j, X, mid, kanan)
            return [mid, kanan_result[1]]
        
    elif X > arr[mid]:
        return binary_search(arr, mid + 1, j, X, kiri, kanan)
    else:
        return binary_search(arr, i, mid - 1, X, kiri, kanan)

# Inisialisasi dengan 0 dan 0 sebagai default (bukan -1, -1)
hasil = binary_search(arr, 0, len(arr) - 1, X, -1, -1)
print(hasil)