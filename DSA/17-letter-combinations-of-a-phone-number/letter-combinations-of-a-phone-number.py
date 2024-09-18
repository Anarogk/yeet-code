class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res: list[str] = []

        digitsToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i: int, curStr: str) -> None:
            if len(digits) == len(curStr):
                res.append(curStr)
                return

            for c in digitsToLetter[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res