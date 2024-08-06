class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return 
        end_i = len(nums1)-1
        while n> 0 and m>0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_i] = nums2[n-1]
                n-=1
            else:
                nums1[end_i]= nums1[m-1]
                m-=1
            end_i-=1
    
        while n>0:
            nums1[end_i] = nums2[n-1]
            n-=1
            end_i -=1


