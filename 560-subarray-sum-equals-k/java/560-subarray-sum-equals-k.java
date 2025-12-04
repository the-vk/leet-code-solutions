class Solution {
  public int subarraySum(int[] nums, int k) {
    HashMap<Integer, Integer> subCount = new HashMap<>();
    subCount.put(0, 1);
    int total = 0, count = 0;

    for (var n : nums) {
      total += n;

      if (subCount.containsKey(total - k)) {
        count += subCount.get(total - k);
      }

      subCount.put(total, subCount.getOrDefault(total, 0) + 1);
    }

    return count;
  }
}