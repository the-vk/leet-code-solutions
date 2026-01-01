class Solution {
  public String minRemoveToMakeValid(String s) {
    var openStack = new ArrayDeque<Integer>();
    var closeStack = new ArrayDeque<Integer>();

    for (var i = 0; i < s.length(); ++i) {
      var c = s.charAt(i);
      switch (c) {
        case '(':
          openStack.add(i);
          break;
        case ')':
          if (!openStack.isEmpty() && openStack.peekLast() < i && (
            closeStack.isEmpty() || closeStack.peekLast() < openStack.peekLast()
          )) {
            openStack.pollLast();
          } else {
            closeStack.add(i);
          }
          break;
      }
    }

    var errors = new ArrayList<Integer>();
    errors.addAll(openStack);
    errors.addAll(closeStack);
    errors.sort(Comparator.naturalOrder());


    var sb = new StringBuilder();
    var ei = 0;
    for (var i = 0; i < s.length(); ++i) {
      if (!errors.isEmpty() && ei < errors.size() && i == errors.get(ei)) {
        ei++;
        continue;
      }
      sb.append(s.charAt(i));
    }

    return sb.toString();
  }
}
