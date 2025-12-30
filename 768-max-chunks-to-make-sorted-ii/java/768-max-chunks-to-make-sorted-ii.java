class Solution {
  public int maxChunksToSorted(int[] arr) {
    var n = arr.length;
    var chunks = 1;

    var maxLeft = new int[n];
    maxLeft[0] = arr[0];
    var minRight = new int[n];
    minRight[n-1] = arr[n-1];

    for (var i = 1; i < n; ++i) {
      maxLeft[i] = Math.max(maxLeft[i-1], arr[i]);
    }

    for (var i = n-2; i >= 0; --i) {
      minRight[i] = Math.min(minRight[i+1], arr[i]);
    }

    for (var i = 0; i < n-1; ++i) {
      if (maxLeft[i] <= minRight[i+1]) {
        chunks++;
      }
    }

    System.out.println("minRight: " + String.join(", ", IntStream.of(minRight).boxed().map(v -> v.toString()).toList()));
    System.out.println("maxLeft: " + String.join(", ", IntStream.of(maxLeft).boxed().map(v -> v.toString()).toList()));

    return chunks;
  }
}
