class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        for i in range(len(s)):
            temp = s[0]
            for i in range(len(s)-1):
                s[i] = s[i+1]
            s[-1] = temp
            if s == list(goal):
                return True
        return False
