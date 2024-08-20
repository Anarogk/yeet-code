class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j=0
        if s == "":
            return True
        for i in range(len(t)):
            if t[i] == s[j]:
                j+=1
            if j ==len(s):
                return True
        return False
            