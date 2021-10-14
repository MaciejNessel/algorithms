# QuickSort (partition Hoare):
def partition_hoare(array, low, high):
    pivot = array[low]
    (i, j) = (low - 1, high + 1)
    while True:
        while True:
            i = i + 1
            if array[i] >= pivot:
                break
        while True:
            j = j - 1
            if array[j] <= pivot:
                break
        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


def quicksort_hoare(array, low, high):
    if low >= high:
        return
    pivot = partition_hoare(array, low, high)
    quicksort_hoare(array, low, pivot)
    quicksort_hoare(array, pivot + 1, high)



# QuickSort (partition Lomuto)
def partition_lomuto(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i+1


def quicksort_lomuto(array, p, r):
    while p < r:
        q = partition_lomuto(array, p, r)
        if q - p < r - q:
            quicksort_lomuto(array, p, q - 1)
            p = q + 1
        else:
            quicksort_lomuto(array, q + 1, r)
            r = q - 1


# Quick Sort (iterative)
from queue import Queue

def quicksort_iterative(array):
    stack = Queue()
    stack.put((0, len(array) - 1))

    while stack.qsize() > 0:
        p, r = stack.get()
        if p < r:
            q = partition_lomuto(array, p, r)
            stack.put((p, q-1))
            stack.put((q+1, r))

    return array




# Examples:
from time import time
from random import randint, seed
seed(42)
n = 10000

print("Iterative:")
data = [randint(1, 100) for _ in range(n)]
start = time()
quicksort_iterative(data)
end = time()
print(f"Sorted: {data} \n time: {(end - start)} sec \n")

print("Horae:")
data = [randint(1, 100) for _ in range(n)]
start = time()
quicksort_hoare(data, 0, len(data) - 1)
end = time()
print(f"Sorted: {data} \n time: {(end - start)} sec \n")

print("Lomuto:")
data = [randint(1, 100) for _ in range(n)]
start = time()
quicksort_lomuto(data, 0, len(data) - 1)
end = time()
print(f"Sorted: {data} \n time: {(end - start)} sec")
