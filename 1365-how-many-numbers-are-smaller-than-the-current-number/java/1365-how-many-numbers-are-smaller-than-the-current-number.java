class Solution {
  public int[] smallerNumbersThanCurrent(int[] nums) {
    var n = nums.length;
    var lookup = Arrays.copyOf(nums, n);     
    Arrays.sort(lookup);

    var answer = new int[n];
    for (var i = 0; i < n; ++i) {
      var v = nums[i];
      answer[i] = Arrays.binarySearch(lookup, v);
      while (answer[i] > 0 && lookup[answer[i]] == lookup[answer[i]-1]) {
        answer[i] -= 1;
      }
    }

    return answer;
  }
}