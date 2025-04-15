graph={'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': ['F'],
'F': [],
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        current = queue.pop(0)
        print("",current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
bfs(visited,graph,'A')