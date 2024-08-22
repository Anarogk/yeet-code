class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for i in s:
            dic[i]+=1
        for j in t:
            dic[j]-=1
        
        for i in dic.values():
            if i != 0:
                return False
        return True