class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        c = []
        s = []
        b = []
        for i in nums1:
            if i not in nums2 and i not in s:
                s.append(i)
        for i in nums2:
            if i not in nums1 and i not in b:
                b.append(i)
        c.append(s)
        c.append(b)
        return c