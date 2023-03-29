public class Solution {
    public int[] CountBits(int num) {
        if (num == 0) return new int[] { 0 };
        var result = new int[num + 1];
        int power = 1;
        for (var i = 1; i <= num; ++i) {
            if (i == power * 2) power *= 2;
            result[i] = result[i - power] + 1;
        }
        return result;
    }
}