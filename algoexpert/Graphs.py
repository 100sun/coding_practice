class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) time | O(v) space # vertex, edges
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


# O(n) time | O(1) space
def hasSingleCycle(array):
    nElemsVisited = 0
    curIdx = 0
    while nElemsVisited < len(array):
        if nElemsVisited > 0 and curIdx == 0:
            return False
        nElemsVisited += 1
        curIdx = (len(array) + array[curIdx] + curIdx) % len(array)
    return curIdx == 0


# O(wh) time | O(wh) space
def riverSizes(matrix):
    sizes = []
    visited = [[False for val in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j]:
                traverseNode(i, j, matrix, visited, sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    curSize = 0
    needsToExplore = [[i, j]]  # queue
    while needsToExplore:
        curNode = needsToExplore.pop()
        i, j = curNode[0], curNode[1]
        if visited[i][j]: continue
        visited[i][j] = True  # regardless of 0 || 1
        if matrix[i][j] == 0: continue  # no need for size
        curSize += 1
        needsToExplore.extend(getUnvisitedNeighbors(i, j, matrix, visited))
    if curSize > 0:
        sizes.append(curSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]: unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]: unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]: unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[i]) - 1 and not visited[i][j + 1]: unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors



