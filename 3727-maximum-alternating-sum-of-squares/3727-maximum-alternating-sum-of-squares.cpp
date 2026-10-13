class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        long large=0,small=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            nums[i]=nums[i]*nums[i];
        }
        sort(nums.begin(), nums.end());
        int mid=n/2;
        for(int i=0;i<mid;i++){
            small+=nums[i];
        }
        for(mid;mid<n;mid++){
            large+=nums[mid];

        }
        return large-small;

    }
};