from collections import defaultdict  # KEY_ERROR -> default value
from collections import deque

from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def __str__(self):
        return f"{self.graph}"

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)  # Mark the current node as visited
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):  # DFS traversal
        visited = set()
        self.DFSUtil(v, visited)

    def BFS(self, s):
        print(self.graph, max(self.graph))
        visited = [False] * (max(self.graph) + 1)
        queue = deque(s)

        queue.append(s)  # source node
        visited[s] = True

        while queue:
            s = queue.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # graph_list = {1: set([3, 4]),
    #               2: set([3, 4, 5]),
    #               3: set([1, 5]),
    #               4: set([1]),
    #               5: set([2, 6]),
    #               6: set([3, 5])}
    # root_node = 1

    def BFS_with_adj_list(graph, root):
        visited = []
        from collections import deque
        queue = deque([root])

        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                queue += graph[n] - set(visited)
        return visited


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        row, col = len(grid), len(grid[0])
        visited = set()
        from collections import deque
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def is_valid(node):
            return 0 <= node[0] < row and 0 <= node[1] < col and node not in visited and grid[node[0]][node[1]] == '1'

        def bfs(start):
            queue = deque([start])
            while queue:
                cur_node = queue.popleft()
                # print(f"{cur_node} was poplefted")
                for Dir in dirs:
                    new_node = (cur_node[0] + Dir[0], cur_node[1] + Dir[1])
                    if is_valid(new_node):
                        visited.add(new_node)
                        queue.append(new_node)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs((r, c))
                    ans += 1
        return ans


if __name__ == '__main__':
    # g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    # print(g)
    # print("\nFollowing is DFS from (starting from vertex 2)")
    # g.DFS(2)
    # print("\nFollowing is BFS from (starting from vertex 2)")
    # g.BFS(2)

    test = Solution()
    # print(test.numIslands(grid=[
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]), 1)
    # print("=======================")
    # print(test.numIslands(grid=[
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]), 3)
