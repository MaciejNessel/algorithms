# Implementation of topological sort

def topological_sort_arr(graph):
    def dfs_visit_arr(g, u):
        nonlocal res
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs_visit_arr(g, v)
        res.append(u)

    n = len(graph)
    res = []
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_visit_arr(graph, u)
    res.reverse()

    return res


def topological_sort_matrix(graph):
    def dfs_visit_matrix(g, u):
        nonlocal res
        visited[u] = True
        for i in range(n):
            if g[u][i] == 1:
                if not visited[i]:
                    dfs_visit_matrix(g, i)
        res.append(u)

    n = len(graph)
    res = []
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_visit_matrix(graph, u)
    res.reverse()

    return res


# Examples:
g_arr = [[1, 2], [2, 4], [], [], [3, 5, 6], [], []]
g_matrix = [[0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
print(topological_sort_arr(g_arr))
print(topological_sort_matrix(g_matrix))
