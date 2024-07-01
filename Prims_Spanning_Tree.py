import random

def prim(graph, start):
    mst = []
    visited = set()
    edges = [(0, start, None)]  # (weight, node, parent)

    while edges:
        # Randomly shuffle edges before selecting the smallest
        random.shuffle(edges)
        min_edge = min(edges, key=lambda e: e[0])
        edges.remove(min_edge)
        weight, node, parent = min_edge

        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, weight))

            # Add all edges from the current node
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    edges.append((edge_weight, neighbor, node))

    return mst

def main():
    graph = {
        'A': [('B', 2), ('G', 3)],
        'B': [('A', 2), ('C', 3), ('D', 4), ('E', 1)],
        'C': [('B', 3)],
        'D': [('B', 4)],
        'E': [('B', 1), ('F', 5)],
        'F': [('E', 5)],
        'G': [('A', 3), ('H', 2)],
        'H': [('G', 2), ('I', 6)],
        'I': [('H', 6)],
    }

    start_node = 'A'
    mst = prim(graph, start_node)

    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]}: {edge[2]}")

main()
