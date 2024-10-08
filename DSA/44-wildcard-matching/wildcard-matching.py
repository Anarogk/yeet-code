class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        dp_ip1 = [True] * (n + 1)
        for j in range(n-1, -1, -1):
            dp_ip1[j] = p[j] == '*' and dp_ip1[j+1]
        
        for i in range(m-1, -1, -1):
            dp_i = [False] * (n+1)
            for j in range(n-1, -1, -1):
                if s[i] == p[j] or p[j] == '?':
                    dp_i[j] = dp_ip1[j+1]
                elif p[j] == '*':
                    dp_i[j] = dp_ip1[j] or dp_i[j+1]
                else:
                    dp_i[j] = False
            dp_ip1 = dp_i
        return dp_ip1[0]