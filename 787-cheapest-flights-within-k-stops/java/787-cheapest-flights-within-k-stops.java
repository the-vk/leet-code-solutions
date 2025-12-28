class Solution {
  public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
    var edges = new HashMap<Integer, List<Pair<Integer, Integer>>>();

    for (var i = 0; i < flights.length; ++i) {
      var from = flights[i][0];
      var to = flights[i][1];
      var price = flights[i][2];

      if (!edges.containsKey(from)) {
        edges.put(from, new ArrayList<>());
      }

      edges.get(from).add(new Pair<>(to, price));
    }

    var cost_dst = new int[n];
    for (var i = 0; i < n; ++i) {
      cost_dst[i] = Integer.MAX_VALUE;
    }

    var queue = new ArrayDeque<Pair<Integer, Integer>>();
    queue.add(new Pair<>(src, 0));
    var stops = 0;

    while (queue.size() > 0 && stops <= k) {
      var size = queue.size();
      for (var i = 0; i < size; ++i) {
        var leg = queue.pollFirst();
        var origin = leg.getKey();
        var cost = leg.getValue();

        for (var t : edges.getOrDefault(origin, List.of())) {
          var destination = t.getKey();
          var price = t.getValue();

          var cost_to = cost + price;
          if (cost_dst[destination] < cost_to) {
            continue;
          }
          cost_dst[destination] = cost_to;
          queue.add(new Pair<>(destination, cost_to));
        }
      }
      ++stops;
    }

    return cost_dst[dst] != Integer.MAX_VALUE ? cost_dst[dst] : -1;
  }
}

