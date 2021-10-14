# Knapsack - two-dimensional problem
# Find maximum profit items, whose total weight and height does not exceed certain values


def knapsack_v2(weights, heights, profits, max_w, max_h):
    n = len(weights)
    f = [[[0 for _ in range(max_h + 1)] for _ in range(max_w + 1)] for _ in range(n)]

    for i in range(weights[0], max_w + 1):
        for j in range(heights[0], max_h + 1):
            f[0][i][j] = profits[0]

    for i in range(1, n):
        for j in range(max_w + 1):
            for k in range(max_h + 1):
                f[i][j][k] = f[i - 1][j][k]
                if j-weights[i]>=0 and k-heights[i]>=0:
                    f[i][j][k] = max(f[i][j][k], (f[i-1][j - weights[i]][k - heights[i]] + profits[i]))

    return f[n-1][max_w][max_h], f


def getsolution(f, weights, heights, profits, i, w, h):
   if i == 0:
       if w >= weights[0] and h >= heights[0]:
           return [0]
       else:
           return []

   if w >= weights[i] and h >= heights[i] and f[i][w][h] == f[i - 1][w - weights[i]][h - heights[i]] + profits[i]:
       return getsolution(f, weights, heights, profits, i - 1, w - weights[i], h - heights[i]) + [i]

   return getsolution(f, weights, heights, profits, i - 1, w, h)


# Example:
profits = [60, 100, 120]
weights = [10, 20, 30]
heights = [40, 60, 90]
max_weight = 40
max_height = 130
res, F = knapsack_v2(weights, heights, profits, max_weight, max_height)
print("Profit: ", res,"\nElements: ", getsolution(F, weights, heights, profits, len(weights) - 1, max_weight, max_height))
