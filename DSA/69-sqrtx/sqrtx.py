class Solution:
    def mySqrt(self, x: int) -> int:
        high = x
        low = 0
        while high >= low:
            l= ((high +low )//2)
            if l * l < x:
                low = l + 1
            elif l *l > x:
                high = l -1
            else:
                return l
            
        return high