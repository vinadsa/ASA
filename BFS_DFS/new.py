from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)
    return visited


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return visited

graph = {
    1: [2, 6, 7, 10, 11],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4],
    6: [1],
    7: [1, 8, 9],
    8: [7],
    9: [7, 10],
    10: [1, 9, 11],
    11: [1, 10]
}

print(bfs(graph, 1))
print(dfs(graph, 1))