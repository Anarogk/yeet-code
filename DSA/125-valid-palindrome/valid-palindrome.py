import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        j = re.sub(r'[^a-z0-9]', '', s)
        return j == j[::-1]