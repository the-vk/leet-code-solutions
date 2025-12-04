class Solution {
  public int lengthOfLongestSubstring(String str) {
    var seenPositions = new HashMap<Character, Integer>();

    var substringMaxLength = 0;
    var substringStart = 0;

    for (var i = 0; i < str.length(); ++i) {
      var c = str.charAt(i);
      if (seenPositions.containsKey(c)) {
        substringStart = Math.max(substringStart, seenPositions.get(c) + 1);
      }

      seenPositions.put(c, i);
      substringMaxLength = Math.max(substringMaxLength, i - substringStart + 1);
    }

    return substringMaxLength;
  }
}
