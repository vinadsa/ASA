# Punya Kevin Adi Santoso
arr = list(input())
def kromosom(arr):
    if len(arr) < 2:
        return False
    else:
        def rekurs(i, count):
            if i >= len(arr) - 1:
                return count % 2 == 0 and count != 0
            if arr[i] == 'X' and arr[i + 1] == 'Y':
                count += 1
            return rekurs(i + 1, count)
    
    return rekurs(0, 0)

print(kromosom(arr))