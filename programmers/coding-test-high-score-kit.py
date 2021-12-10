# 정렬

## K번째 수 찾기

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# answer = [sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1] for cmd in commands]
answer = list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))

## 가장 큰 수

from itertools import permutations

numbers = [0, 0, 0, 0, 0]
# answer = max([''.join(i) for i in list(permutations([str(num) for num in numbers], len(numbers)))])
str_numbers = list(map(str, numbers))
str_numbers.sort(key=lambda x: x * 3, reverse=True)
answer = str(int(''.join(str_numbers)))

## H-Index

citations = [3, 0, 6, 1, 5]
citations = [1, 2, 4, 5]
# citations = [22, 42]
answer = sorted(citations)[len(citations) // 2]
print(answer, type(answer))
