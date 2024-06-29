import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cn = Counter(arr)
        freq = sorted(cn.values(), reverse=True)
        rem = 0
        nums = 0

        for i in freq:
            rem +=i
            nums += 1
            if rem >= len(arr)//2:
                break
        return nums
        # heapq.heapify(cn)
        # amount = len(arr)//2 + len(arr) % 2
        # counter = 0
        # while amount > 0:
        #     amount += heapq.heappop(cn)
        #     counter += 1
        return counter