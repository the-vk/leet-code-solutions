class Solution {
  private ArrayList<Integer> weight;
  private Random rnd;

  public Solution(int[] w) {
    this.rnd = new Random();
    this.weight = new ArrayList<Integer>();
    var total = 0;
    for (var i = 0; i < w.length; ++i) {
      total += w[i];
      this.weight.add(total);
    }
  }
    
  public int pickIndex() {
    var v = this.rnd.nextInt(this.weight.getLast() + 1);
    var r = Collections.binarySearch(this.weight, v);
    if (r < 0) {
      r = -1 * (r + 1);
    }
    return r;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
