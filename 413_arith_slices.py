class Solution(object):
 
    def lookupFunc(self, n):
        if n not in self.lookup:
            self.lookup[n] = -self.lookupFunc(n-2) + 2*self.lookupFunc(n-1) + 1
        return self.lookup[n]
            
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.lookup = {3:1, 4:3}
        slices, accumLen, accumDiff = 0, 0, None
        
        for idx in range(1, len(A)):
            curDiff = A[idx]-A[idx-1]
            if curDiff == accumDiff:
                accumLen += 1
            else:
                if accumLen >= 3:
                    slices += self.lookupFunc(accumLen)
                accumLen = 2
                accumDiff = curDiff
        if accumLen >= 3:
            slices += self.lookupFunc(accumLen)
        return slices
        