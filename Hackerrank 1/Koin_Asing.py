def Koin_Asing(koin, N):
    first = koin[0]
    if koin[1] == koin[2] and first != koin[1]: #ABBBBBBB:
        return 1
    else: #BABBBBBB
        for i in range(1, N):
            if koin[i] != first:
                return i + 1

N = 8
koin = input()[:N]

print(Koin_Asing(koin, N))