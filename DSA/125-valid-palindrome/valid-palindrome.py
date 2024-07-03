class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        j = ""
        for i in s:
            if i.isalnum():
                j +=i
        return j == j[::-1]