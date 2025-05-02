def Belanjaan_Budi(X, A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == X:
                print(i, j)


X = int(input())
N = int(input())
A = [int(x) for x in input().split()[:N]]

Belanjaan_Budi(X, A)


