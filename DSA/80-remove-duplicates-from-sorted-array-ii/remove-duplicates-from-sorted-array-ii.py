class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s= defaultdict(int) 
        s[nums[0]] = 1
        idx = 0       

        for i in range(1, len(nums)):
            if s[nums[i]]<2:
                idx +=1
            nums[idx] = nums[i]
            s[nums[i]]+=1
        return idx+1