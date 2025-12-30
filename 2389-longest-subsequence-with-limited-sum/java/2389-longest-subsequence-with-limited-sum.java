class Solution {
  public int[] answerQueries(int[] nums, int[] queries) {
    List<Integer> items = IntStream.of(nums).boxed().sorted(Comparator.reverseOrder()).toList();

    var total = items.stream().reduce((l, r) -> l + r).get();

    var answer = new int[queries.length];

    for (var i = 0; i < answer.length; ++i) {
      var current = total;
      for (var j = 0; j < items.size(); ++j) {
        if (current <= queries[i]) {
          answer[i] = nums.length - j;
          break;
        }
        current -= items.get(j);
      }
    }

    return answer;
  }
}
