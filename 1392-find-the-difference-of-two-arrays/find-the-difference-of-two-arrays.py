class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a= set(nums1)
        b = set(nums2)
        return [(a-b), (b-a)]