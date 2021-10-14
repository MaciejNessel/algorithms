# Find optimal cost of matrix multiplication
# Time complexity: O(n)

def min_cost_matrix(T):
    n = len(T)
    f = [0 for _ in range(n)]
    p = [[0,0] for _ in range(n)]

    f[1] = T[0][0] * T[0][1] * T[1][1]
    p[0][0], p[0][1] = T[0][0], T[0][1]
    p[1][0], p[1][1] = T[0][0], T[1][1]

    for i in range(2, n):
        # brackets: (X*Y)*Z
        f[i] = f[i-1] + p[i-1][0] * p[i-1][1] * T[i][1]
        p[i][0], p[i][1] = T[i][0], T[i][1]
        # brackets: X*(Y*Z)
        if f[i] > f[i-2] + T[i-1][0] * T[i-1][1] * T[i][1] + T[i-2][0] * T[i-2][1] * T[i][1]:
            p[i][0], p[i][1] = T[i-2][0], T[i][1]
            f[i] = f[i-2] + T[i-1][0] * T[i-1][1] * T[i][1] + T[i-2][0] * T[i-2][1] * T[i][1]

    return f[n-1]

# Example
T = [[40, 20], [20, 30], [30, 10], [10, 30] ]
print(f"Minimal cost: {min_cost_matrix(T)}")