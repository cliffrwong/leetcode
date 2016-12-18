class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        maxArea = 0
        stack = []
        for idx, height in enumerate(heights):
            if not stack:
                stack.append((height, height))
                maxArea = height
                continue
            maxWidth = 0
            while stack:
                (xHeight, xArea) = stack.pop()
                if xHeight > height:
                    maxArea = xArea if xArea > maxArea else maxArea
                    width = xArea/xHeight
                    maxWidth = width if width > maxWidth else maxWidth
                else:
                    stack.append((xHeight, xArea))
                    break
            stack = [(xHeight, xArea+xHeight) for (xHeight, xArea) in stack]
            if not stack or (stack and height > stack[-1][0]):
                stack.append((height, height*(maxWidth+1)))
        maxArea = max(max(stack,key=lambda item:item[1])[1], maxArea)
        return maxArea