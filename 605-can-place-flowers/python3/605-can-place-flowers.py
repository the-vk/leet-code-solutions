class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
      first, last = 0, len(flowerbed)-1
      for i in range(len(flowerbed)):
        if n > 0 and (flowerbed[i] == 0) and (i == first or flowerbed[i-1] == 0) and (i == last or flowerbed[i+1] == 0):
          flowerbed[i] = 1
          n -= 1
        if n == 0:
          return True
      return False