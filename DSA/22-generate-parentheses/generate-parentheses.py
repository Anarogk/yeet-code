class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []

        def backtrack(opend, closed):
            if opend == closed == n:
                res.append("".join(s))
                return

            if opend <n:
                s.append("(")
                backtrack(opend+1, closed)
                s.pop()
            if closed < opend:
                s.append(")")
                backtrack(opend, closed +1)
                s.pop()

        backtrack(0,0 )
        return res