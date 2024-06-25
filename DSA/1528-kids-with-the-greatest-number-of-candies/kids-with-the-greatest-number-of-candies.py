class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = 0
        for i in candies:
            if highest < i:
                highest = i
        diff = highest - extraCandies
        arr = []
        for j in candies:
            if j >= diff:
                arr.append(True)
            else:
                arr.append(False)
        return arr
