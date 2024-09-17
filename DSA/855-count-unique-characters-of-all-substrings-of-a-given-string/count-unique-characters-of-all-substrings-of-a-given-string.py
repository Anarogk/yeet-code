class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dp = defaultdict(list)
        ans = 0
        for i, c in enumerate(s):
            dp[c].append(i)

        for arr in dp.values():
            for i, idx in enumerate(arr):
                left = 0 if i == 0 else arr[i - 1] + 1
                right = len(s) - 1 if i == len(arr) - 1 else arr[i + 1] - 1
                ans += (idx - left + 1) * (right + 1 - idx)
        return ans