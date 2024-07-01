import random
def dfs(graph, start_node):
    visited = set() # set to track visited nodes
    stack = [start_node] #initialize stack with the starting node

    while stack:
        node = stack.pop() #pop the top node from the stack
        if node not in visited:
            visited.add(node)
            print(node, end=" ") #Print or process the node here

            ##Randomly shuffle the neighbors before pushing onto the stack
            neighbors = graph[node]
            random.shuffle(neighbors)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)


#example graph usage
graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

start_node = 'A'
print("Rndomized DFS traversal starting from node", start_node)
dfs(graph, start_node)