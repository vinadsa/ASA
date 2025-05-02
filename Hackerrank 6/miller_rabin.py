# Punya Kevin Adi Santoso
import random

def miller_rabin(n, k):
    if n <= 1:
        return False
    if n == 2 or n == 3:  # pasti prima
        return True
    if n % 2 == 0:
        return False  # genap pasti bkn prima

    # n-1 = 2^s * d dengan d ganjil
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 2) # pilih bil acak dari 2 ke n - 2
        x = pow(a, d, n) # x = a^d mod n
        if x == 1 or x == n - 1:
            continue
            
        for j in range(0, s - 1): # loop j idx 1 ke s - 1
            x = (x * x) % n
            if x == n - 1:
                break
                
        else:
            return False
    return True


N = int(input())
k = 10

for i in range(N): # output masing2
    n = int(input())

    if miller_rabin(n, k):
        print("Prima")
    else:
        print("Komposit")