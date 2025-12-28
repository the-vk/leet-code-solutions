class Solution {
  public int countNegatives(int[][] grid) {
    var m = grid.length;
    var n = grid[0].length;

    var res = 0;

    for (var r = 0; r < m; ++r) {
      for (var c = 0; c < n; ++c) {
        if (grid[r][c] >= 0) {
          continue;
        }

        if (c == 0) {
          res += (m - r) * n;
          return res;
        } else {
          res += n - c;
          break;
        }
      }
    }

    return res;
  }
}

