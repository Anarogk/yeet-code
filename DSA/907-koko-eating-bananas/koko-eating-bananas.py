class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isSuff(cnt):
            return sum(ceil(i/cnt)for i in piles)<=h
        if h== len(piles):
            return max(piles)
        l , r = 1, max(piles)
        while l<r:
            m = (l+r)//2
            if isSuff(m):
                r= m
            else:
                l= m+1
        return l


    
    
