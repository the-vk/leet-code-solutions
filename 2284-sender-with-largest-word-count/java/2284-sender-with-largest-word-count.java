class Solution {
  public String largestWordCount(String[] messages, String[] senders) {
    var counter = new HashMap<String, Integer>();
    var n = senders.length;
    for (var i = 0; i < n; ++i) {
      var s = senders[i];
      var m = messages[i];
      var count = m.split(" ").length;
      counter.put(s, counter.getOrDefault(s, 0) + count);
    }
    var largestWordCount = counter.values().stream().sorted(Comparator.reverseOrder()).findFirst().get();
    var candidates = new ArrayList<String>();
    for (var kv : counter.entrySet()) {
      if (largestWordCount == kv.getValue()) {
        candidates.add(kv.getKey());
      }
    }
    candidates.sort(Comparator.reverseOrder());
    return candidates.get(0);
  }
}
