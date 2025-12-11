class Solution {
 
  public int countCoveredBuildings(int n, int[][] buildings) {
    var rows = new HashMap<Integer, List<Integer>>();
    var cols = new HashMap<Integer, List<Integer>>();
    for (var b : buildings) {
      var r = b[0];
      var c = b[1];
      if (!rows.containsKey(r)) {
        rows.put(r, new ArrayList<Integer>());
      }
      if (!cols.containsKey(c)) {
        cols.put(c, new ArrayList<Integer>());
      }

      rows.get(r).add(c);
      cols.get(c).add(r);
    }

    for (var v: rows.values()) {
      v.sort(Comparator.naturalOrder());
    }
    for (var v: cols.values()) {
      v.sort(Comparator.naturalOrder());
    };

    var dirs = new int[][] {
      new int[] {-1, 0},
      new int[] {1, 0},
      new int[] {0, 1},
      new int[] {0, -1}
    };

    var result = 0;
    
    for (var b : buildings) {

      var r = b[0];
      var c = b[1];

      var row = rows.get(r);
      var col = cols.get(c);

      var covered_row = row.get(0) != c && row.get(row.size() - 1) != c;
      var covered_col = col.get(0) != r && col.get(col.size() - 1) != r;
      if (covered_row && covered_col) {
        result++;
      }
    }

    return result;
  }
 
}