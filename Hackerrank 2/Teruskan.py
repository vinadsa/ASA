# Punya Kevin Adi Santoso
arr = eval(input())
x = int(input())
n = len(arr)
def pencarian_rekursif(arr, n, x):
    if n < 0:
        return -1
    if arr[n] == x:
        return n

    else:
        return pencarian_rekursif(arr, n - 1, x)

print(pencarian_rekursif(arr, n - 1, x) if pencarian_rekursif(arr, n - 1, x) != -1 else '"Tidak ditemukan"')


