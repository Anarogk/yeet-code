import re
class Solution:
    def decodeString(self, s: str) -> str:
        while (m:= re.search(r"([0-9]+)\[([a-z]+)\]", s)):
            s = s.replace(m.group(), f"{m[2]* int(m[1])}")
        return s
