class Solution:
    def isValid(self, word: str) -> bool:
        vowel , consonant = 0,0
        if len(word) <3:
            return False
        if '@' in word or '#' in word or '$' in word:
            return False
        for i in range(len(word)):
            if word[i].isalpha():
                if word[i] in ['a', 'e', 'i', 'o', 'u'] or word[i] in ['A', 'E', 'I', 'O', 'U']:
                    vowel += 1
                else:
                    consonant += 1
        return True if (vowel != 0 and consonant != 0) else False