class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        s = set()
        freq1= []
        freq2 = []
        for a in word1:
            if a not in word2:
                return False
            if a not in s:
                freq1.append(word1.count(a))
                freq2.append(word2.count(a))
                s.add(a)
        freq1.sort()
        freq2.sort()
        if freq1 != freq2:
            return False
        return True
            