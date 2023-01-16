class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        lettersPerCycle = max(2 * numRows - 2, 1)
        columnsPerCycle = max(numRows - 1, 1)
        cycles = len(s) // lettersPerCycle + 1
        matrix = [ [None for x in range(cycles * columnsPerCycle)] for y in range(numRows)]
        for i in range(len(s)):
            y = i % lettersPerCycle
            if y >= numRows:
                y = lettersPerCycle - y
            x = i % lettersPerCycle
            if x < numRows:
                x = 0
            else:
                x = x - numRows + 1
            matrix[y][x + (i // lettersPerCycle * columnsPerCycle)] = s[i]
        result = ""
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] != None:
                    result+= matrix[y][x]
        return result