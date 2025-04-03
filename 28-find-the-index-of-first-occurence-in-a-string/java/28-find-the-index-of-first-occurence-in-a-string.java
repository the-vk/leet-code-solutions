class Solution {
    public int strStr(String haystack, String needle) {
        int l = 0;
        int r = 0;
        while (l < haystack.length() - needle.length() + 1) {
          while (r < needle.length() && haystack.charAt(l+r) == needle.charAt(r)) {
            r++;
          }
          if (r == needle.length()) {
            return l;
          }
          l++;
          r = 0;
        }
        return -1;
    }
}