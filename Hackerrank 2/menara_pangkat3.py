# Punya Kevin Adi Santoso
x, y, m = map(int, input().split())
def exp_mod(x, y, m): #fungsi eksponen modular (square and multiply)
    hasil = 1
    while y > 0:
        if y % 2 == 1:
            hasil = (hasil * x) % m
        x = (x * x) % m
        y //= 2
    return hasil

def menara_pangkat(x, y, m):
    if m == 1:
        return 0
    if y == 0:
        return 1
    return exp_mod(x, menara_pangkat(x, y - 1, m), m)

print(menara_pangkat(x, y, m))