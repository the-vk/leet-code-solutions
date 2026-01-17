class Solution {
  public int titleToNumber(String columnTitle) {
    var ans = 0;
    for (var c : columnTitle.chars().boxed().toList()) {
      ans *= 26;
      ans += charToCol(c);
    }
    return ans;
  }

  private int charToCol(int c) {
    return c - 'A' + 1;
  }
}
