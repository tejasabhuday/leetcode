import random

def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]

    while current != goal:
        neighbors = list(graph[current].keys())
        if not neighbors:
            return None
        
        next_node = min(neighbors, key=lambda n: heuristic[n])
        if heuristic[next_node] >= heuristic[current]:
            return None
        
        current = next_node
        path.append(current)
    
    return path

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 2,
    'F': 0
}

start = 'A'
goal = 'F'

result = hill_climbing(graph, start, goal,heuristic)

if result:
    print(f"Path: {' -> '.join(result)}")
else:
    print("Goal not reachable")
