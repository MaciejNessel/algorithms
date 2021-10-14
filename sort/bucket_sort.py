# Bucket Sort
# Good for uniformly distributed data
# Time Complexity: O(n) for uniformly distributed data; O(n^2)

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


def bucket_sort(array):
    slot_num, max_num = len(array), max(array)
    buckets = [[] for _ in range(slot_num + 1)]

    for num in array:
        index_b = int(slot_num * (num / max_num))
        buckets[index_b].append(num)

    for bucket_num in range(slot_num):
        buckets[bucket_num] = insertion_sort(buckets[bucket_num])

    k = 0
    for bucket_num in range(slot_num):
        for num in range(len(buckets[bucket_num])):
            array[k] = buckets[bucket_num][num]
            k += 1

    return array



x = [0,0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.25, 0.77, 0.95, 0.01, 0.99, 0.7, 1.7]
bucket_sort(x)
print(f"Sorted: {x}")
