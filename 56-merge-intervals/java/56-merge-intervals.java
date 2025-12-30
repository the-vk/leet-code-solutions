
class Solution {
  public int[][] merge(int[][] intervals) {
    List<int[]> ilist = Arrays.asList(intervals);
    List<int[]> answer = new ArrayList<>();

    ilist.sort(Comparator.comparing(v -> v[0]));

    for (var i : ilist) {
      if (answer.isEmpty()) {
        answer.add(i);
      } else {
        var current = answer.getLast();
        if (current[1] >= i[0]) {
          if (current[1] <= i[1]) {
            current[1] = i[1];
          }
        } else {
          answer.add(i);
        }
      }
    }

    return answer.toArray(new int[answer.size()][2]);
  }
}
