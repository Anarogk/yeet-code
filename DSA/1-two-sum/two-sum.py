class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, j in enumerate(nums):
            if target - j in h_map:
                return [h_map.get(target - j), i]
            else:
                h_map[j] = i

        return []