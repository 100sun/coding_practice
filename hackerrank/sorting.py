from random import randint
from timeit import repeat

ARRAY_LENGTH = 10000


# avg : O(n2)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False

        if already_sorted:
            break

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item
    return array


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def count_sort(arr):
    new_arr = []
    # print(max(arr), arr)
    count = [0] * (max(arr) + 1)
    # print(count)
    for i in arr:
        count[i] += 1
    # print(count)
    for i in range(len(count)):
        # count[i] will be 0 or 1
        for j in range(count[i]):
            # print(f"i:{i}, j:{j}, count[i]:{count[i]}")
            new_arr.append(i)
    return new_arr


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    arr = [4, 7, 2, 8]
    print("\n", count_sort(arr))

    # array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    # run_sorting_algorithm(algorithm="bubble_sort", array=array)
    # run_sorting_algorithm(algorithm="insertion_sort", array=array)
