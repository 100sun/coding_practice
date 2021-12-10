1. codeup 기초 100제로 기초를 다지고 사용할 언어에 익숙해지도록 한다.
2. 백준온라인 저지 단계별, 유형별 문제를 푼다. 배열, 문자열, 정렬, 브루트포스(완전탐색), 재귀, 백트래킹, 동적계획법, bfs/dfs 등의 유형에 익숙해진다.
    - 완전탐색(재귀나 백트래킹으로)-> 시뮬레이션->그래프(위상정렬, 다익스트라..)->최소신장유니온트리(유니온파인드 등)->심화문제(스택으로 라인스위핑 같은)->DP, dp는 코딩테스트에 나오면 완죠니 어렵게
      나온다고 한다.
3. 프로그래머스 코딩테스트 고득점 kit를 푼다.: 유형별 4~7문제를 풀며 자주 나오는 유형을 익힌다.
4. 프로그래머스 스킬체크 : 주어진 시간내에 2문제를 풀고, 나의 실력을 파악한다. 레벨3정도면 웬만한 코딩테스트에 합격할 수 있다고 한다.

# DP, DC

* 모두 문제를 쪼개 가장 작은 단위로 분할
* DP: 상향식, Memorization 기법 (O) - 가장 최하위 먼저, 부분 문제는 중복 -> 재활용 ex. 피보나치 수열
* DC: 하향식, Memorization 기법 (X) - 가장 최상위 먼저, 재귀함수 알반적 ex. 병합정렬, 퀵정렬

## Dynamic Programming

```python
dp = [0, 1, 2, 4]
for _ in range(4, 14):
    dp.append(sum(dp[-3:]))
for _ in range(int(input())):
    print(dp[int(input())])

```

# DFS, BFS

* 모두 경로 탐색에 사용
* BFS: 최단 보장, 메모리 많이 씀
* DFS: back-tracking

```python
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
```

* 재귀로 풀 경우

```python
import sys

sys.setrecursionlimit(100000)
```

## Breadth First Search

deque

```python
from collections import deque

q = deque()  # []
qq = deque([1])


# 인접한 노드 중 방문하지 않았던 노드만 큐에 넣어서 방문하기
def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


print(BFS_with_adj_list(graph_list, root_node))
```

## Depth First Search

python's list := stack just use list

끝까지 간 뒤에 이전 갈림길로 돌아오기

```python
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited
```