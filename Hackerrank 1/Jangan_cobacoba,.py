import ast

def coba(arr, X):
    i = 0
    while i < len(arr):
        if arr[i] == X:
            return i
        else:
            i += 1
    return 0


arr = ast.literal_eval(input(""))
X = int(input())

Y = coba(arr, X)
if Y == 0:
    print('"Tidak ditemukan"')
else:
    print(Y)