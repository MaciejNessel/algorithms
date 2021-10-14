# Wander on chessboard (n x n)
# Find minimum cost of transition from field A(1,1) to B(n,n)
# Use only move down and right


def find_way(array):
    n = len(array)
    f = [[0 for _ in range(n)] for _ in range(n) ]

    for i in range(1,n):
        f[1][i] = array[1][i]
        f[i][1] = array[i][1]

    for i in range(1, n):
        for j in range(1, n):
            f[i][j] = min(f[i-1][j] + array[i][j], f[i][j - 1] + array[i][j])

    return f


def find_path_res_recur(arr, costs, m, n, res):
    if m == 1 and n == 1:
        return res
    res = [[m, n]] + res
    if m > 1 and costs[m][n] == costs[m - 1][n] + arr[m][n]:
        return find_path_res_recur(arr, costs, m - 1, n, res)
    if n > 1 and costs[m][n] == costs[m][n - 1] + arr[m][n]:
        return find_path_res_recur(arr, costs, m, n - 1, res)


def print_res(array):
    cost = find_way(array)
    n = len(array)
    print(f"Finded way: {find_path_res_recur(array, cost, n - 1, n - 1, [])}\nCost: {cost[n - 1][n - 1]}")


# Example:
data = [[0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1]]

print_res(data)

