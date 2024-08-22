class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= k% len(nums)
        start = len(nums) -k
        end = len(nums) -1
        while start< end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1  
        print(nums[k:])
        start = 0
        end = len(nums)-k-1
        while start < end:
            nums[start] , nums[end]= nums[end], nums[start]
            start +=1
            end-=1
        print(nums[:k])
        start = 0
        end = len(nums) -1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
        print(nums[:])

        
        