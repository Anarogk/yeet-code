class Solution:
    def isValid(self, word: str) -> bool:
        vovel , consonent = False, False
        if len(word) <3:
            return False
        for i in word:
            if not i.isalnum():
                return False
            if i in "aeiouAEIOU":
                vovel = True
            if i.isalpha() and i not in "aeiouAEIOU":
                consonent = True
        if vovel and consonent:
            return True
        return False
