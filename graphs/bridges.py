# Finding bridges in a graph

def bridges(graph):
    def dfs(g, u, n):
        nonlocal time
        visited[u] = True
        time += 1
        d[u] = time
        low[u] = time
        for v in range(n):
            if g[u][v]:
                if not visited[v]:
                    parent[v] = u
                    dfs(g, v, n)
                    low[u] = min(low[u], low[v])
                    if low[v] > d[u]:
                        b.append([u, v])
                elif v != parent[u]:
                    low[u] = min(low[u], d[v])

    n = len(graph)
    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [math.inf for _ in range(n)]
    low = [math.inf for _ in range(n)]
    b = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, n)

    return b