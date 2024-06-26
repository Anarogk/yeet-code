class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []

        def back(r):
            if r == n:
                result.append(curr[:])
            
            for c in range(n):
                if c in column or r+c in dig or r-c in adig:
                    continue
                dig.add(r+c)
                column.add(c)
                adig.add(r-c)
                curr.append('.'*c+'Q'+'.'*(n-c-1))
                back(r+1)
                dig.remove(r+c)
                column.remove(c)
                adig.remove(r-c)
                curr.pop()

        column, dig, adig, curr, result = set(), set(), set(), [], []
        back(0)

        return result