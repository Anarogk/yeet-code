import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cn = Counter(arr)
        print(cn)
        cn = [-value for value in cn.values()]
        heapq.heapify(cn)
        
        amount = len(arr)//2 + len(arr) % 2
        counter = 0
        while amount > 0:
            amount += heapq.heappop(cn)
            counter += 1
        return counter