import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums_h = nums
        heapq.heapify(nums)
        print(nums)
        arr = []
        while nums:
            item = heapq.heappop(nums)
            arr.append(heapq.heappop(nums))
            arr.append(item)

        return arr