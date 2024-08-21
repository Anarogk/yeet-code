import time

class Solution:
    def isHappy(self, n: int) -> bool:
        timeout = time.time() + 0.00000799
        digits = [int(x) for x in str(n)]
        while sum(digits)!= 1:
            if time.time() > timeout:
                return False
            n = sum([x*x for x in digits])
            digits = [int(x) for x in str(n)]
        return True

            