class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b=="0":
            return "0"
        num, num2 = 0,0
        for j,i in enumerate(a[::-1]):
            num += int(i) * 2**j
        for j,i in enumerate(b[::-1]):
            num += int(i) * 2**j
        s = ""
        while num>0:
            s = str(num%2) + s
            num = num//2
        
            
        return s