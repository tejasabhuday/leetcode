import heapq
def unicost(graph,start,goal):
    priority_queue = [(0,[start])]
    visited = set()
    while priority_queue:
        current_cost ,path = heapq.heappop(priority_queue)
        current_node = path[-1]
        if current_node == goal:
            return(current_cost,path)
        if current_node not in visited:
            visited.add(current_node)
        for neighbor, cost in graph.get(current_node, {}).items():
            if neighbor not in visited:
                new_cost = current_cost + cost
                new_path = path + [neighbor]
                heapq.heappush(priority_queue,(new_cost, new_path))
        return None

graph = {
'A': {'B': 1, 'C': 4},
'B': {'A': 1, 'D': 2, 'E': 5},
'C': {'A': 4, 'F': 3},
'D': {'B': 2},
'E': {'B': 5, 'F': 1},
'F': {'C': 3, 'E': 1}
}
start = 'A'
goal = 'F'
result = unicost(graph, start, goal)
if result:
    print(f"Path: {result[1]} with cost: {result[0]}")
else:
    print("Goal not reachable")