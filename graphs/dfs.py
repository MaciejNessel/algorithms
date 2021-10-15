#Implementation of DFS

def dfs_arr(graph):
    def dfs_visit_arr(g, u):
        print(u, end=' ')
        nonlocal time
        time += 1
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit_arr(g, v)
        time += 1

    time = 0
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_visit_arr(graph, u)


def dfs_matrix(graph):
    def dfs_visit_matrix(g, u):
        print(u, end=' ')
        nonlocal time
        time += 1
        visited[u] = True
        for i in range(n):
            if g[u][i] == 1:
                if not visited[i]:
                    parent[i] = u
                    dfs_visit_matrix(g, i)
        time += 1

    time = 0
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_visit_matrix(graph, u)


# Examples:
g_matrix= [[0, 1, 0, 0, 1, 0],
           [1, 0, 1, 0, 1, 1],
           [0, 1, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1],
           [1, 1, 1, 0, 0, 1],
           [0, 1, 1, 1, 1, 0]]
g_arr = [[4, 1], [0, 4, 5, 2], [1, 5, 3, 4], [2, 5], [0, 1, 2, 5], [1, 2, 4, 3]]

dfs_matrix(g_matrix)
print()
dfs_arr(g_arr)