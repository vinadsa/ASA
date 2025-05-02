#Punya Kevin Adi Santoso
def euler(n): #euler totient
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def power_tower_mod(x, y, m): #kalkulasi x^(x^(...^x)) mod m
    if m == 1: #semua mod 1 pasti 0
        return 0
    if y == 0:
        return 1
    phi_m = euler(m) #phi(m)
    exp = power_tower_mod(x, y - 1, phi_m) 
    return pow(x, exp, m)


x, y, m = map(int, input().split())
print(power_tower_mod(x, y, m))