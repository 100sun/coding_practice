import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        print(repr(self))
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


#   inputs = [[2, 10, [7, 4, 5, 6]],  # 8
#               [100, 100, [10]],  # 101
#               [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]]  # 110
#     for input in inputs:
#         print(f"=============\n{trucks_on_bridge_solution(input[0], input[1], input[2])}")
def trucks_on_bridge_solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    # initialization as much as bridge_length
    for i in range(bridge_length):
        bridge.push(DUMMY_TRUCK)
    # Bridge(0/max_weight : [[0, 0]])

    count = 0
    while trucks:
        # print(f"time:{count}")

        bridge.pop()

        if bridge.push(trucks[0]):  # appended
            trucks.popleft()
        else:  # is full
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        # print(f"ttime:{count}", end=", ")
        bridge.pop()
        count += 1

    return count


def q_solution(priorities, location):
    from collections import deque
    waiting_q = deque([i for i in range(len(priorities))])
    printed_q = deque()
    while waiting_q:
        max_v = max(list(map(lambda p: priorities[p], waiting_q)))
        now = waiting_q.popleft()
        if priorities[now] == max_v:
            printed_q.append(now)
        else:
            waiting_q.append(now)
    return printed_q.index(location) + 1


def solution_h(inputString):
    pair = 0
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    map = dict(zip(open_tup, close_tup))
    from collections import deque
    queue = deque()
    for idx, char in enumerate(inputString):
        if char in open_tup:
            queue.append(map[char])
        elif char in close_tup:

            tmp = queue.pop()

            if not queue or char != tmp:
                return -idx
    if not queue:
        # import re
        # return len(re.findall(r'\[({<.*?})>]\]', inputString))
        return pair
    else:
        return -idx


def solution1(inputString):
    pair = 0
    open_list = ['(', '[', '{', '<']
    close_list = [')', ']', '}', '>']
    stack = []
    for idx, char in enumerate(inputString):
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            pos = close_list.index(char)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                pair += 1
            else:
                return -idx
    if len(stack) == 0:
        return pair
    else:
        return -idx


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def solution(array):
    ts = sorted(array)
    answer = [0] * len(array)
    for idx, num in enumerate(array):
        greater = ts[ts.index(num) + 1:]
        if not greater:
            print(num, greater, -1)
            answer[idx] = -1
        else:
            answers = list()
            min_abs = min((list(map(lambda x: abs(idx - array.index(x)), greater))))
            min_idxs = [answers.extend(duplicates(array, i)) for i in greater if abs(idx - array.index(i)) == min_abs]
            print(num, greater, min_abs, min_idxs, answers)
            answer[idx] = min(answers)

    return answer


# Python 3 implementation of simple
# algorithm to find smaller element
# on left side

# Prints smaller elements on left
# side of every element
# def printPrevSmaller(arr):
#     # Create an empty stack
#     S = list()
#     n = len(arr)
#
#     # Traverse all array elements
#     for i in range(n):
#
#         # Keep removing top element from S
#         # while the top element is greater
#         # than or equal to arr[i]
#         while (len(S) > 0 and S[1] <= arr[i]):
#             S.pop()
#
#         # If all elements in S were greater
#         # than arr[i]
#         if (len(S) == 0):
#             print("_, ", end="")
#         else:  # Else print the nearest
#             # smaller element
#             print(S[1], end=", ")
#
#         # Push this element
#

# This code is contributed by
# Smitha

print(solution([7, 4, 4, 2, 9, 6]), [4, 0, 0, 2, -1, 4])
# print(solution("ABC({ABC)ABC"))
# print(solution(")a"))
# print(solution("a"))
# print(solution("ABC)ABC"))
#
# def solution(inputString):
#     pair = 0
#     idx = 0
#     open_tup = tuple('({[<')
#     close_tup = tuple(')}]>')
#     openn = dict()
#     close = dict()
#     cnt = 0
#
#     map = dict(zip(open_tup, close_tup))
#     from collections import deque
#     queue = deque()
#     op, cl = 0, 0
#     for idx, char in enumerate(inputString):
#         if char in open_tup:
#             queue.append(map[char])
#             op += 1
#         elif char in close_tup:
#             if not queue or char != queue.pop():
#                 return -idx
#             if op:
#                 op -= 1
#             else:
#                 cl += 1
#
#     if op and cl == 0:
#         if op in openn.keys():
#             openn[op] += 1
#         else:
#             openn[op] = 1
#
#     if cl and op == 0:
#         if cl in openn.keys():
#             close[cl] += 1
#         else:
#             close[cl] = 1
#
#
#     if (op == 0 and cl == 0):
#         cnt += 1
#
#     cnt = cnt //2
#     for it in openn:
#         cnt += min(openn[it], close[it])
#
#     return cnt
#     if not queue:
#         return "Balanced"
#     else:
#         return -idx

#
# def main():
#     inputs = [[[2, 1, 3, 2], 2],  # 1
#               [[1, 1, 9, 1, 1, 1], 0]]  # 5
#     for input in inputs:
#         print(f"=============\n{solution(input[0], input[1])}")
#
#
# if __name__ == '__main__':
#     main()


# 문제 설명
# "Sofia"은 유저에게 어떤 순서로 광고를 노출할지 고민하고 있습니다.
#
# 광고는 각각 [노출할 수 있는 시작 시간, 대기 시간당 손해 비용]으로 구성됩니다. 한 번에 하나의 광고만 노출할 수 있고, 특정 시점에 노출할 수 있는 광고가 하나 이상 존재하면 반드시 노출해야 합니다. 또한 노출하기 시작한 광고는 노출 시간이 끝날 때까지 중단할 수 없으며, 모든 광고는 정확히 5s의 시간 동안 노출합니다.
#
# 예를 들어, [A: 1s 시점부터 노출할 수 있는 광고, B: 3s 시점부터 노출할 수 있는 광고, C: 5s 시점부터 노출할 수 있는 광고]와 같은 광고들이 있다고 가정해 보겠습니다.
#
# 한 번에 하나의 광고만 노출할 수 있고 노출하기 시작한 광고는 중단할 수 없기 때문에 광고를 노출할 수 있는 시작 시간 순서대로 처리하면 다음과 같습니다.
#
# 광고 A는 0s, B는 3s, C는 6s의 대기 시간이 발생하며, 광고 A, B, C의 대기 시간당 손해 비용이 각각 2, 1, 3일 경우 총 손해 비용은 (0 * 2) + (3 * 1) + (6 * 3) = 21이 됩니다. 이를 시간대 별로 확인하면 다음과 같습니다.
#
# 시간	노출될 수 있는 광고	손해비용	총 손해비용
# 0	-	0	0
# 1	A	0	0
# 6	B, C	3 * 1 + 1 * 3 = 6	6
# 11	C	5 * 3 = 15	6 + 15 = 21
# 16	-	0	21
# "브라운"은 총 손해 비용이 최소가 되도록 광고를 처리하려고 합니다. [노출할 수 있는 시작 시간, 대기 시간당 손해 비용]으로 구성된 2차원 배열의 광고 리스트 ads를 입력받았을 때, 최소가 되는 총 손해 비용을 반환해 주세요.
#
# 제한 사항
# ads의 길이는 1 이상 5,000 이하입니다.
# ads는 광고 각각에 대해 [노출할 수 있는 시작 시간, 대기 시간당 손해 비용]을 담은 2차원 배열입니다.
# 각 광고를 노출할 수 있는 시작 시간은 0 이상 25,000 이하입니다.
# 대기 시간당 손해 비용은 1 이상 10 이하입니다.
# 모든 광고의 노출 시간은 5s 입니다.
# 입출력 예
# ads	return
# [[1, 3], [3, 2], [5, 4]]	20
# [[0, 3], [5, 4]]	0
# [[0, 1], [0, 2], [6, 3], [8, 4]]	40
# [[5, 2], [2, 2], [6, 3], [9, 2]]	33