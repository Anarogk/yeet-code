class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans(nums.size());
        for (int i : nums) {
            ans[i] = nums[nums[i]];
        };
        return ans;   
    }
};