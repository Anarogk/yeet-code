class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i , j = 0, len(nums)-1
        count = 0
        if val not in nums:
            return len(nums)
        while(i<j):
            if nums[i] == val:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                elif nums[j] == val:
                    j-=1
            else:
                i+=1
        return  i 