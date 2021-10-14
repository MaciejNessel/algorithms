# Coverage by unit intervals
# A set of points is given: X = {x1,. . . , xn}
# Find the minimum number of closed unit intervals, needed to cover all points with X.
# Example: If X = {0.25, 0.5, 1.6} then you need two intervals, e.g. [0.2, 1.2] and [1.4, 2.4]).



def find_intervals(x):
    n = len(x)
    x.sort()
    result = [(x[0], x[0] + 1)]
    high = x[0] + 1
    cnt = 1
    for i in range(1, n):
        if x[i] <= high:
            continue
        else:
            result.append((x[i], x[i] + 1))
            high = x[i] + 1
            cnt += 1

    return cnt, result

# Example:
X = [0.25,0.5,1.6,2.6,2.7,3.0,3.5,3.6]
counter, intervals = find_intervals(X)
print("Result: ", counter, "Intervals: ", intervals)



