class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):  # reverse
            for j in range(i + 1, len(nums)):  # sub of curr(i)-end
                if nums[i] < nums[j]:  # if curr(i) is less than jth
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)