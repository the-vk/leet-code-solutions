class Solution {
  public int repeatedNTimes(int[] nums) {
    var set = new HashSet<Integer>();
    for (var n : nums) {
      if (set.contains(n)) {
        return n;
      }
      set.add(n);
    }

    return -1;
  }
}
