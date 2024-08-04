class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            l = ord(s[i])
            m = ord(s[i+1])
            sum += abs(l-m)
        return sum