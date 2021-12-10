def dfs_solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1 * numbers[0], 0]]  # [[1, 0], [-1, 0]]
    while stack:
        temp, idx = stack.pop()
        idx += 1
        if idx < len(numbers):
            print([x[0] for x in stack], numbers[idx])
            stack.append([temp + numbers[idx], idx])
            stack.append([temp - numbers[idx], idx])
        else:  # if temp is the last index
            if temp == target:  # if temp is as same as target
                print("!!!!", idx, temp)
                answer += 1
    return answer


MAX_P = 200000


def catching_game(subin_p, bro_p):
    from collections import deque
    time = [0] * MAX_P
    q = deque()
    q.append(subin_p)
    while q:
        v = q.popleft()
        print(f"v={v}, q={q}, time={time[0:30]}")
        if v == bro_p:
            return time[v]
        for next_step in (v - 1, v + 1, v * 2):
            if 0 <= next_step < MAX_P and not time[next_step]:  # 범위 이내이고 방문하지 않았다
                time[next_step] = time[v] + 1
                q.append(next_step)


def catching_game_line(cony_p, brown_p):
    from collections import deque
    t = 0
    brown_visited_at = [[False] * 2 for _ in range(MAX_P + 1)]  # (visited_pos, visited_time)
    where_brown_can_visit = deque()
    where_brown_can_visit.append((brown_p, t))  # (pos, time)
    # 초 계속 증가
    while 1:
        cony_p += t
        if cony_p > MAX_P:
            return -1
        if brown_visited_at[cony_p][t % 2]:
            # print(brown_visited_at[cony_p], t, t % 2, brown_visited_at[:26])
            return t
        # print("========\nq:", list(where_brown_can_visit)[:len(where_brown_can_visit)])
        # q안에 있는 모든 경우의 수 돌기
        for _ in range(0, len(where_brown_can_visit)):
            brown_cur = where_brown_can_visit.popleft()
            brown_cur_p = brown_cur[0]
            from operator import not_
            new_t = not_(brown_cur[1])  # (brown_cur[1] + 1) % 2
            # brown이 갈 수 있는 경우의 수들 중 방문하지 않은 곳 (visited[position][time] 이 0인것) 모두 q에 넣어주기
            for new_p in (brown_cur_p - 1, brown_cur_p + 1, brown_cur_p * 2):
                if 0 <= new_p <= MAX_P and not brown_visited_at[new_p][new_t]:
                    brown_visited_at[new_p][new_t] = True
                    where_brown_can_visit.append((new_p, new_t))
        t += 1


def main():
    # print(catching_game(5, 17), 4)
    print(catching_game_line(11, 2), 5)


# print(dfs_solution([1, 1, 1, 1, 1], 3), 5)
# print(dfs_solution([1, 2, 1, 2], 2), 3)
# print(dfs_solution([1, 2, 1, 2], 6), 1)


if __name__ == '__main__':
    main()
