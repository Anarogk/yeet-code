class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j= 0 , len(height)-1
        maxx = min(height[i],height[j]) * (j-i)

        while i < j and i<len(height)-1:
            maxx = max(maxx, (min(height[i],height[j]) * (j-i)))
            
            if height[i] <height[j]:
                i+=1
            else:
                j-=1
        return maxx  