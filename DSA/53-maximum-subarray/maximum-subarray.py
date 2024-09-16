class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total = 0

        for n in nums:
            total += n
            max_sum = max(max_sum, total)
            if total < 0:
                total = 0
        return max_sum