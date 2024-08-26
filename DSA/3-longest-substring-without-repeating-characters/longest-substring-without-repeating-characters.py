class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = set()
        left , maxs = 0, 0
        for i in range(len(s)):
            while s[i] in t:
                t.remove(s[left])
                left +=1
            t.add(s[i])
            maxs = max(maxs, i -left+1)

        return maxs















        # t = set()
        # left , maxs = 0, 0
        # for i in range(len(s)):
        #     while s[i] in t:
        #         t.remove(s[left])
        #         left +=1
        #     t.add(s[i])
        #     maxs = max(maxs, i -left+1)

        # return maxs