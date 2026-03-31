class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    valid_nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    def checkSegment(s: List[str]) -> bool:
      seen = set()
      for v in s:
        if v == '.':
          continue
        if v not in valid_nums:
          return False
        if v in seen:
          return False
        seen.add(v)
      return True

    # test lines
    for i in range(9):
      if not checkSegment(board[i]):
        return False

    # test columns
    for i in range(9):
      segment = [x[i] for x in board]
      if not checkSegment(segment):
        return False

    # test boxes
    for x in range(0, 9, 3):
      for y in range(0, 9, 3):
        segment = []
        for xi in range(x, x+3):
          for yi in range(y, y+3):
            segment.append(board[yi][xi])

        if not checkSegment(segment):
          print("failed box ", x, y)
          return False

    return True

