# Knapsack problem
# Time Complexity: O(n * MaxW)
# f(i, w) - the greatest profit that can be achieved without exceeding the MaxW weight


def knapsack(weights, profits, max_weight):
    n = len(weights)
    f = [[0] * (max_weight + 1) for _ in range(n)]

    for i in range(weights[0], max_weight + 1):
        f[0][i] = profits[0]

    for i in range(1, n):
        for w in range(1, max_weight + 1):
            f[i][w] = f[i - 1][w]
            if w >= weights[i]:
                f[i][w] = max(f[i][w], f[i - 1][w - weights[i]] + profits[i])

    return f[n - 1][max_weight], f


def get_solution(f, weights, profits, i, w):
    if i == 0:
        if w >= weights[0]: return [0]
        return []
    if w >= weights[i] and f[i][w] == f[i - 1][w - weights[i]] + profits[i]:
        return get_solution(f, weights, profits, i - 1, w - weights[i]) + [i]
    return get_solution(f, weights, profits, i - 1, w)
