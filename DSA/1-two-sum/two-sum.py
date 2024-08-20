class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {nums[0]:0} # add first item to map with index
        for i, num in enumerate(nums):
            if target - num in mapp.keys() and i not in mapp.values():
                return [mapp.get(target -num), i]
            mapp[num] = i
        return []
    
                
            