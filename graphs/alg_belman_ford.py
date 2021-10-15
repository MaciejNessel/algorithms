# Implementation of Bellman–Ford Algorithm

from math import inf

def get_solution(p,i,res):
    if p[i] is None:
        return [i] + res
    return get_solution(p, p[i], [i] + res)


def bellman_ford(G, s, t):
    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    #1. initialization:
    n = len(G)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0

    # 2. relaxation:
    for i in range(n-1):
        for v in range(n):
            for u in G[v]:
                relax(v, u[0], u[1])

    # 3. verification:
    for v in range(n):
        for u in G[v]:
            if d[u[0]] > d[v] + u[1]:
                return False

    #Found route s - t:
    print(f"Found route: {get_solution(parent, t, [])}")
    return True


# Example:
g = [[(1,5)], #0
     [(3,3),(4,9)],
     [(1,-3),(0,3)],
     [(4,3),(5,2)],
     [(5,-5),(2,-1)],
     [(2,8),(0,9)]]

print(bellman_ford(g, 0, 5))