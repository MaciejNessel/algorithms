# Bubble Sort
# The simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# Time Complexity: O(n^2)

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Example:
T = [10, 5, 2, 0, 11, 16, 5, 3, 1, 0]
bubble_sort(T)
print(T)
