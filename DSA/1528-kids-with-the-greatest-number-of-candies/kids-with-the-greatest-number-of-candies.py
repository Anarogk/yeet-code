class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if c + extraCandies >= max(candies) else False for c in candies]
