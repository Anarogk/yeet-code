class Solution:
    def intToRoman(self, num: int) -> str:
        nums = ["M","CM", "D","CD", "C","XC","L","XL","X","IX","V","IV","I"]
        imp = [1000, 900, 500, 400,100, 90, 50, 40, 10,9,5,4,1 ]
        st= ""
        i =0
        while num>0 and i < len(imp):
            if num >= imp[i]:
                num =num-imp[i]
                st+= nums[i]
            else:
                i+=1
        return st