N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

def daftar_permutasi(N):
    permutasi = [[]]  # Mulai dengan daftar kosong sebagai permutasi awal
    for num in range(N):
        new_permutasi = []  # Daftar sementara untuk menyimpan permutasi baru
        for p in permutasi:
            # Tambahkan elemen baru ke semua posisi yang mungkin
            for i in range(len(p) + 1):
                new_p = p[:i] + [num] + p[i:]  # Sisipkan elemen baru di posisi i
                new_permutasi.append(new_p)     # Tambahkan permutasi baru ke daftar
        permutasi = new_permutasi  # Perbarui permutasi dengan daftar baru
    return permutasi

# Cetak semua permutasi yang dihasilkan
permutasi = daftar_permutasi(N)
def biaya_minimum(matrix, permutasi):
    min = 1000000000
    for p in permutasi:
        sum = 0
        for i in range(len(p)):
            sum += matrix[i][p[i]]
        if sum < min:
            min = sum
    return min

print(biaya_minimum(matrix, permutasi))