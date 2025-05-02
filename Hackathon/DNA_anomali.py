# Punya Kevin Adi Santoso
def DNA_anomali(s):
    count_A = 0
    count_T = 0
    count_C = 0
    count_G = 0

    for i in range(len(s)):
        if s[i] == 'A':
            count_A += 1
        elif s[i] == 'T':
            count_T += 1
        elif s[i] == 'C':
            count_C += 1
        elif s[i] == 'G':
            count_G += 1

        if count_T > count_A or count_G > count_C:
            print(i + 1) 
            break
    else:
        print(-1)

s = input().strip()
DNA_anomali(s)