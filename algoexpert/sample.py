# Time O(N) Space O(1) (pointer)
def isValidSubsequence(array, sequence):
    pointer = 0
    for num in array:
        if sequence[pointer] == num:
            pointer += 1
    return pointer == len(sequence)

# Time O(W*H) == O(N) Space  O(W*H) == O(N) (visited)
def visitAdjacent(matrix, visited, n, m, size):
    li = [[n - 1, m], [n + 1, m], [n, m - 1], [n, m + 1]]
    for tmp_n, tmp_m in li:
        if tmp_n >= 0 and tmp_m >= 0:
            visited[tmp_n][tmp_m] = 1
            if matrix[tmp_n][tmp_m]:
                print(size, tmp_n, tmp_m, matrix[tmp_n][tmp_m])
                size += 1
                visitAdjacent(matrix, visited, tmp_n, tmp_m, size)
    return visited, size


def riverSizes(matrix):
    sizes = []
    visited = [[False] * len(matrix[0])] * len(matrix)
    # while (!all(all(row) for row in visited)):
    # for n, li in enumerate(matrix):
    #     for m, num in enumerate(li):
    #         if not visited[n][m]:
    #             visited, size = visitAdjacent(matrix, visited, n, m, 0)
    #             sizes.append(size)
    return sorted(sizes)


if __name__ == '__main__':
    test = {
        "array": [5, 1, 22, 25, 6, -1, 8, 10],
        "sequence": [1, 6, -1, 10]
    }
    isValidSubsequence(test["array"], test["sequence"])
    print(riverSizes([
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]))
