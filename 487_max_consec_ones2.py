# LeetCode 487. Max Consecutive Ones II

# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# Example 1:

# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.

[1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1]

maxOnes = 6
consOnesFlip = 1
consOnes = 0

class Solutions:
    
    def maxConsOnes(self, nums):
        maxOnes = 0
        consOnes = 0
        consOnesFlip = 0

        for item in nums:
            if item == 1:
                consOnes += 1
                consOnesFlip += 1
            else:
                if consOnesFlip > maxOnes:
                    maxOnes = consOnesFlip
                consOnesFlip = consOnes + 1 
                consOnes = 0
        return max(maxOnes, consOnesFlip)


