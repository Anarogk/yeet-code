class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)  # init counter
        l, total, res = 0, 0, 0  # left, cur total , res

        # iterating for right pointer of window
        for r in range(len(fruits)):
            count[fruits[r]] += 1  # increase count of curr r fruit
            total += 1  # increase total

            while len(count) > 2:  # validate window for most 2 type fruits
                f = fruits[l]  # remove left fruit
                count[f] -= 1
                total -= 1  # remove 1 from total
                l += 1  # move left pointer
                if not count[f]:  # if one type is completely 0 pop it
                    count.pop(f)

            res = max(res, total)  # update res to max of res or total

        return res