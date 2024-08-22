class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for x in s:
            dic[x] +=1
        for x in t:
            dic[x] -=1
        for i in dic.values():
            if i != 0:
                return False
        return True