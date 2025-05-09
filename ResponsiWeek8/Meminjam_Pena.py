# Punya Kevin Adi Santoso
def hedar_dfs(n, graph, start):
    stack = [start - 1] # 0 indeks
    visited = [0] * n
    
    while stack:
        siswa_now = stack.pop()
        visited[siswa_now] += 1

        if visited[siswa_now] == 2:
            return siswa_now + 1

        siswa_ditandain = graph[siswa_now]
        next_siswa = siswa_ditandain - 1 
        
        stack.append(next_siswa)
        

n = int(input())
urutan_siswa = [int(x) for x in input().split()]

hasil_search = []
for i in range(1, n + 1):
    hasil = hedar_dfs(n, urutan_siswa, i)
    hasil_search.append(str(hasil))

print(" ".join(hasil_search))