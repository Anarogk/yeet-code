class Solution:
    def numberToWords(self, num: int) -> str:
        numbers = [
            1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20,
            19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        ]  # 31 numbers

        words = [
            "Billion", "Million", "Thousand", "Hundred", "Ninety", "Eighty",
            "Seventy", "Sixty", "Fifty", "Forty", "Thirty", "Twenty",
            "Nineteen", "Eighteen", "Seventeen", "Sixteen", "Fifteen", "Fourteen",
            "Thirteen", "Twelve", "Eleven", "Ten", "Nine", "Eight", "Seven",
            "Six", "Five", "Four", "Three", "Two", "One"
        ]

        result = []

        for i in range(31):
            if num >= numbers[i]:
                if num >= 100:
                    result.append(self.numberToWords(num // numbers[i]) + " " + words[i])
                else:
                    result.append(words[i])

                num %= numbers[i]

                if num == 0:
                    break

        return "Zero" if not result else " ".join(result)

        
    #     if num == 0:
    #         return "Zero"
        
    #     bigString = ["Thousand", "Million", "Billion"]
    #     result = self.numberToWordsHelper(num % 1000)
    #     num //= 1000
        
    #     for i in range(len(bigString)):
    #         if num > 0 and num % 1000 > 0:
    #             result = self.numberToWordsHelper(num % 1000) + bigString[i] + " " + result
    #         num //= 1000
        
    #     return result.strip()

    # def numberToWordsHelper(self, num: int) -> str:
    #     digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    #     teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",        "Eighteen", "Nineteen"]
    #     tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
    #     result = ""
    #     if num > 99:
    #         result += digitString[num // 100] + " Hundred "
        
    #     num %= 100
    #     if num < 20 and num > 9:
    #         result += teenString[num - 10] + " "
    #     else:
    #         if num >= 20:
    #             result += tenString[num // 10] + " "
    #         num %= 10
    #         if num > 0:
    #             result += digitString[num] + " "
        
    #     return result