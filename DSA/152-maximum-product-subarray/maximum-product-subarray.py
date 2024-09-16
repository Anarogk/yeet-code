class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]  # first item
        curMin, curMax = 1, 1  # maintain min and max prod

        for n in nums:

            tmp = curMax * n # currMax * curr
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res