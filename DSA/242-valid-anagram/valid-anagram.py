class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        
        for i in s:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i] = 1
        for j in t:
            if j in dic2:
                dic2[j]+=1
            else:
                dic2[j] = 1
        for k in dic1:
            if k not in dic2 or dic1[k] != dic2[k]:
                return False
        return True