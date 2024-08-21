import time

class Solution:
    def isHappy(self, n: int) -> bool:
        # timeout = time.time() + 0.00000799
        # digits = [int(x) for x in str(n)]
        # while sum(digits)!= 1:
        #     if time.time() > timeout:
        #         return False
        #     n = sum([x*x for x in digits])
        #     digits = [int(x) for x in str(n)]
        # return True


        nums = set()

        while n not in nums:
            nums.add(n)

            curr_sum = 0
            while n >= 10:
                curr_sum = curr_sum + (n % 10) ** 2
                n = n // 10

            curr_sum += n**2
            if curr_sum == 1:
                return True

            n = curr_sum

        return False

            