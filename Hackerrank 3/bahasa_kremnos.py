# Punya Kevin Adi Santoso
def is_ekuivalen(a, b):
    if a == b: # basis partisi
        return True
    if len(a) % 2 == 1: # kalau ganjil
        return False
    
    mid = len(a) // 2
    a1, a2 = a[:mid], a[mid:] # partisi
    b1, b2 = b[:mid], b[mid:]
    
    return (is_ekuivalen(a1, b1) and is_ekuivalen(a2, b2)) or (is_ekuivalen(a1, b2) and is_ekuivalen(a2, b1)) 

a, b = input(), input()
if is_ekuivalen(a, b):
    print("YA")
else:
    print("TIDAK")