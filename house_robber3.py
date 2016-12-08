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
        return self.treeDFS(root)[1]
        
    def treeDFS(self, node):
        if not node:
            return (0,0)
        accGrdLeft, accLeft = self.treeDFS(node.left)
        accGrdRight, accRight = self.treeDFS(node.right)
        accum = max([accGrdLeft+accGrdRight+node.val, accLeft+accRight])
        return (accLeft+accRight, accum)