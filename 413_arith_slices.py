class Solution(object):
 
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        slices, accumLen, accumDiff = 0, 0, None
        for idx in range(1, len(A)):
            curDiff = A[idx]-A[idx-1]
            if curDiff == accumDiff:
                accumLen += 1
                slices += accumLen
            else:
                accumLen = 0
                accumDiff = curDiff
        return slices
        