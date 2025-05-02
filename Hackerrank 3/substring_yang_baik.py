# Punya Kevin Adi Santoso
str = input()

def substring_baik(str):
    if len(str) < 2: # basis partisi
        return ""
    
    for i in range(len(str)): 
        char = str[i]
        if char.lower() not in str or char.upper() not in str:
            kiri = substring_baik(str[:i]) # partisi
            kanan = substring_baik(str[i+1:])
            
            if len(kiri) >= len(kanan): # return partisi lbih panjang
                return kiri
            else:
                return kanan
    return str # sudah memenuhi syarat

print(substring_baik(str))
                