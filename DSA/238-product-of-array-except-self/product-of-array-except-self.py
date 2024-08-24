class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # prefix = 1
        # postfix = 1
        # result = [0] *n
        # for i in range(n):
        #     result[i] = prefix
        #     prefix *=nums[i]
        # for i in range(n-1,-1,-1):
        #     result[i]*=postfix
        #     postfix*=nums[i]
        # return result


        nums1 = [1 for i in nums]
        nums2 = [1 for i in nums]
        
        for i in range(1,len(nums)):
            nums1[i] = nums1[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            nums2[i] = nums2[i+1] * nums[i+1]
        
        # print(nums1,nums2)
        nums3 = [i[0]*i[1] for i in zip(nums1,nums2)]
        return nums3            