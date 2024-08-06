class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int l=0, r=0;
        vector<int> ans = nums1;
        int i = 0;
        while(l<m && r<n){
            if(ans[l] < nums2[r]){
                nums1[i] = ans[l];
                ++l;
            }
            else{
                nums1[i] = nums2[r];
                ++r;
            }
            ++i;
        }
        for(int j=r; j<n; j++){
            nums1[i] = nums2[j];
            ++i;
        }
        for(int j=l; j<m; j++){
            nums1[i] = ans[j];
            ++i;
        }
    }      
};