class Solution {
  public int minimumDeviation(int[] nums) {
    var pq = new PriorityQueue<Integer>(Comparator.<Integer>comparingInt(v -> v).reversed());

    int min_v = Integer.MAX_VALUE;
    int min_dev = Integer.MAX_VALUE;

    for (var i = 0; i < nums.length; ++i) {
      var v = nums[i];
      if (v % 2 == 1) {
        v *= 2;
      }
      min_v = Math.min(min_v, v);

      pq.add(v);
    }

    while (true) {
      var max_v = pq.poll();
      min_dev = Math.min(min_dev, max_v - min_v);
      if (max_v % 2 == 1) {
        break;
      }
      max_v /= 2;
      min_v = Math.min(min_v, max_v);
      pq.add(max_v);
    }

    return min_dev;
  }
}

