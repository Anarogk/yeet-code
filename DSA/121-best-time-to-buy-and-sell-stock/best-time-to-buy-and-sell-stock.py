class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i, j = 0, len(prices) - 1
        # max_p = float("-inf")

        # while i < j:
        #     max_p = max(max_p, prices[j] - prices[i])
        #     j -= 1
        #     if j == i:
        #         i += 1
        #         j = len(prices) - 1

        # return 0 if max_p < 0 else max_p

        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res