class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = prev = 0
        l = []
        if len(nums) ==1:
            return [f"{nums[0]}"]
        for i in range(1,len(nums)):
            if i == len(nums) -1:
                if nums[i]- nums[prev] == 1:
                    l.append(f"{nums[start]}->{nums[i]}")
                    break
                elif start == prev:
                    l.append(f"{nums[start]}")
                    l.append(f"{nums[i]}")
                    break
                else:
                    l.append(f"{nums[start]}->{nums[prev]}")
                    l.append(f"{nums[i]}")
                    break
            if nums[i] - nums[prev] ==1:
                prev = i
            else:
                if nums[start] - nums[prev] == 0 or start == prev:
                    l.append(f"{nums[start]}")
                elif nums[prev]- nums[start] >= 1:
                    l.append(f"{nums[start]}->{nums[prev]}")
                start = i
                prev = i
        return l