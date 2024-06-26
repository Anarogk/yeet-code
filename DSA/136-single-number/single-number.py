class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for x in nums:
            out ^= x
        return out
