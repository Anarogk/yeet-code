class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        count =0
        dic = dict()
        for i in nums:
            if i in dic.keys():
                dic[i] +=1
            else:
                dic[i] = 1
        for i,j in dic.items():
            if j> n:
                return i

        return count
