class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = float('-inf')
        i, j = 0, len(height)-1
        while i <j:
            min_height = min(height[i], height[j])
            vol = (j-i) * min_height
            maxx = max(maxx, vol)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return maxx





        # maximum = float("-inf")  # set max to -inf
        # i, j = 0, len(height) - 1  # initialized 2 pointers at end of array

        # while i < j:  # loop through height array
        #     # we select min of both -- because overflow
        #     min_height = min(height[i], height[j])
        #     vol = (j - i) * min_height  # vol =
        #     maximum = max(maximum, vol)
        #     if height[i] < height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return maximum