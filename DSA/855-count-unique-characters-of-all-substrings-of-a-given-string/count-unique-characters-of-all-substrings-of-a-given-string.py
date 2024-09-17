class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last_exists = collections.defaultdict(lambda: [-1, -1])
        res = 0
        for i, c in enumerate(s):
            last_exists[c][0], last_exists[c][1] = i, last_exists[c][0]
            for _, exists in last_exists.items(): res += exists[0] - exists[1]
        return res