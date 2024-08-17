class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        while i< j:
            if s[i] in "AEIOUaeiou"and s[j] in "AEIOUaeiou":
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
                continue
            
            if s[i] not in "AEIOUaeiou":
                i+=1
            if s[j] not in "AEIOUaeiou":
                j-=1
       
        k ="".join([i for i in s])
        return k    