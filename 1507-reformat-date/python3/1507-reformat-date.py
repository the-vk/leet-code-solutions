import datetime

MONTH = {
  'Jan': 1,
  'Feb': 2,
  'Mar': 3,
  'Apr': 4,
  'May': 5,
  'Jun': 6,
  'Jul': 7,
  'Aug': 8,
  'Sep': 9,
  'Oct': 10,
  'Nov': 11,
  'Dec': 12
}

class Solution:
    def reformatDate(self, date: str) -> str:
      parts = date.split()
      day = int(parts[0][:-2])
      month = MONTH[parts[1]]
      year = int(parts[2])
      return datetime.date(year, month, day).strftime('%Y-%m-%d')