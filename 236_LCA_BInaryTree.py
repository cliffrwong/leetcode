# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def findLowest(self, node):
        if node == None:
            return False
        curBool = False
        if node.val in self.pq:
            self.found += 1
            curBool = True
        if self.found == 2:
            return True
        
        leftRes = self.findLowest(node.left)
        if leftRes and curBool:
            self.result = node
        if self.result:
            return True
        
        rightRes = self.findLowest(node.right)
        if (leftRes and rightRes) or (rightRes and curBool):
            self.result = node
        if self.result:
            return True
        
        return leftRes or rightRes or curBool
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.pq = [p, q]
        self.found = 0
        self.result = None
        self.findLowest(root)
        return self.result

a = TreeNode(2)
b = TreeNode(1)
a.left = b

sol = Solution()
result = sol.lowestCommonAncestor(a, 1, 2)

assert result.val == 2

        