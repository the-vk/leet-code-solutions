class Solution {
  public int majorityElement(int[] nums) {
    var map = new HashMap<Integer, Integer>();
    for (var n : nums) {
      if (map.containsKey(n)) {
        map.put(n, map.get(n) + 1);
      } else {
        map.put(n, 1);
      }
    }

    Comparator<Map.Entry<Integer, Integer>> cmp = Comparator.comparing(v -> v.getValue());

    return map.entrySet().stream().sorted(cmp.reversed()).findFirst().get().getKey();
  }
}
