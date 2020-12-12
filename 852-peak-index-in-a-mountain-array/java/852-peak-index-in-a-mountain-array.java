class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int maxi = 0;
        int max = arr[maxi];
        for (int i = 1; i < arr.length; ++i) {
            if (arr[i] > max) {
                max = arr[i];
                maxi = i;
            }
        }
        return maxi;
    }
}