# 완전탐색: 순열조합 / BFS / 백트랙킹

def check_answer(answers):  # 모의고사
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    checks = [0] * len(students)
    for answer_cnt, answer in enumerate(answers):
        for stu_cnt, student in enumerate(students):
            if answer == student[answer_cnt % len(student)]:
                checks[stu_cnt] += 1
    return [check + 1 for check_cnt, check in enumerate(checks) if check == max(checks)]


from itertools import permutations


def check_prime_numbers(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


def find_prime_nums_mine(numbers):  # 소수찾기
    answer = 0
    for i in range(1, len(numbers) + 1):
        for j in set(map(int, (map("".join, permutations(list(numbers), i))))):
            if check_prime_numbers(j) and len(list(str(j))) == i:
                answer += 1
    return answer


from itertools import permutations


def find_prime_nums_mine_solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))  # omit 0, 1 ( not prime nums )
    # print(f"{a} : 2 ~ {int(max(a) ** 0.5 + 1)}")
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
        # print(f"{i}: -= ({i * 2}, {max(a) + 1}, {i}) => {a}")
    return len(a)


def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return sorted(divisors)[0:len(divisors) // 2 + 1]


def tile_solution(brown, yellow):
    for x in get_divisors(brown + yellow):
        y = (brown + yellow) // x
        # print(x, y)
        if x * 2 + y * 2 - 4 == brown:
            return [x, y] if x >= y else [y, x]
    return []


def solution(brown, yellow):
    print(int(yellow ** 0.5) + 1)
    for i in range(1, int(yellow ** 0.5) + 1):
        print(i, end=" ")
        if yellow % i == 0:
            if 2 * (i + yellow // i) == brown - 4:  # 세로 == 가로
                return [yellow // i + 2, i + 2]


inputs = [(10, 2), (8, 1), (24, 24)]
for input in inputs:
    print(f"\n{input}->{solution(input[0], input[1])}")
