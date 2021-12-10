# O(n!*n*n) time | O(n!*n) space
# TIME n!(permuatations) * n(recursive call) * n(for loop)
# SPACE n!(permutations) * n(cur_permutation) <- no space for recusive call <- call stack
# pick and remove each index -> empty: append to the list
def getPermutations_usingRemoval(array):
    permutations = []  # O(n!) space
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(array, cur_permutation, permutations):
    if not len(array) and len(cur_permutation):  # all were removed in arr, and there is cur_perm
        # print(f"!! arr:{array}, cur_perm:{cur_permutation}")
        permutations.append(cur_permutation)  # O(n!) time
    else:
        for i in range(len(array)):
            new_arr = array[:i] + array[i + 1:]  # O(n) time, space : remove idx one by one
            new_permutation = cur_permutation + [array[i]]  # insert cur_val
            # print(f"{i}) arr: {array} new_arr:{new_arr}, cur_perm:{cur_permutation}, new_perm:{new_permutation}")
            permutationsHelper(new_arr, new_permutation,
                               permutations)  # O(n) time: until empty array -> all is append to cur_perm


# in place : swap -> back again => if last idx -> append
# TIME n! (permuatations)
# SPACE n! (permuatations) * n (len())
def getPermutations_usingSwap(array):
    permutations = []  # O(n!) space
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:  # O(n) space
        permutations.append(array[:])  # O(n!) time <- snapshot
        # a shallow copy of the array, hence allowing you to modify your copy without damaging the original.
    else:
        for j in range(i, len(array)):  # swap cur_idx w/ every all left elems
            swap(array, i, j)
            permutationsHelper(i + 1, array, permutations)  # O(n)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def random_sublist(L, N):
    from itertools import combinations
    print(list(combinations(L, N)))
    print(get_combinations_using_removal(L, N))


# O(n*n!) Time | O(n!*n)
def get_combinations_using_removal(lst, n):
    if n == 0:
        return [[]]
    my_combinations = []
    for i in range(len(lst)):  # O(n)
        cur_val = lst[i]
        new_arr = lst[i + 1:]
        for case in get_combinations_using_removal(new_arr, n - 1):  # O(n!)
            new_perm = [cur_val] + case
            my_combinations.append(new_perm)
    return my_combinations



random_sublist([1, 2, 3, 4, 5], 3)
