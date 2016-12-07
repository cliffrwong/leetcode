# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.accum = 0
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
        maxLeftGChild, maxLeftChild, leftAccum = (self.treeDFS(node.left), \
                                        node.left.accum, node.left.accum) \
                                        if node.left else (0, 0, 0)
        maxRightGChild, maxRightChild, rightAccum = (self.treeDFS(node.right), \
                                        node.right.accum, node.right.accum) \
                                        if node.right else (0, 0, 0)
        
        node.accum = max([maxLeftGChild+maxRightGChild + node.val, \
                        maxLeftChild+maxRightChild, \
                        maxRightGChild+maxLeftChild, \
                        maxLeftGChild+maxRightChild])
        if node.accum > self.max:
            self.max = node.accum
            
        return leftAccum + rightAccum
        
        