# Implementation of Dijkstra algorithm

from queue import PriorityQueue
from math import inf


def get_solution(p, i, res):
    if p[i] == -1:
        return [i] + res
    return get_solution(p, p[i], [i] + res)


def dijkstry_matrix(g, s, e):
    def relax_matrix(u, v):
        if d[v] > d[u] + g[u][v]:
            d[v] = d[u] + g[u][v]
            parent[v] = u
            pq.put((d[v], v))

    n = len(g)
    d = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]

    d[s] = 0
    pq = PriorityQueue()
    pq.put((d[s], s))

    while pq.qsize()>0:
        u = pq.get()
        for v in range(n):
            if g[u[1]][v] > 0:
                relax_matrix(u[1], v)

    res = get_solution(parent,e,[])
    print(f"Route: {res}\nCost: {d[e]}")


def dijkstry_arr(G,s,e):
    def relax_arr(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u
            pq.put((d[v], v))

    n = len(G)
    d = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    pq = PriorityQueue()

    d[s] = 0
    pq.put((d[s], s))

    while pq.qsize()>0:
        u = pq.get()

        for v in G[u[1]]:
            relax_arr(u[1], v[0], v[1])

    res = get_solution(parent,e,[])
    print(f"Route: {res}\nCost: {d[e]}")


# Examples:
start = 0
end = 4
graph = [[0, 0, 1, 5, 0],
         [0, 0, 8, 3, 1],
         [1, 8, 0, 2, 7],
         [5, 3, 2, 0, 0],
         [0, 1, 7, 0, 0]]

graph_arr = [[(2, 1), (3, 5)],
             [(3, 3), (2, 8), (4, 1)],
             [(0, 1), (1, 8), (3, 2), (4, 7)],
             [(0, 5), (1, 3), (2, 2)],
             [(1, 1), (2, 7)]]


dijkstry_matrix(graph, start, end)
dijkstry_arr(graph_arr, start, end)
