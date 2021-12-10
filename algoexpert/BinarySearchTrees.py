# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# O(logN) - half of a tree O(N) - one length time | O(logN) space
def findClosestValueInBst(tree, target):
    visited = []
    from collections import deque
    nodesToVisit = deque([tree])
    closestVal = tree.value

    while nodesToVisit:
        node = nodesToVisit.popleft()
        if node.value in visited: continue
        if abs(node.value - target) < abs(closestVal - target): closestVal = node.value
        visited.append(node.value)
        if node.left: nodesToVisit.append(node.left)
        if node.right: nodesToVisit.append(node.right)

    return closestVal


# O(NlogN)-using .insert O(N)- if manually time | O(N) space
def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)


def constructMinHeightBst(array, bst, startIdx, endIdx):
    if endIdx < startIdx: return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array(midIdx)
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)  # logN
    constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)


# O(n) Time |
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))  # max negative infinity and postivie infinity


def validateBstHelper(tree, minValue, maxValue):
    if tree is None: return True
    if tree.value < minValue or tree.value >= maxValue: return False
    return validateBstHelper(tree.left, minValue, tree.value) and validateBst(tree.right, tree.value, maxValue)
