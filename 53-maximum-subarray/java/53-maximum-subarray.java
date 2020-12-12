class Solution {
    public int maxSubArray(int[] nums) {
        int ans = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i-1] > 0) {
                nums[i] += nums[i-1];
            }
            ans = Math.max(ans, nums[i]);
        }
        return ans;
    }
}
