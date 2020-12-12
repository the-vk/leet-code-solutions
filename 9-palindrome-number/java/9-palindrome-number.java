import java.util.LinkedList;

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        LinkedList<Integer> digits = new LinkedList<Integer>();
        while (x != 0) {
            int d = x % 10;
            digits.add(d);
            x /= 10;
        }
        Iterator<Integer> head = digits.iterator();
        Iterator<Integer> tail = digits.descendingIterator();
        while (head.hasNext() && tail.hasNext()) {
            int hd = head.next();
            int td = tail.next();
            if (hd != td) {
                return false;
            }
        }
        return true;
    }
}