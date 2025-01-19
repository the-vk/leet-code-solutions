class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits) - 1
        if n == -1:
            return []
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def nestedLoops(prefix, i):
            l = letters[digits[i]]
            for x in l:
                s = prefix + x
                if i == n:
                    res.append(s)
                else:
                    nestedLoops(s, i+1)
        nestedLoops('', 0)
        return res
