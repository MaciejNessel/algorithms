# Implementation of Floyd-Warshall algorithm

from math import inf


def floyd_warshall(g):
    n = len(g)
    d = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                d[i][j] = 0
            elif g[i][j] !=0:
                d[i][j] = g[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d


# Example
graph = [[0, 7, 2, 8, 0, 3],
         [7, 0, 0, 1, 0, 0],
         [2, 0, 0, 0, 5, 0],
         [8, 1, 0, 0, 4, 12],
         [0, 0, 5, 4, 0, 6],
         [3, 0, 0, 12, 6, 0]]

print(floyd_warshall(graph))