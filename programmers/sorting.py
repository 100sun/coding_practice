# H-index [[2, 2], [1545, 2, 999, 790, 540, 10, 22], [3, 0, 6, 1, 5], [1, 7, 0, 1, 6, 4], [0, 0, 0], [0], [7]]
def h_index_fastest(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        # print(f"{i} >= {citation}", end=" / ")
        if i >= citation:
            return i
    return len(citations)


def h_index_solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))


inputs = [[2, 2], [1545, 2, 999, 790, 540, 10, 22], [3, 0, 6, 1, 5], [1, 7, 0, 1, 6, 4], [0, 0, 0], [0], [7]]
for input in inputs:
    print(solution(input))
