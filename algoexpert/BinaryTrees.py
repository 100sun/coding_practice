# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(N) time | O(logN-N) space
def branchSums(root):
    if not root.left and not root.right: return [root.value]
    return traverseBranch(root, 0, [])


def traverseBranch(node, runningSum, branchSums):
    if node is None: return
    runningSum += node.value
    if not node.left and not node.right:
        branchSums.append(runningSum)
        return
    traverseBranch(node.left, runningSum, branchSums)
    traverseBranch(node.right, runningSum, branchSums)
    return branchSums


def findSuccessor(tree, node):
    inOrderTraversalOrder = getInOrderTraversalOrder(tree)
    for idx, currentNode in enumerate(inOrderTraversalOrder):
        if currentNode != node:
            continue
        if idx == len(inOrderTraversalOrder) - 1:
            return None
        return inOrderTraversalOrder[idx + 1]


def getInOrderTraversalOrder(node, order=[]):
    print(f"node={node}, order={order}")
    if node is None:
        return order

    getInOrderTraversalOrder(node.left, order)
    order.append(node)
    getInOrderTraversalOrder(node.right, order)

    return order

