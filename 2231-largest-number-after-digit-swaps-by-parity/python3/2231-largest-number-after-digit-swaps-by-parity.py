class Solution:
    def largestInteger(self, num: int) -> int:
        arr = [int(v) for v in list(str(num))]
        for i in range(len(arr)-1):
          for j in range(i+1, len(arr)):
            l = arr[i]
            r = arr[j]
            if (l % 2) == (r % 2) and l < r:
              arr[i], arr[j] = arr[j], arr[i]
        return int(''.join([str(v) for v in arr ]))

