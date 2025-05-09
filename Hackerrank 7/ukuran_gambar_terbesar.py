# Punya Kevin Adi Santoso
from collections import deque

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def konstruktor_tree(nodes):
    if not nodes:
        return None
    
    # convert ke int or none
    for i in range(len(nodes)):
        if nodes[i] == 'null':
            nodes[i] = None
        else:
            nodes[i] = int(nodes[i])
    
    root = Tree(nodes[0]) if nodes[0] is not None else None
    if not root:
        return None
    
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        current = queue.popleft()
        
        # left child
        if i < len(nodes) and nodes[i] is not None:
            current.left = Tree(nodes[i])
            queue.append(current.left)
        i += 1
        
        # right child
        if i < len(nodes) and nodes[i] is not None:
            current.right = Tree(nodes[i])
            queue.append(current.right)
        i += 1
    
    return root

def max_per_level(root):
    if not root:
        return []
    
    hasil = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        nilai_max = float('-inf')
        
        for _ in range(level_size):
            current = queue.popleft()
            nilai_max = max(nilai_max, current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        hasil.append(nilai_max)
    
    return hasil


n = int(input())
nodes = input().split()

root = konstruktor_tree(nodes)
hasil = max_per_level(root)

print(' '.join(map(str, hasil)))
