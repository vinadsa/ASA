def DFS(start, graph, visited):
    if start in visited:
        return
    visited.add(start)
    for child in graph[start]:
        DFS(child, graph, visited)

visited = set()