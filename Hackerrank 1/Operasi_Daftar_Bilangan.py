def operasi_daftar_bilangan(arr):
    if len(arr) % 2 == 0:
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        return sum
    else:
        tengah = arr[len(arr)//2]
        sum = 0
        for i in range(len(arr)):
            if i == len(arr)//2:
                continue
            sum += arr[i]
        return sum * tengah



arr = [int(x) for x in input().split()]

print(arr)
print(operasi_daftar_bilangan(arr))