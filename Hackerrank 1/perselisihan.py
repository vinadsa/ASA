def perselisihan(A):
    if len(A) > 1:
        terkecil = abs(A[0] - A[1])
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if abs(A[i] - A[j]) <= terkecil:
                    terkecil = abs(A[i] - A[j])
        return terkecil



A = [int(x) for x in input().split()]

print(perselisihan(A))