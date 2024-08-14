class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        c , q = {0:-1}, 0
        for i , v in enumerate(nums):
            q+= v -0.5
            res = max(res, i - c.setdefault(q, i))
        
        return res
        