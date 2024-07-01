class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    edges = []
    nodes = set(graph.keys())
    node_to_index = {node: idx for idx, node in enumerate(nodes)}

    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))

    edges.sort()  # Sort edges by weight

    n = len(nodes)
    mst = []
    ds = DisjointSet(n)

    for weight, u, v in edges:
        if ds.find(node_to_index[u]) != ds.find(node_to_index[v]):
            ds.union(node_to_index[u], node_to_index[v])
            mst.append((u, v, weight))

    return mst

# Example usage:
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

mst = kruskal(graph)
print("Edges in the Minimum Spanning Tree (Kruskal's algorithm):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
