def DFS(start, graph):
    visited = set()
    stack = [start]

    while stack :
        expand = stack.pop()
        if expand not in visited:
            visited.add(expand)
            for child in graph[expand]:
                if child not in visited:
                    stack.append(child)

    return visited