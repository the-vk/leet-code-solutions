class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        var counter = new HashMap<Integer, Integer>();
        for (var i : nums) {
          counter.merge(i, -1, (o, n) -> o + n);
        }
        var pq = new PriorityQueue<HashMap.Entry<Integer, Integer>>(Comparator.comparing(v -> v.getValue()));
        for (var kv : counter.entrySet()) {
          pq.add(kv);
        }
        var answer = new int[k];
        while (k > 0) {
          answer[answer.length - k] = pq.poll().getKey();
          k -= 1;
        }
        return answer;
    }
}