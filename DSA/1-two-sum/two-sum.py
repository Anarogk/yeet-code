class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {nums[0]:0}
        for i in range(1,len(nums)):
            if target - nums[i] in mapp.keys():
                return [mapp.get(target -nums[i]), i]
            mapp[nums[i]] = i
        return []
    
                
            