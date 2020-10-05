"""
    BellFord is one of the SSSP(Single Source Shortest Path) Algorithms.
    Its complexity is much worse than Dijkstra Algorithm - O(VE).
    It is useful in those cases where edge weights are negative.
    It is also useful to find negative cycles.
"""

from collections import defaultdict as dd
from sys import maxsize


class Graph:
    def __init__(self, vertices):
        self.adjmat = dd(dict)
        self.vertices = vertices
        self.ordering = [0 for i in range(self.vertices)]
        self.vis = [False for i in range(self.vertices)]
        for i in range(vertices):
            self.adjmat[i] = dd(int)

    def insert(self, u, v, w=1):
        self.adjmat[u][v] = w

    def bellman_ford(self, source):
        dist = [maxsize for i in range(self.vertices)]
        dist[source] = 0
        for _ in range(self.vertices - 1):
            for i in self.adjmat.keys():
                for j in self.adjmat[i].keys():
                    dist[j] = min(dist[j], dist[i] + self.adjmat[i][j])
        # Checking for the negative cycles
        for _ in range(self.vertices - 1):
            for i in self.adjmat.keys():
                for j in self.adjmat[i].keys():
                    # If a better answer exists for a node than it is in negative cycle
                    # or is being affected by some negative cycle.
                    if dist[j] > dist[i] + self.adjmat[i][j]:
                        dist[j] = -maxsize
        return dist


G = Graph(6)
G.insert(0, 1, 3)
G.insert(0, 5, 5)
G.insert(1, 5, -9)
G.insert(1, 3, 6)
G.insert(5, 3, -8)
G.insert(3, 2, 5)
G.insert(3, 4, 7)
G.insert(2, 4, 4)
print(G.bellman_ford(0))
