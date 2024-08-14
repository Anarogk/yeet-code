class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxx = 0
        while i < j:
            if self.area(i,height[i],j,height[j])> maxx:
                maxx = self.area(i,height[i],j,height[j])
            if height[i]< height[j]: 
                i+=1
            else:
                j-=1
            
        return maxx
            

    def area(self,i, a,j, b):
        return min(a,b)* (j-i)