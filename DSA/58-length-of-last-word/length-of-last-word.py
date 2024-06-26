class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in s[::-1]:
            if i ==" " and count != 0:
                break
            if i != " ":
                print(i)
                count+=1        
        return count