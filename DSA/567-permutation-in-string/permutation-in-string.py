class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm, w, s = Counter(s1), len(s1), set(s1)
        for i in range(len(s2)):
            if s2[i] in s:  # right border
                hm[s2[i]] -= 1
                if hm[s2[i]] == 0:
                    hm.pop(s2[i])
            if i >= w and s2[i - w] in s:  # left border
                hm[s2[i - w]] += 1
                if hm[s2[i - w]] == 0:
                    hm.pop(s2[i - w])
            if len(hm) == 0:
                return True
        return False