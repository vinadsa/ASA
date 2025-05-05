from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.pop()
        if node not in visited:
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
    return visited