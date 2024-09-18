class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # start, res = 0, 0

        # for i in s:
        #     while i in charSet:
        #         charSet.remove(s[start])
        #         start += 1
        #     charSet.add(i)

        #     res = max(res, len(charSet))
        # return res

        charSet: set = set()
        start, res = 0, 0

        for end in s:
            while end in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(end)
            res = max(res, len(charSet))

        return res