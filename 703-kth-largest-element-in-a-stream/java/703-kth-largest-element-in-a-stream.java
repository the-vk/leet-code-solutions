class KthLargest {
  private final int k;
  private final PriorityQueue<Integer> scores;

  public KthLargest(int k, int[] nums) {
    this.k = k;
    this.scores = new PriorityQueue<>(k);
    for (var i = 0; i < nums.length; ++i) {
      this.scores.offer(nums[i]);
      if (this.scores.size() > this.k) {
        this.scores.poll();
      }
    }
  }
  
  public int add(int val) {
    this.scores.offer(val);
    if (this.scores.size() > this.k) {
      this.scores.poll();
    }
    
    return this.scores.peek();
  }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */