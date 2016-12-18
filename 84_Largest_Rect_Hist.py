class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []
        for idx, height in enumerate(heights):
            if not stack:
                stack.append((height, 0))
                maxArea = height
                continue
            maxWidth = 0
            while stack:
                (xHeight, xIdx) = stack.pop()
                if xHeight > height:
                    width = idx-xIdx
                    xArea = xHeight*width
                    maxArea = xArea if xArea > maxArea else maxArea
                    maxWidth = width if width > maxWidth else maxWidth
                else:
                    stack.append((xHeight, xIdx))
                    break
            if not stack or height > stack[-1][0]:
                stack.append((height, idx-maxWidth))
        maxArea = max([(len(heights)-xIdx)*xHeight for (xHeight, xIdx) in stack] + [maxArea])
        return maxArea