class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sm = defaultdict(int)
        s = s1.strip().split()
        t = s2.strip().split()

        for i in s:
            sm[i] = 1+ sm.get(i, 0)

        for i in t:
            if i in sm:
                sm[i] +=1
            else:
                sm[i] = 1
        
        return [i for i in sm.keys() if sm[i]== 1]