class Solution {
  private final static int BASE = 1337;
  
  private int powmod(int a, int k) {
    a %= BASE;
    int result = 1;
    for (var i = 0; i < k; ++i) {
      result = (result * a) % BASE;
    }

    return result;
  }

  public int superPow(int a, int[] b) {
    int result = 1;
    for (int i = b.length - 1; i >= 0; --i) {
      result = (result * powmod(a, b[i])) % BASE;
      a = powmod(a, 10);
    }
    return result;
  }
}
