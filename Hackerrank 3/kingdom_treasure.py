# Punya Kevin Adi Santoso
N = int(input())
arr = [int(x) for x in input().split()]

def mencari_max(arr):
    if len(arr) == 0: # handle case utk array kosong
        return -1
    else:
        return maks(0, len(arr) - 1, arr)
    
def maks(i, j, arr):
    if i == j: # basis partisi
        return arr[i]
    mid = (i + j) // 2
    return max(maks(i, mid, arr), maks(mid + 1, j, arr))

print(mencari_max(arr))