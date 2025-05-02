# Punya Kevin Adi Santoso
angka = int(input())
biner = []
for i in range (0, 32 - len(bin(angka)[2:])):
    biner.append('0')
biner.extend(list(bin(angka)[2:]))

def gol_bersejarah(biner, i, j):
    if i == j:
        return 1 if biner[i] == '1' else 0
    mid = (i + j) // 2
    
    kiri = gol_bersejarah(biner, i, mid)
    kanan = gol_bersejarah(biner, mid + 1, j)
    
    return kiri + kanan
    
print(gol_bersejarah(biner, 0, 31))

# print(sum(1 for bit in biner if bit == '1')) hehe 