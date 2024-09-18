class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for _ in range(2, n + 1):
            temp = curr  # saving curr for prev to move
            curr = prev + curr  # calculating current
            prev = temp  # moving prev ahead
        return curr