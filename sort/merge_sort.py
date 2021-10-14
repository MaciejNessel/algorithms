# Merge Sort
# Stable sort
# Time Complexity: O(n * logn),  n - len(array)

def mergesort(array):
    dl = len(array)
    if dl < 2:
        return array

    l, p = array[:dl // 2], array[dl // 2:]
    mergesort(l)
    mergesort(p)

    i = j = idx = 0
    while i < len(l) and j < len(p):
        if l[i] <= p[j]:
            array[idx] = l[i]
            i += 1
        else:
            array[idx] = p[j]
            j += 1
        idx += 1

    while i < len(l):
        array[idx] = l[i]
        i += 1
        idx += 1

    while j < len(p):
        array[idx] = p[j]
        j += 1
        idx += 1

    return array


# Example:
from random import randint
data = [randint(1, 10) for i in range(10)]
mergesort(data)
print(f"Sorted: {data}")

