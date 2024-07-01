import random

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end="")
    neighbors = graph[node]
    random.shuffle(neighbors)
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    graph = {
        'A' : ['B','G'],
        'B' : ['C', 'D', 'E'],
        'C' : [],
        'D' : [],
        'E' : ['F'],
        'F' : [],
        'G' : ['H'],
        'H' : ['I'],
        'I' : [], 
    }

    #the set is used for optimized membership testing
    #ensuring eahc element is unique
    visited = set()
    print(type(visited))
    dfs(graph, 'A', visited)
    print("\nVisted nodes:", visited)

main()