class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        ans = 0
        
        while res > 0:
            ans += res & 1  
            res >>= 1     
        
        return ans