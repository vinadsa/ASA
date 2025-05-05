def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

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

dfs_iterative(graph, 1)