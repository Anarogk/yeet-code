class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            a = s[0]
            s = s[1:] + a
            if s == goal:
                return True
        return False
