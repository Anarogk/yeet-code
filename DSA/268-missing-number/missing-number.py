class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            print(i)
            if i in nums:
                continue
            else:
                return i
        return 0