from collections import deque

def BFS(start, graph):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        expand = queue.popleft()
        print(expand, end=' ')
        for child in graph[expand]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return visited

