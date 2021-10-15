# Implementation of an algorithm that checks if the graph is bipartite

from queue import Queue


def bipartite(G, s):
    n = len(G)
    visited = [None for _ in range(n)]
    que = Queue()
    que.put(s)
    visited[s] = True
    while que.qsize() > 0:
        u = que.get()
        for i in range(n):
            if G[u][i] == 1:
                if visited[u] is visited[i]:
                    return False
                if visited[i] is None:
                    visited[i] = not visited[u]
                    que.put(i)
    return True


g_true = [[0, 1, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

g_false = [[0, 1, 1, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 1, 0],
           [1, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 0, 1, 1, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 1, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

print(bipartite(g_true, 0))
print(bipartite(g_false, 0))
