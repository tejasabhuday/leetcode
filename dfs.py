graph = {'0': set(['1', '2']),
'1': set(['3', '4']),
'2': set(['5']),
'3': set(['1']),
'4': set(),
'5': set()}

visited = set()
stack = []

def dfs(graph,visited,node):
    visited.add(node)
    stack.append(node)
    while stack:
        s = stack.pop()
        print(s , end = "")
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

dfs(graph, visited, '0')