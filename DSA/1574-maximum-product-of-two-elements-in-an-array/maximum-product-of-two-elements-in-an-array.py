class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        heapq.heapify(nums)
        while len(nums)>2:
            heapq.heappop(nums)
        return (nums[0]-1)* (nums[1]-1) 