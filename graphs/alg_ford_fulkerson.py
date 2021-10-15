# Implementation of Ford-Fulkerson algorithm

from queue import Queue
from math import inf


def bfs_search(n, s, t, parent):
    visited = [False for _ in range(n)]
    queue = Queue()

    queue.put(s)
    visited[s] = True

    while queue.qsize() > 0:
        u = queue.get()
        for i in range(n):
            if graph[u][i] > 0 and visited[i] is False:
                queue.put(i)
                visited[i], parent[i] = True, u

    return visited[t]


def ford_fulkerson(g, source, sink):
    n = len(g)
    parent = [None for _ in range(n)]
    max_flow = 0
    while bfs_search(n, source, sink, parent):
        path_flow = inf
        s = sink
        while s != source:
            path_flow = min(path_flow, g[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]

    return max_flow


# Example:
graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print("Max Flow: ", ford_fulkerson(graph, 0, 5))