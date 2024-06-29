from heapq import heapify

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()

        for num in nums:
            if num:
                unique.add(num)
            
        return len(unique)
                    
                