from collections import defaultdict, deque

def is_valid_path(n, edges, start, target):
    """
    Determine if there is a valid path from start to target using BFS
    
    Parameters:
    - n: number of nodes (0 to n-1)
    - edges: list of edges where each edge is [u, v]
    - start: starting node
    - target: target node
    
    Returns:
    - boolean: True if path exists, False otherwise
    """
    # Build adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    
    # BFS algorithm
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current_node = queue.popleft()
        
        # If we've reached the target, return True
        if current_node == target:
            return True
        
        # Explore all neighbors
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # tidak ketemu
    return False


n = int(input().strip())
e = int(input().strip())

edges = []
for x in range(e):
    u, v = map(int, input().strip().split())
    edges.append([u, v])

start, target = map(int, input().strip().split())

# Determine if valid path exists
print(is_valid_path(n, edges, start, target))