from collections import deque

class HitCounter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitDeque = deque()
        self.accumHits = 0
    
    def updateDeque(self, timestamp):
        while self.hitDeque and timestamp - self.hitDeque[0][0] >= 300:
            self.accumHits -= self.hitDeque[0][1]
            self.hitDeque.popleft()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.hitDeque or self.hitDeque[-1][0] != timestamp:
            self.hitDeque.append([timestamp, 1])
        else:
            self.hitDeque[-1][1] += 1
        self.accumHits += 1
        self.updateDeque(timestamp)   
            
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.updateDeque(timestamp)
        return self.accumHits
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)