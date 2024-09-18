class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        result = 0
        left = 0
        for right, num in enumerate(nums):
            product *= num  # consider num in prod
            while product >= k:  # validate
                product /= nums[left]
                left += 1
            result += right - left + 1
        return result