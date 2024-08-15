class Solution:
    def intToRoman(self, num: int) -> str:
        map = [1000, 900, 500, 400, 100, 90 , 50 , 40, 10, 9, 5, 4, 1]
        rom = ["M", "CM", "D", "CD", "C", "XC", "L","XL","X","IX","V","IV","I"]
        i=0
        res = ''
        while num> 0 and i<len(map):
            if num >=map[i]:
                res+=rom[i]
                num -= map[i]
            else:
                i+=1
        return res