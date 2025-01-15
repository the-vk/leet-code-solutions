class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def bitCount(num: int) -> int:
            res = 0
            while num > 0:
                if num % 2 == 1:
                    res += 1
                num = num // 2
            return res

        n1 = bitCount(num1)
        n2 = bitCount(num2)

        x = 0
        b = 0
        for i in range(math.ceil(math.log2(max(num1, num2))), -1, -1):
            if num1 & (1 << i) != 0:
                x = x | (1 << i)
                b += 1
            if b == n2:
                return x
            if b == n1:
                break
        i = 0
        while b < n2:
            if x & (1 << i) == 0:
                x = x | (1 << i)
                b += 1
            i += 1
        return x
                    
        