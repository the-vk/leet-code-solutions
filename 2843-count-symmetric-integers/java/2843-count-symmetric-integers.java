class Solution {
  public int countSymmetricIntegers(int low, int high) {
    return (int)IntStream.rangeClosed(low, high)
      .boxed()
      .map(this::digitize)
      .map(this::isSymmetric)
      .filter(v -> v)
      .count();
  }

  private List<Integer> digitize(int v) {
    var res = new ArrayList<Integer>();
    while (v > 0) {
      res.addFirst(v % 10);
      v /= 10;
    }
    return res;
  }

  private boolean isSymmetric(List<Integer> number) {
    var n = number.size();

    if (n % 2 != 0) {
      return false;
    }

    return number.stream().limit(n/2).reduce((l, r) -> l + r).get() == 
      number.stream().skip(n/2).reduce((l, r) -> l + r).get();
  }
}
