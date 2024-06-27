class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i == len(prices):
                return 0

            take = prices[i] + dfs(i + 1, 2 * i + 1)
            skip = dfs(i + 1, j) if j >= i and i > 0 else float('inf')

            return min(take, skip)

        return dfs(0, 0)