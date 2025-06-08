from collections import defaultdict

N, M = map(int, input().split())

adj = [[] for x in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    if not (0 <= u < N and 0 <= v < N):
        raise ValueError("nah man")
    
    adj[u].append(v)
    adj[v].append(u)

    print(f"Iteration {_}")
    print(adj)

print(adj)