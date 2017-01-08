class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        x = [0]*(len(s)+1)
        x[0] = 1
        for i in range(len(s)):
            if s[i] == '0':
                if s[i-1] == '0':
                    return 0
                else:
                    continue
            x[i+1] = x[i] + x[i+1]
            if i < len(s)-1:
                if int(s[i:i+2]) <= 26:
                    x[i+2] = x[i] + x[i+2]
        return x[-1]
                