class Solution {
  public int[] plusOne(int[] digits) {
    var dig = new ArrayList<Integer>(IntStream.of(digits).boxed().toList());

    int carry = 1;
    var i = dig.size() - 1;

    while (carry != 0 && i >= 0) {
      var d = dig.get(i);
      d = d + carry;
      carry = d / 10;
      d = d % 10;
      dig.set(i, d);
      i--;
    }

    if (carry != 0) {
      dig.addFirst(carry);
    }

    return dig.stream().mapToInt(v -> v).toArray();
  }
}
