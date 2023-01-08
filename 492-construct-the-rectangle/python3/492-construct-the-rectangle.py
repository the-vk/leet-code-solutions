import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(math.floor(math.sqrt(area)))
        w = area / l
        while w % 1 != 0:
            l += 1
            w = area / l
        return [int(max(w, l)), int(min(w, l))]
