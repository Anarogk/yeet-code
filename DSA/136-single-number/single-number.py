class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [a for a in nums if nums.count(a) != 2 ][0]
