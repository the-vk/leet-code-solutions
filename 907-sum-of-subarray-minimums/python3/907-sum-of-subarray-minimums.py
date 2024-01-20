class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    modulo = 10**9 + 7
    n = len(arr)
    stack = []
    left = [-1] * n
    right = [n] * n
    for i in range(n):
      while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
      if stack:
        left[i] = stack[-1]
      stack.append(i)
    stack = []
    for i in range(n-1, -1, -1):
      while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
      if stack:
        right[i] = stack[-1]
      stack.append(i)

    return sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % modulo