from collections import deque

def build_graph(level_vals):
    """
    level_vals: list berisi int atau None, mewakili pohon secara level-order.
    Mengembalikan:
      - graph: dict {node_index: [child_index, ...]}
      - values: list, sama dengan level_vals, agar Anda bisa lookup nilai node.
    Node index 0 adalah root, anak kiri 2*i+1, anak kanan 2*i+2.
    """
    n = len(level_vals)
    graph = {}
    for i, v in enumerate(level_vals):
        if v is None:
            continue
        children = []
        left, right = 2*i + 1, 2*i + 2
        if left < n and level_vals[left] is not None:
            children.append(left)
        if right < n and level_vals[right] is not None:
            children.append(right)
        graph[i] = children
    return graph, level_vals

# Contoh penggunaan:
if __name__ == "__main__":
    # misal input
    raw = [1, 3, 2, 5, 3, None, 9]
    graph, values = build_graph(raw)

    # BFS asli Anda, cuman kali ini kita print nilai, bukan index
    def bfs_print_values(graph, values, start):
        visited = set([start])
        queue = deque([start])
        while queue:
            u = queue.popleft()
            print(values[u], end=" ")
            for w in graph.get(u, []):
                if w not in visited:
                    visited.add(w)
                    queue.append(w)
        print()

    bfs_print_values(graph, values, 0)
    # Output: 1 3 2 5 3 9
