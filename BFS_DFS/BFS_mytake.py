from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        expand = queue.popleft()
        print(expand, end=" ")

        for child in graph[expand]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
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

bfs(graph, 1)