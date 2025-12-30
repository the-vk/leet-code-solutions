class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int i = 0, j = 0;
    var n = nums1.length;
    var m = nums2.length;
    int m1 = 0, m2 = 0;

    for (var count = 0; count <= (n + m) / 2; ++count) {
      m2 = m1;
      if (i != n && j != m) {
        if (nums1[i] < nums2[j]) {
          m1 = nums1[i++];
        } else {
          m1 = nums2[j++];
        }
      } else if (i < n) {
        m1 = nums1[i++];
      } else {
        m1 = nums2[j++];
      }
    }

    if ((n + m) % 2 == 1) {
      return (double) m1;
    } else {
      return ((double)m1 + (double)m2) / 2.0;
    }
  }
}

