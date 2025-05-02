def dfs(graph, start, visited):
    if start in visited:
        return
    print(start, end=" ")
    visited.add(start)
    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)

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

dfs(graph, 1, set())