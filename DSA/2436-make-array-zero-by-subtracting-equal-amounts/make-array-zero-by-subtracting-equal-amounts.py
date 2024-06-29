from heapq import heapify

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniqueNumbers = set()
        for i in nums:
            if i==0:
                continue
            if i in uniqueNumbers:
                continue
            uniqueNumbers.add(i)
        return len(uniqueNumbers)
                    
                