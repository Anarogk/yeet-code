class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # count

        l = 0
        max_f = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)  # add 1 to count of curr
            max_f = max(max_f, count[s[r]]) # max is max of max or curr count

            if (r - l + 1) - max_f > k: # if len - max > k we decrement count from left element
                count[s[l]] -= 1
                l += 1 # move left

        return r - l + 1 # return left