class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        max_sum = curr
        for i in range(k, len(nums)):
            curr = curr - nums[i-k] + nums[i]
            max_sum= max(curr, max_sum)
        return max_sum/k

