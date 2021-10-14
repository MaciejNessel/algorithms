# Insertion Sort
# Benefits:
#    a. efficient for pre-sorted data
#    b. efficient for small collections
#    c. sorting in place
#    d. stable sort
# Time Complexity: O(n^2)

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j > -1 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


# Example:
T = [2, 0, 1000, 11, 23, 7, 255, 2, 4, 5, 111, 1, 1111111111111, 0]
insertion_sort(T)
print(T)
