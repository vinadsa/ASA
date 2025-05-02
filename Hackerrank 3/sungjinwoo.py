nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]

def hitung_meningkat(nums1, nums2):
    n = len(nums1)
    # Menyimpan posisi setiap elemen di nums1
    posisi = [0] * n
    for i in range(n):
        posisi[nums1[i]] = i
    
    # Mengubah nums2 berdasarkan posisi di nums1
    transformasi = [0] * n
    for i in range(n):
        transformasi[i] = posisi[nums2[i]]
    
    return bagi_kuasai(transformasi, 0, n-1)

def bagi_kuasai(arr, awal, akhir):
    # Basis: jika hanya ada 2 elemen atau kurang, tidak ada pola meningkat 3-elemen
    if akhir - awal + 1 <= 2:
        return 0
    
    tengah = (awal + akhir) // 2
    
    # Hitung pola di bagian kiri dan kanan secara rekursif
    jumlah_kiri = bagi_kuasai(arr, awal, tengah)
    jumlah_kanan = bagi_kuasai(arr, tengah + 1, akhir)
    
    # Hitung pola yang melintasi bagian tengah
    jumlah_lintas = hitung_lintas(arr, awal, tengah, akhir)
    
    return jumlah_kiri + jumlah_kanan + jumlah_lintas

def hitung_lintas(arr, awal, tengah, akhir):
    jumlah = 0
    # Cari pola (i, j, k) di mana i di bagian kiri, k di bagian kanan
    # dan elemen arr[i] < arr[j] < arr[k]
    for i in range(awal, tengah + 1):
        for k in range(tengah + 1, akhir + 1):
            if arr[i] < arr[k]:
                # Jika elemen i dan k meningkat, cek jika ada j di antaranya
                # yang memenuhi arr[i] < arr[j] < arr[k]
                for j in range(i + 1, k):
                    if arr[i] < arr[j] < arr[k]:
                        jumlah += 1
    
    return jumlah

hasil = hitung_meningkat(nums1, nums2)
print(hasil)