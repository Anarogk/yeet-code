class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet: set[str] = set()  # charset
        start = 0  # starting of curr substring
        res = 0  # result string

        for curr in range(len(s)):  # iterate over s
            while s[curr] in charSet:  # while curr in charSet we remove from start pos
                charSet.remove(s[start])
                start += 1  # and move start until distinct
            charSet.add(s[curr])  # add new
            # result is max of current max or new substring
            res = max(res, curr - start + 1)
        return res