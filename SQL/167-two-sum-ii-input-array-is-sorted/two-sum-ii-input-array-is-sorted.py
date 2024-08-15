class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {numbers[0]:1}
        arr = []
        for i in range(1, len(numbers)):
            if target- numbers[i] in dic:
                return [dic.get(target-numbers[i]), i+1]
            else:
                dic.update({numbers[i]:i+1})
        return []