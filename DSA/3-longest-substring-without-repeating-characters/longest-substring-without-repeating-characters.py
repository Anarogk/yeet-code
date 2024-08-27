class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0 if len(s) == 0 else 1
        t = set()
        left = 0
        maximum = 0
        for i in range(len(s)):
            while s[i] in t:
                t.remove(s[left])
                left +=1
            t.add(s[i])
            maximum = max(maximum, i-left +1)
        return maximum















        # t = set()
        # left , maxs = 0, 0
        # for i in range(len(s)):
        #     while s[i] in t:
        #         t.remove(s[left])
        #         left +=1
        #     t.add(s[i])
        #     maxs = max(maxs, i -left+1)

        # return maxs