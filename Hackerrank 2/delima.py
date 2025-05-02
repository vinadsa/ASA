# Punya Kevin Adi Santoso
N = int(input())
delima = [int(x) for x in input().split()]
sum_berat = sum(delima)

def selisih_terkecil(i, berat_sekarang, N, sum_berat, delima):
    if i == N:
        return abs(berat_sekarang - (sum_berat - berat_sekarang))
    else:
        kantong_1 = selisih_terkecil(i + 1, berat_sekarang + delima[i], N, sum_berat, delima)
        kantong_2 = selisih_terkecil(i + 1, berat_sekarang, N, sum_berat, delima)
        return min(kantong_1, kantong_2)

print(selisih_terkecil(0, 0, N, sum_berat, delima))