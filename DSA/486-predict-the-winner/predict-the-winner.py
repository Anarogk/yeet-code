class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        diff = nums        
        for gap in range(1, len(nums)):
            diff = [max(nums[lo]-diff[lo+1], nums[lo+gap]-diff[lo]) for lo in range(len(nums)-gap)]

        return diff[0] >= 0
                