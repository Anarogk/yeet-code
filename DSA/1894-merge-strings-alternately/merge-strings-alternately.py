class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        for i in range(min(len(word1), len(word2))):
            s += (str(word1[i])+ str(word2[i]))
        if len(word1)> len(word2):
                s += str(word1[len(word2):])    
        if len(word1)< len(word2):
                s += str(word2[len(word1):])

        return s