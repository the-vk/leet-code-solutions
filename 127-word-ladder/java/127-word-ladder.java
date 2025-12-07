class Solution {
  public int ladderLength(String beginWord, String endWord, List<String> wordList) {
    var set = new HashSet<String>(wordList);
    if (!set.contains(endWord)) {
      return 0;
    }

    var queue = new ArrayDeque<String>(List.of(beginWord));
    var seen = new HashSet<String>(List.of(beginWord));

    var changes = 1;

    while (!queue.isEmpty()) {
      var size = queue.size();
      for (var i = 0; i < size; ++i) {
        var w = queue.poll();
        if (endWord.equals(w)) {
          return changes;
        }

        seen.add(w);

        for (var ci = 0; ci < w.length(); ++ci) {
          for (int c = 'a'; c <= 'z'; ++c) {
            var chars = w.toCharArray();
            chars[ci] = (char)c;

            var nextStr = String.valueOf(chars);
            if (set.contains(nextStr) && !seen.contains(nextStr)) {
              queue.add(nextStr);
            }
          }
        }
      }
      
      ++changes;
    }

    return 0;
  }
}