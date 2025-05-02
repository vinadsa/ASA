# Punya Kevin Adi Santoso
arr = eval(input())

def wall_E(kiri, kanan, arr):
    if kiri > kanan: 
        return 0
    if kiri == kanan: 
        return 1
    
    mid = (kiri + kanan) // 2
    wall_E(kiri, mid, arr)
    wall_E(mid + 1, kanan, arr)
    
    rentang = []
    for i in range(kiri, kanan + 1):
        rentang.append(arr[i])
    rentang.sort(key=lambda x: x[0])

    grup = []
    for start, end in rentang:
        terjadwalkan = False
        for i in range(len(grup)):
            if start > grup[i]:
                grup[i] = end
                terjadwalkan = True
                break
        
        if not terjadwalkan:
            grup.append(end)
    
    return len(grup)

print(wall_E(0, len(arr) - 1, arr))