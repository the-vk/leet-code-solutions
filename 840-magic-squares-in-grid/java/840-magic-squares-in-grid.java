class Solution {
  public int numMagicSquaresInside(int[][] grid) {
    var ans = 0;

    var rows = grid.length;
    var cols = grid[0].length;

    for (var r = 0; r <= (rows - 3); ++r) {
      for (var c = 0; c <= (cols - 3); ++c) {
        if (this.isMagic(grid, r, c)) {
          ans += 1;
        }
      }
    }

    return ans;
  }

  private boolean isMagic(int[][] grid, int r, int c) {
    var expected = new HashSet<Integer>(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9));

    for (var rr = r; rr < (r + 3); ++rr) {
      for (var cc = c; cc < (c + 3); ++cc) {
        var v = grid[rr][cc];
        if (v < 1 || v > 9) {
          return false;
        }
        if (!expected.remove(v)) {
          return false;
        }
      }
    }
    if (expected.size() != 0) {
      return false;
    }

    var sums = new int[8];

    for (var i = 0; i < 3; ++i) {
      sums[i] = grid[r+i][c+0] + grid[r+i][c+1] + grid[r+i][c+2];
      sums[i+3] = grid[r+0][c+i] + grid[r+1][c+i] + grid[r+2][c+i];
    }

    sums[6] = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2];
    sums[7] = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c];

    for (var i = 1; i < sums.length; ++i) {
      if (sums[0] != sums[i]) {
        return false;
      }
    }

    return true;
  }
}

