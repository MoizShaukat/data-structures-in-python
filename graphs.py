# 1. First, we initialize the number of vertices in the graph.
# 2. Then, we define a dictionary to store the adjacency list.
# 3. Next, we add the edges to the graph.
# 4. Finally, we print the adjacency list.
# Time Complexity: O(V + E)

class graph:
    def __init__(self, vertices, directed=True):
        self.V = vertices
        self.nodes = range(self.V)
        
        # Define the type of graph
        # for directed graph   ->  directed = True
        # for undirected graph ->  directed = False
        self.m_directed = directed

        self.adj_list = {node: set() for node in self.nodes}

    def add_edge(self, node1, node2, weight=1):
        self.adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.adj_list[node2].add((node1, weight))

    def delete_edge(self, node1, node2, weight=1):
        self.adj_list[node1].remove((node2, weight))

        if not self.m_directed:
            self.adj_list[node2].remove((node1, weight))

    def print_adj_list(self):
        for key in self.adj_list.keys():
            print('node {}: {}'.format(key, self.adj_list[key]))


Graph = graph(5)
Graph.add_edge(0, 1, 3)
Graph.add_edge(0, 4, 6)
Graph.add_edge(1, 2, 9)
Graph.add_edge(2, 0, 1)
Graph.add_edge(2, 4, 11)
Graph.add_edge(2, 3, 17)
Graph.add_edge(3, 0, 18)
Graph.add_edge(3, 4, 4)
Graph.add_edge(4, 1, 7)


Graph.print_adj_list()


Graph.delete_edge(3, 0, 18)
Graph.delete_edge(3, 4, 4)
Graph.delete_edge(4, 1, 7)

Graph.print_adj_list()
