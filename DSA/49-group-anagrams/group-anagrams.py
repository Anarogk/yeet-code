from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hmap = defaultdict(list)
        # for i in strs:
        #     k = "".join(sorted(i))
        #     hmap[k].append(i)
        
        # return list(hmap.values())

        h_map = defaultdict(list)

        for word in strs:
            w = "".join(sorted(word))
            h_map[w].append(word)

        return h_map.values()
