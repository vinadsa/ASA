# Punya Kevin Adi Santoso
def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n: # cek boundary
        return
    if visited[x][y] or grid[x][y] == 0:
        return
    
    visited[x][y] = True
    # explore tetangga
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(m)]

visited = [[False] * n for _ in range(m)]
jumlah_island = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            jumlah_island += 1

print(jumlah_island)