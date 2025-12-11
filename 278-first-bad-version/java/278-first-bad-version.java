/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
  public int firstBadVersion(int n) {
    int l = 1, r = n;   

    while (l != r) {
      var m = (l + r) / 2;
      if (this.isBadVersion(m)) {
        r = m;
      } else {
        l = m + 1;
      }
    }

    return l;
  }
}