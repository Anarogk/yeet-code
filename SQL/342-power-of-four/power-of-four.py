class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        arr= []
        for i in range(100):
            arr.append(4**i)
        if n in arr:
            return True
        return False