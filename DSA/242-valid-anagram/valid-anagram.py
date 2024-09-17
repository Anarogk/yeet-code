class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = defaultdict(int), defaultdict(int)

        for i in s:
            s1[i] = 1 + s1.get(i, 0)
        for i in t:
            t1[i] = 1 + t1.get(i, 0)
        return s1 == t1