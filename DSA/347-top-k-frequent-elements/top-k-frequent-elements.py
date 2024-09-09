class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = Counter(nums)
        
        sorted_ele = dict(sorted(counter_map.items(), key= lambda item: item[1], reverse= True))

        return list(sorted_ele.keys())[:k]