class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path): # backtrack func
            result.append(path) # appending path
            for i in range(start , len(nums)): # runing for len(nums)
                backtrack(i+1, path + [nums[i]])
        
        result = []
        backtrack(0, [])
        return result

            