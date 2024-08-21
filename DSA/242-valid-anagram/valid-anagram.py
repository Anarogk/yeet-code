class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if Counter(list(s)) != Counter(list(t)):
            return False
        return True