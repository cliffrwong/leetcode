from math import ceil, floor

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0,]
        accList = [[0],[1]]
        numBits = math.log(num+1,2)
        
        for i in range(2, int(ceil(numBits)+1)):
            list2 = accList[-1] + [x+1 for x in accList[-1]]
            if i <= numBits:
                accList.append(list2)
            else:
                accList.append(list2[:int(num+1-2**floor(numBits))])
        # Flatten list of lists
        return [item for sublist in accList for item in sublist]
            