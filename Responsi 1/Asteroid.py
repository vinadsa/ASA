def submatrix(matrix, x, y, n, m):
    sum = 0
    #vertikal
    for i in range(0, n):
        sum += matrix[i][y]

    #horizontal
    for j in range(0, m):
        sum += matrix[x][j]
    sum -= matrix[x][y]
    return sum
    
def asteroid(n, m, matrix):
    coordX = -1
    coordY = -1
    max_hancur = 0
    for i in range(n):
        for j in range(m):
            total_asteroid_hancur = submatrix(matrix, i, j, n, m)
            if total_asteroid_hancur > max_hancur:
                max_hancur = total_asteroid_hancur
                coordX = i
                coordY = j
    return coordX, coordY, max_hancur

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

x, y, jumlah = asteroid(n, m, matrix)
print(jumlah)
