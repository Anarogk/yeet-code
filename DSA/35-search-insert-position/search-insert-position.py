class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        if target < nums[0]:
            return 0
        while lo<= hi:
            mid = lo + ((hi-lo) //2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            elif nums[mid] < target:
                lo = mid+1 
        return lo