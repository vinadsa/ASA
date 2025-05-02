
def Pecahan_Uang_Minumum(X):
    i = len(pecahan) -1
    X = X
    counter = 0
    while X > 0:
        while i >= 0:
            if X - pecahan[i] >= 0:
                X -= pecahan[i]
                counter += 1
            else:
                i -= 1

    return counter

pecahan = [1, 5, 10, 25, 50]
X = int(input())

print(Pecahan_Uang_Minumum(X))
