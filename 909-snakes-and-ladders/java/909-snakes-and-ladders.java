class Solution {
  public int snakesAndLadders(int[][] board) {
    var n = board.length;
    var bl = new int[n * n];
    var c = 0;
    var cd = 1;
    var i = 0;
    for (var r = n - 1; r >= 0; --r) {
      while (c >=0 && c < n) {
        bl[i++] = board[r][c];
        c += cd;
      }
      cd *= -1;
      c += cd;
    }

    var dp = new int[n * n];
    for (i = 1; i < dp.length; ++i) {
      dp[i] = Integer.MAX_VALUE;
    }

    var queue = new ArrayDeque<Pair<Integer, Integer>>();
    queue.add(new Pair<>(0, 0));

    while (!queue.isEmpty()) {
      var p = queue.pollFirst();
      var square = p.getKey();
      var rolls = p.getValue();

      for (var r = 1; r <= 6; ++r) {
        var ns = square + r;
        if (ns >= (n*n)) {
          break;
        }
        if (bl[ns] != -1) {
          ns = bl[ns] - 1;
        }
        if (dp[ns] > rolls + 1) {
          dp[ns] = rolls + 1;
          queue.add(new Pair<>(ns, rolls + 1));
        }
      }
    }

    return dp[dp.length - 1] != Integer.MAX_VALUE ? dp[dp.length - 1] : -1;
  }
}

