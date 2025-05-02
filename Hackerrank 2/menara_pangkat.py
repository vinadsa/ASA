#Punya Kevin Adi Santoso
def menara_pangkat(x, y):
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            half_power = menara_pangkat(x, y // 2)
            return half_power * half_power
        else:
            return x * menara_pangkat(x, y - 1)
    
x, y, m = map(int, input().split())

print(menara_pangkat(x, y) % m)