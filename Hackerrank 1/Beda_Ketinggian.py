def Beda_Ketinggian(arr):
    tertinggi = max(arr)
    terendah = min(arr)
    
    return abs(tertinggi - terendah)


n = int(input())
arr = [int(x) for x in input().split()]

print((Beda_Ketinggian(arr)))