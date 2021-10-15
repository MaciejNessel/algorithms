#Implementation of bfs
from queue import Queue

def bfs_arr(g, s):
    n = len(g)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)]
    que = Queue()
    que.put(s)
    visited[s] = True
    while que.qsize()>0:
        u = que.get()
        print(u, end =' ')
        for x in g[u]:
            if visited[x] is False:
                visited[x] = True
                d[x] = d[u] + 1
                parent[x] = u
                que.put(x)


def bfs_matrix(g, s):
    n = len(g)
    que = Queue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)]
    que.put(s)
    visited[s] = True
    while que.qsize()>0:
        u = que.get()
        print(u, end =' ')
        for i in range(n):
            if g[u][i] == 1:
                if visited[i] is False:
                    visited[i] = True
                    d[i] = d[u] + 1
                    parent[i] = u
                    que.put(i)


# Examples:
g_arr = [[4, 1], [0, 4, 5, 2], [1, 5, 3, 4], [2, 5], [0, 1, 2, 5], [1, 2, 4, 3]]
g_matrix = [[0, 1, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1],
            [0, 1, 1, 1, 1, 0]]

bfs_matrix(g_matrix, 0)
print()
bfs_arr(g_arr, 0)