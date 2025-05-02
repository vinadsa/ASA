N = int(input())
arr = [int(x) for x in input().split()]

def selisih_terkecil(arr, i, j):
    # Basis kasus: array hanya berisi satu elemen
    if j <= i:
        return float('inf'), -1
    
    # Basis kasus: array berisi dua elemen
    if j == i + 1:
        return abs(arr[j] - arr[i]), i
    
    mid = (i + j) // 2
    
    kiri = selisih_terkecil(arr, i, mid)
    kanan = selisih_terkecil(arr, mid+1, j)
    
    # Temukan minimum dari kiri dan kanan
    hasil = kiri if bandingkan(kiri, kanan) else kanan
    
    # Untuk mencari pasangan yang melintasi bagian tengah,
    # kita perlu mengurutkan dan membandingkan elemen dari kedua sisi
    # Tetapi pendekatan divide-and-conquer tidak efisien untuk masalah ini
    
    # Cari semua pasangan yang melintasi bagian tengah
    for i in range(i, mid+1):
        for j in range(mid+1, j+1):
            selisih = abs(arr[i] - arr[j])
            pasangan_tengah = (selisih, min(i, j))
            hasil = pasangan_tengah if bandingkan(pasangan_tengah, hasil) else hasil
    
    return hasil

def bandingkan(calon1, calon2):
    if calon1[0] < calon2[0]:
        return True
    elif calon1[0] == calon2[0]:
        return calon1[1] < calon2[1]
    return False

# Pasangan (selisih, indeks)
hasil = selisih_terkecil(arr, 0, N-1)
print(hasil[0], hasil[1]+1)  # +1 karena indeks dimulai dari 1
