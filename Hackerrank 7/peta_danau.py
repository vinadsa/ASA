# Punya Kevin Adi Santoso
def dfs(x, y, komponen):
    if x < 0 or x >= m or y < 0 or y >= n: # cek boundary
        return
    if visited[x][y] or grid[x][y] == 1: # tidak visited dan bukan 1
        return
    
    visited[x][y] = True
    komponen.append((x,y))
    # explore tetangga, kalau 0 maka visited dan merupakan komponen
    dfs(x + 1, y, komponen)
    dfs(x - 1, y, komponen)
    dfs(x, y + 1, komponen)
    dfs(x, y - 1, komponen)
    

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(m)]

visited = [[False] * n for _ in range(m)]
jumlah_danau = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            komponen = [] # komponen adalah 0 yg terhubung dgn 0 awal
            dfs(i, j, komponen)
            if len(komponen) == 1 : # tidak punya komponen selain dirinya sndiri
                jumlah_danau += 1

print(jumlah_danau)