class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, total = 0, 1  # set start and total len of substring
        for i in range(len(s)):
            right = i  # first right means curr pos
            # checking right bound and curr letter
            while right < len(s) - 1 and s[right] == s[i]:
                right += 1

            left = i - 1  # decrementing left to be curr pos -1
            # checking left bound and left letter equals right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # we continue left and right
                right += 1

            # getting len of substring that is s[left : right] == right -left +1 ( +1 for inclusive right)
            cur = right - left - 1
            if cur > total:
                total = cur
                start = left + 1
        return s[start : start + total] # returning s[start: start + total]


    