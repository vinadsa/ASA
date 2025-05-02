# Punya Kevin Adi Santoso
N, kotak = map(int, input().split())
arr = [int(x) for x in input().split()]
 
def jml_unik(sub_arr): # hitung jml elemen unik
    return len(set(sub_arr))

def partisi(i, segment, arr):
    n = len(arr)
    if segment == 0: # basis, segment habis
        if i == n:
            return 0
        else:
            return -10000
    
    best = -10000
    for j in range(i + 1, n - segment + 3):
        cost = jml_unik(arr[i:j])
        best = max(best, cost + partisi(j, segment - 1, arr))
    
    return best


hasil = partisi(0, kotak, arr)
print(hasil)
