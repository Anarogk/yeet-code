class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])       














        # count = 0
        # s = s[::-1]
        # for i in range(len(s)):
        #     if s[i] == " " and count != 0:
        #         print(i)
        #         return count
        #     if s[i] != " ":
        #         if i == len(s)-1:
        #             return count
        #         count += 1
            
        # return 0