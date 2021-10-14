# Longest common subsequence two array
# Time complexity: O(n^2)

def longest_common_subsequence(a, b):
    n = len(a)
    f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    return f[n][n]

# Example:
a1 = [1,14,2,8,9,10]
a2 = [1,2,3,10,5,4]
print(longest_common_subsequence(a1, a2))
