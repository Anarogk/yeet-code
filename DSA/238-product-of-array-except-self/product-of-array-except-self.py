class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)  # [1, 1, 1, 1, 1..]
        # for i in range(1, len(nums)):
        #     res[i] = res[i - 1] * nums[i - 1]  # [num[0], nums[1], nums[j]]
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res

        n = len(nums)

        prefix = [1] * n  # len(nums)
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer