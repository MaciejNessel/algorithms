# Heapsort
# Slower than Quicksort, but better pessimistic time complexity
# Time Complexity: O(n * logn),  n - len(array)
# Memory: O(n)

def heapify (array, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and array[l] > array[m]:
        m = l
    if r < n and array[r] > array[m]:
        m = r
    if m != i:
        array[i], array[m] = array[m], array[i]
        heapify(array, n, m)


def buildheap(array):
    n = len(array)
    for i in range(n-2//2, -1, -1):
        heapify(array, n, i)


def heapsort(array):
    buildheap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


def insert(array, el):
    array.append(el)
    n = len(array) - 1
    while n > 0 and array[(n - 1) // 2] < array[n]:
        array[(n - 1) // 2], array[n] = array[n], array[(n - 1) // 2]
        n = (n-1) // 2


# Example:
data = [20,10,12,30,432,123,2,21,2,1]
heapsort(data)
print(f"Sorted: {data}")