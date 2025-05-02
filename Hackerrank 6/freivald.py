# Punya Kevin Adi Santoso
import random

N = int(input())
# matrix A
a = [list(map(int, input().split())) for i in range(N)]
# matrix B
b = [list(map(int, input().split())) for i in range(N)]
# matrix C
c = [list(map(int, input().split())) for i in range(N)]

k = 10

def freivald(a, b, c, N):
    # vektor acak {0, 1}
    r = [random.randrange(2) for i in range(N)]
    
    # hitung x = Br
    x = [0] * N
    for i in range(N):
        for j in range(N):
            x[i] += b[i][j] * r[j]
    # hitung y = Ax -> (A * Br)
    y = [0] * N
    for i in range(N):
        for j in range(N):
            y[i] += a[i][j] * x[j]
    # hitung z = Cr
    z = [0] * N
    for i in range(N):
        for j in range(N):
            z[i] += c[i][j] * r[j]
    
    # cek y != z
    for i in range(N):
        if y[i] != z[i]:
            return False
        
    return True


def isSama(a, b, c, N, k):
    for i in range(k):
        if not freivald(a, b, c, N):
            return False
        
    return True

if isSama(a, b, c, N, k):
    print("Sama")
else:
    print("Tidak Sama")
