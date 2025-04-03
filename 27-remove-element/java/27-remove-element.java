class Solution {
    public int removeElement(int[] nums, int val) {
        int l = 0;
        int r = 0;
        int n = nums.length;
        if (n == 0) {
          return 0;
        }
        while (r < n) {
          while (r < n && nums[r] == val) {
            r++;
          }
          if (r == n) {
            break;
          }
          nums[l] = nums[r];
          l++;
          r++;
        }
        return l;
    }
}