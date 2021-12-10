class Graph(object):
    def __init__(self):
        self.graph = {}
        self.color = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)

    def set_color(self, u, color):
        self.color[u] = color

    def bfs(self, node):
        distance = 0
        color = self.color[node]
        visited = [0] * (len(self.graph) + 1)

        from collections import deque
        queue = deque([node])
        visited[node] = 1

        while queue:
            node = queue.popleft()
            distance += 1
            for t in self.graph[node]:
                if not visited[t]:
                    if self.color[t] == color:
                        return distance
                    queue.append(t)
                    visited[t] = 1
        return 10 ** 6

    def print(self):
        print("graph: ", self.graph)
        print("color: ", self.color)


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    print(graph_nodes, graph_from, graph_to, ids, val, sep=',')
    graph = Graph()
    for u, v in zip(graph_from, graph_to):
        graph.add_edge(u, v)
        graph.add_edge(v, u)
    for node in range(1, len(ids) + 1):
        graph.set_color(node, ids[node - 1])

    graph.print()

    min_distance = 10 ** 6

    for node in range(1, graph_nodes + 1):
        if graph.color[node] == val:
            min_distance = min(min_distance, graph.bfs(node))

    if min_distance == 10 ** 6:
        return -1
    return min_distance


findShortest(5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2)
