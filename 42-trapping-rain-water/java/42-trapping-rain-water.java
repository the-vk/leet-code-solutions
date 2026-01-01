class Solution {
  public int trap(int[] height) {
    var answer = 0;

    int left = 0, right = height.length - 1;
    int leftMax = 0, rightMax = 0;

    while (left <= right) {
      if (height[left] < height[right]) {
        if (leftMax > height[left]) {
          answer += leftMax - height[left];
        } else {
          leftMax = height[left];
        }
        left++;
      } else {
        if (rightMax > height[right]) {
          answer += rightMax - height[right];
        } else {
          rightMax = height[right];
        }
        right--;
      }
    }

    return answer;
  }
}
