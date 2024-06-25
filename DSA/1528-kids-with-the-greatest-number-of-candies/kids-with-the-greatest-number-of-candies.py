class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = max(candies)
        s =[]
        for i in candies:
            if i+extraCandies>=l:
                s.append(True)
            else:
                s.append(False)
        return s
