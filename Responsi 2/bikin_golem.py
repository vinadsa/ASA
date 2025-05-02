# Punya Kevin Adi Santoso
def bikin_golem(permutasi):
    if len(permutasi) == N:
        return [permutasi]
    
    hasil = []
    for angka in range(1, N+1):
        if angka not in permutasi:
            if len(permutasi) >= 2:
                if not ((permutasi[-1] > permutasi[-2] and permutasi[-1] > angka) or 
                        (permutasi[-1] < permutasi[-2] and permutasi[-1] < angka)):
                    continue
            hasil.extend(bikin_golem(permutasi + [angka]))
    return hasil

N = int(input())
for permutasi in bikin_golem([]):
    print(''.join(map(str, permutasi)))
