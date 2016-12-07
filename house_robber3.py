# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max = 0
        self.treeDFS(root)
        return self.max
    
    def treeDFS(self, node):
        accGrdLeft, accLeft = self.treeDFS(node.left) if node.left else (0, 0)
        accGrdRight, accRight = self.treeDFS(node.right) if node.right else (0, 0)
        accum = max([accGrdLeft+accGrdRight+node.val, accLeft+accRight, \
                    accGrdRight+accLeft, accGrdLeft+accRight])
        if accum > self.max:
            self.max = accum
        return (accLeft + accRight, accum)

