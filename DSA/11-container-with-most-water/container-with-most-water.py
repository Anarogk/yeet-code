class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_vol = float("-inf")
        while i < j:
            min_height = min(height[i], height[j])
            max_vol = max(max_vol, min_height * (j - i))
            if height[j] <= height[i]:
                j -= 1
            else:
                i += 1

        return max_vol