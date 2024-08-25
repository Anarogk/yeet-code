
class Solution:
    def decodeString(self, s: str) -> str:
        # while (m:= re.search(r"([0-9]+)\[([a-z]+)\]", s)):
        #     s = s.replace(m.group(), f"{m[2]* int(m[1])}")
        # return s
        st = []; curNum = 0; curStr = ''
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == '[':
                st.append(curStr)
                st.append(curNum)
                curStr = ''
                curNum = 0
            elif c == ']':
                preNum = st.pop()
                prevStr = st.pop()
                curStr = prevStr + curStr * preNum
            else:
                curStr += c
        return curStr