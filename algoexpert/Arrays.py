# O(n) time, O(1) space
def isValidSubsequence(array, sequence):
    pointer = 0
    for num in array:
        if pointer == len(sequence):
            break
    if sequence[pointer] == num:
        pointer += 1
    return pointer == len(sequence)
