# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val, self.left, self.right}"


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def sortedArrayToBST(self, num):
        if not num: return None
        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid + 1:])

        return root

    def inOrder(self, root, output):
        if root is None: return
        self.inOrder(root.left)
        self.res.append(root.val)
        self.inOrder(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.res = list()
        self.inOrder(root)
        return self.res == sorted(self.res) and len(set(self.res)) == len(self.res)

    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
            # level = []
            # for n in level:
            #     for kid in (n.left, n.right):
            #         if kid is not None:
            #             level.append(kid)
        return ans

    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node: return 0
            val = dfs(node.left) + dfs(node.right)


if __name__ == '__main__':
    test = Solution()
    # print(test.twoSum(nums=[3, 3], target=6))
    # print(test.threeSum(nums=[-5, 0, -2, 3, -2, 1, 1, 3, 0, -5, 3, 3, 0, -1]))
    t = TreeNode([2, 2, 2])
    t = TreeNode([0, -1])
    print(test.isValidBST(t))
