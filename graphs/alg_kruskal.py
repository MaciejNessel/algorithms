# Implementation of Kruskal algorithm

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(g):
    n = len(g)
    g.sort(key = lambda x: x[2])

    A = []
    arr = [Node(i) for i in range(n)]
    for i in range(0, n):
        x = arr[g[i][0]]
        y = arr[g[i][1]]
        x = find(x)
        y = find(y)
        if x != y:
            union(x, y)
            A.append([g[i][0], g[i][1]])

    print(A)


# Example:
graph = [(0, 1, 7), (0, 2 ,2), (0, 3, 8), (0, 5, 3), (1, 3, 1), (2, 4, 5), (3, 4, 4), (3, 5, 12), (4, 5, 6)]
kruskal(graph)