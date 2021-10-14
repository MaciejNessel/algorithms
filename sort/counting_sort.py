# Counting Sort
# This is implementation for natural numbers
# Time Complexity: O(len(arr) + max_val)

def counting_sort(array, max_val):
    counter = [0] * max_val
    help_arr = [0] * len(array)

    for x in array:
        counter[x] += 1

    for i in range(1, max_val):
        counter[i] += counter[i-1]

    for i in range(len(array) - 1, -1, -1):
        counter[array[i]] -= 1
        help_arr[counter[array[i]]] = array[i]

    for i in range(len(array)):
        array[i] = help_arr[i]


# Example:
data = [40, 2, 2, 8, 3, 3, 1]
max_val = max(data) + 1
counting_sort(data, max_val)
print(f"Sorted: {data}")
