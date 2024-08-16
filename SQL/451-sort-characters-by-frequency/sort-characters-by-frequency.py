class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(sorted([i*j for i, j in Counter(s).items()], key=len, reverse=True))