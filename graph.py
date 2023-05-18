class Graph:
    def __init__(self, number_of_vertices):
        self.v = number_of_vertices
        self.edges = [
            [float('inf') for i in range(number_of_vertices)] for j in range(number_of_vertices)
        ]
        self.visited = []

    def add_edge(self, u, v, w):
        self.edges[u][v] = w
        self.edges[v][u] = w