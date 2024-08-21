class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {numbers[0]:0}
        for i in range(1, len(numbers)):
            if target -numbers[i] in dic.keys():
                return [dic.get(target-numbers[i])+1, i+1]
            else:
                dic.update({numbers[i]:i})
        return []



        
        # i, j = 0, len(numbers)-1
        # while i < j and i < len(numbers)-1:
        #     if numbers[i] + numbers[j] == target:
        #         return [i+1, j+1]
        #     j-=1
        #     if i ==j:
        #         j = len(numbers)-1
        #         i+=1
        # return -1









        # dic = {numbers[0]:1}
        # arr = []
        # for i in range(1, len(numbers)):
        #     if target- numbers[i] in dic:
        #         return [dic.get(target-numbers[i]), i+1]
        #     else:
        #         dic.update({numbers[i]:i+1})
        # return []