class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i, j in enumerate(nums):
            if j in hash_map:
                return True
            else:
                hash_map[j] = i
        return False